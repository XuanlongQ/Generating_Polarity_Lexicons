import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')


# Componetnts of the Package    
def get_syns(term: str, pos: str = "noun", sense: int = None, syns: bool = True):
    """
    
    Retrieves synsets or words for a given term, part of speech, and optionally a specific sense.


    Args:
        term (str): The word for which to retrieve synsets or associated words.
        pos (str, optional): The part of speech for the word. Options are 'NOUN', 'VERB', 'ADJECTIVE'. Defaults to 'noun'. 
        sense (int, optional): The specific sense index to retrieve. If None, retrieves all senses.. Defaults to None.
        syns (bool, optional):  Determines the type of return value. Defaults to True.

    Returns:
        list: A list of synsets or words based on the `syns` parameter.
    """
    try:
        # Map the PoS input to WordNet's format
        pos_map = {
            "NOUN": wn.NOUN,
            "VERB": wn.VERB,
            "ADJECTIVE": wn.ADJ
        }
        pos = pos_map.get(pos.upper(), wn.NOUN)

        # Retrieve synsets
        synsets = wn.synsets(term, pos=pos)

        # If a specific sense is desired
        if sense is not None and sense <= len(synsets):
            synsets = [synsets[sense - 1]]  # Adjust for 0-based index

        # Return either synsets or words
        if not syns:
            words = [lemma.name() for syn in synsets for lemma in syn.lemmas()]
            return list(set(words))
        else:
            return synsets

    except Exception as e:
        print(f"ERROR in get_syns: '{term}', PoS: '{pos}', sense: '{sense}' not found")
        return None
    
def get_antonyms(synsets, syns=True):
    """
    Expands a list of synsets by retrieving antonyms for each lemma within the synsets.


    Args:
        synsets (list): A list of synsets from which to find antonyms.
        syns (bool, optional): Determines the type of return value. Defaults to True.

    Returns:
        list: A list of unique antonyms, either as synsets or words, based on the `syns` parameter.
    """
    try:
        antonyms = []
        
        # Process each synset to find antonyms
        for synset in synsets:
            for lemma in synset.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.append(antonym.synset() if syns else antonym.name())
        
        # Remove duplicates
        antonyms = list(set(antonyms))
        
        return antonyms
        
    except Exception as e:
        print("ERROR in get_antonyms")
        return None

def get_derivrelto(synsets, syns=True):
    """
    Expands a list of synsets by retrieving derivationally related forms from the lemmas.

    Args:
        synsets (list): A list of synsets from which to find derivationally related forms.
        syns (bool, optional): Determines the type of return value.. Defaults to True.

    Returns:
        list: A list of unique derivationally related forms, either as synsets or words, based on the `syns` parameter.
    """
    try:
        derivationally_related = []

        # Process each synset to find derivationally related forms
        for synset in synsets:
            for lemma in synset.lemmas():
                for related_form in lemma.derivationally_related_forms():
                    derivationally_related.append(related_form.synset() if syns else related_form.name())

        # Remove duplicates
        derivationally_related = list(set(derivationally_related))

        return derivationally_related

    except Exception as e:
        print("ERROR in get_derivrelto")
        return None

def get_adj_expansion(synsets, syns=True):
    """
    Expands a list of synsets by retrieving related synsets through specific adjective relationships, 
    including "see also", "similar to", and "attributes".

    Args:
        synsets (list): A list of synsets to be expanded using their adjective relations.
        syns (bool, optional): Determines the type of return value. Defaults to True.

    Returns:
        list: A list of unique synsets or words based on the `syns` parameter, representing the expanded set.
    """
    try:
        expansion = []

        for synset in synsets:
            # See also
            seealso = synset.also_sees()
            # Similar
            similar = synset.similar_tos()
            # Attributes
            attribute = synset.attributes()
            
            # Combine all related synsets
            expansion.extend(seealso + similar + attribute)

        # Remove duplicates
        expansion = list(set(expansion))

        if not syns:
            # Return unique words if Syns is False
            return list(set(lemma.name() for syn in expansion for lemma in syn.lemmas()))
        else:
            return expansion

    except Exception as e:
        print("ERROR in get_adj_expansion")
        return None

def get_hypos(synsets, syns=True):
    """
    Expands a list of synsets by recursively retrieving all hyponyms, building a hierarchy of more specific terms.

    Args:
        synsets (list): A list of synsets to expand by retrieving their hyponyms.
        syns (bool, optional): Determines the type of return value.. Defaults to True.

    Returns:
        list: A list of unique hyponyms. The content of the list is determined by the `syns` parameter.
    """
    final_list = []
    
    try:
        while synsets:
            next_level = []
            for synset in synsets:
                hyponyms = synset.hyponyms()
                next_level.extend(hyponyms)
                final_list.extend(hyponyms)
            
            synsets = next_level
        
        if not syns:
            # Return unique words if Syns is False
            return list(set(lemma.name() for syn in final_list for lemma in syn.lemmas()))
        else:
            return list(set(final_list))

    except Exception as e:
        print("ERROR in get_hypos")
        return None

