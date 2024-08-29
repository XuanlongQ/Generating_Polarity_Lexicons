# The Usage of GPLWordNet

## Introduction
GPL WordNet (Generating Polarity Lexicions with WordNet) is a lexicon-generating tool that uses WordNet as a database to find two sets of lexicons.

It provides two basic function,
- Full expansion: This function is used to find target words' antonyms, synsets, adjectives, derivational words, and hyponyms.
- Antonyms expansion - This function is used for finding target words' antonyms.

This tool is an extended Python version of [Nicolas et al.'s dictionary-generating approach](https://gandalfnicolas.github.io/SADCAT/). As their team only provides the R version, it is quite hard to use. Therefore, I provide this Python version, and you can absolutely improve and self-define this package's function by git my code from [my GitHub](https://github.com/XuanlongQ/Generating_Polarity_Lexicons/tree/master).

## Function
1. example.full_expand()
2. example.antonyms_expand()

| Function Name | Features |
|:--|:-----|
|full_expand()|find target words' antonyms, synsets, adjectives, derivational words, and hyponyms|
|antonyms_expand()|find target words' antonyms|


## Agruments
### Input Parameters
#### 1. full_expand() function
| Parameter Name | Required | Type | Description |
|:--|:--:|:--:|:-----|
| datax  | Yes  | list  | A list where each dictionary contains 'term', 'PoS', and 'sense'. 'term' (str): The word to expand.'PoS' (str): Part of Speech ('NOUN', 'VERB', 'ADJECTIVE').The specific sense index to use for the term(False,single words; True, synsets).|
| antonym  | No  | bool  | Whether to include antonyms in the expansion. Defaults to True.  |
| syns  | No  | bool  | Whether to return synsets. Defaults to False.|

**Notes: Only key 'term' is compulsory.**

#### 2. antonyms_expand() function
| Parameter Name | Required | Type | Description |
|:--|:--:|:--:|:-----|
| datax  | Yes  | list  | A list where each dictionary contains 'term', 'PoS', and 'sense'. 'term' (str): The word to expand.'PoS' (str): Part of Speech ('NOUN', 'VERB', 'ADJECTIVE').The specific sense index to use for the term(False,single words; True, synsets).|
| syns  | No  | bool  | Whether to return synsets. Defaults to False.|

**Notes: Only key 'term' is compulsory.**

### Output Parameters
#### 1. full_expand() function
| Parameter Name  | Type | Description |
|:--|:--:|:-----|
|You called function|list|A list of unique words or synsets, expanded from the input terms based on the specified relationships.

#### 2. antonyms_expand() function
| Parameter Name  | Type | Description |
|:--|:--:|:-----|
|You called function|list|A list of unique words or synsets, expanded from the input terms based on the specified relationships.

## Example
### 1. full_expand() function

Basic function
```{python}
data = [{'term': 'good'}]
print(example.full_expand(data))
```

```{python}
data = [{'term': 'good', 'PoS': 'ADJECTIVE'}]
print(example.full_expand(data))
```

Extra Parameters
```{python}
data = [{'term': 'good', 'PoS': 'ADJECTIVE'}]
print(example.full_expand(data,syns=True,antonym=False))
```

### 2.antonyms_expand() function

Basic function
```{python}
data = [{'term': 'good', 'PoS': 'ADJECTIVE'}]
print(example.antonyms_expand(data))
```

Extra Parameters
```{python}
data = [{'term': 'good', 'PoS': 'ADJECTIVE'}]
print(example.antonyms_expand(data,syns=True))
```

## Supplemantal Materials
1. This work is an replication work of Nicolas' SADCAT codes, which only have R version. For more details about Nicolas Works, please refer to following link,
   - [Nicolas dictonaries Webpage.](https://gandalfnicolas.github.io/SADCAT/)
   - [Nicolas GitHub.](https://github.com/gandalfnicolas/SADCAT)

2. The approach I mainly learned from Maks et al.'s(2014) Paper.
   - [Generating Polarity Lexicons with WordNet propagation in five languages.](http://www.lrec-conf.org/proceedings/lrec2014/pdf/847_Paper.pdf)

## Call for Contributions
The GPLWordNet project welcomes your expertise and enthusiasm!

Small improvments of fixes are always appreciated, please submit your feature [according GitHUb](https://github.com/XuanlongQ/Generating_Polarity_Lexicons/tree/master).

Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact my public email at xuanlongqin.cu@gmail.com . 

## Acknowledge
I would like to sincerely thank my dear Ling Yan, who spent three hours accompanying me and watching TV series alone during this period, supporting me to complete this project.
