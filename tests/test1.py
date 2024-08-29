# This file show the basic usage of the GPLWordNet package
# Two functions of the package are shown here

from GPLWordNet import example



# First, we will use the full_expand function
# This function takes a list of dictionaries as input, and returns a list of dictionaries
# This function is used for finding target words' antonyms, synsets, adjectives, derivational words, and hyponyms
data1 = [{'term': 'good', 'PoS': 'ADJECTIVE'}]
print(example.full_expand(data1))
print(example.full_expand(data1,syns=True))


data2 = [{'term': 'good', 'PoS': 'ADJECTIVE','sense': 1}]
# print(example.full_expand(data2))


# Second, we will use the antonyms_expand function
# This function takes a list of dictionaries as input, and returns a list of dictionaries
# This function is used for finding target words' antonyms
data3 = [{'term': 'good', 'PoS': 'NOUN', 'sense': 1},
        {'term': 'competence', 'PoS': 'Noun'}]
# print(example.antonyms_expand(data3))