# Main component of the package
def full_expand(datax, antonym=True, syns=False):
    """
    Expands a list of seed words by retrieving related synsets or words based on several relationships
    like antonyms, derivationally related forms, adjective expansions, and hyponyms.

    Args:
        datax (list of dict): A list where each dictionary contains 'term', 'PoS', and 'sense'.
            - 'term' (str): The word to expand.
            - 'PoS' (str): Part of Speech ('NOUN', 'VERB', 'ADJECTIVE').
            - 'sense' (optional): The specific sense index to use for the term.
        antonym (bool, optional): Whether to include antonyms in the expansion. Defaults to True.
        syns (bool, optional): Whether to return synsets. Defaults to False.

    Returns:
        list: A list of unique words or synsets, expanded from the input terms based on the specified relationships.
    """
    
    # Validate input
    valid_pos = {'NOUN', 'VERB', 'ADJECTIVE'}
    for entry in datax:
        if not isinstance(entry, dict):
            raise ValueError("Each item in datax must be a dictionary.")
        
        if 'term' not in entry or not isinstance(entry['term'], str):
            raise ValueError("Each dictionary must contain a 'term' key with a string value.")
        
        if 'PoS' not in entry or entry['PoS'].upper() not in valid_pos:
            raise ValueError("Each dictionary must contain a 'PoS' key with value 'NOUN', 'VERB', or 'ADJECTIVE'.")
        
        if 'sense' in entry and not isinstance(entry['sense'], bool):
            raise ValueError("The 'sense' key, if present, must be a boolean value.")
    
    # main logistic
    WL = [synset for d in datax for synset in (get_syns(d['term'], d['PoS'], d.get('sense')) or [])]
    
    # WL = [get_syns(d['term'], d['PoS'], d.get('sense')) for d in datax] # you can also set it with 2-dimensional matrix

    if antonym:
        antonym_list = get_antonyms(WL)
        WL.extend(antonym_list)
        
    derivrelto_list = get_derivrelto(WL)
    WL.extend(derivrelto_list)
    

    adj_expansion_list = get_adj_expansion(WL)
    hypos_list = get_hypos(WL)
    WL.extend(adj_expansion_list)
    WL.extend(hypos_list)
    
    if antonym:
        hypos_antonym_list = get_antonyms(hypos_list)
        WL.extend(hypos_antonym_list)
    
    if not syns:
        # Flatten and get unique words
        WL = list(set(lemma.name() for synset in WL if synset for lemma in synset.lemmas()))
    else:
        # Flatten and get unique synsets
        WL = list(set(WL))
    
    return WL


def antonyms_expand(datax,syns = False):
    """
    Retrieves antonyms for a list of synsets derived from input terms, based on their part of speech
    and sense, with robust input validation.

    Args:
        datax (list of dict): A list where each dictionary contains 'term', 'PoS', and 'sense'.
            - 'term' (str): The word for which to find antonyms.
            - 'PoS' (str): Part of Speech ('NOUN', 'VERB', 'ADJECTIVE').
            - 'sense' (optional): The specific sense index to use for the term.
        syns (bool, optional): Determines the type of antonyms returned.
            - If True, returns a list of synsets corresponding to the antonyms.
            - If False, returns a list of unique words (lemmas) that are antonyms. Defaults to False.

    Returns:
        list: A list of antonyms, either as synsets or words, based on the `syns` parameter.
    """
    
    # Validate input
    valid_pos = {'NOUN', 'VERB', 'ADJECTIVE'}
    for entry in datax:
        if not isinstance(entry, dict):
            raise ValueError("Each item in datax must be a dictionary.")
        
        if 'term' not in entry or not isinstance(entry['term'], str):
            raise ValueError("Each dictionary must contain a 'term' key with a string value.")
        
        if 'PoS' not in entry or entry['PoS'].upper() not in valid_pos:
            raise ValueError("Each dictionary must contain a 'PoS' key with value 'NOUN', 'VERB', or 'ADJECTIVE'.")
        
        if 'sense' in entry and not (isinstance(entry['sense'], int) and entry['sense'] > 0):
            raise ValueError("The 'sense' key, if present, must have a positive integer value.")
    
    # main logistic
    
    WL = [synset for d in datax for synset in (get_syns(d['term'], d['PoS'], d.get('sense')) or [])]
    antonym_list = get_antonyms(WL,syns)
    return antonym_list
    
