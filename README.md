# Tatoeba Tools

These scripts use the sentences.csv, sentences_detailed.csv, links.csv, and user_languages.csv files, which can be downloaded from [this Tatoeba page](https://tatoeba.org/en/downloads).
The sentences_detailed.csv file can be used instead of the sentences.csv file, but not vice-versa.
Unused lines in these files can be deleted to improve performance.

## Balance

These are scripts that try to create subcorpora of Tatoeba that are more balanced in terms of vocabulary.
A language must be specified.
Search the internet for frequency lists to create a dictionary file.

### balance-s

`balance-s.py` requires a language that uses spaces, but doesn't require a dictionary file.
The arguments are: language, sentences file, and output file.
```
python balance-s.py eng sentences.csv balanced.csv
```
### balance-ds
`balance-ds.py` requires a language that uses spaces and requires a dictionary file.
The arguments are: language, dictionary file, sentences file, and output file.
```
python balance-ds.py eng dictionary.csv sentences.csv balanced.csv
```
### balance-d
`balance-d.py` doesn't require a language that uses spaces, but requires a dictionary file.
It's slower than the other two scripts.
The arguments are: language, dictionary file, sentences file, and output file.
```
python balance-d.py eng dictionary.csv sentences.csv balanced.csv
```
## Native

`native.py` is a script that filters all sentences written by native speakers.
The arguments are: languages file, detailed sentences file, and output file.
```
python native.py user_languages.csv sentences_detailed.csv native.csv
```

## Untranslated

`untranslated.py` is a script that lists all sentences in a given language that don't have any direct or indirect translations into some other given language.
It also generates an intermediate file to save on memory usage.
The arguments are: source language, target language, links file, sentences file, intermediate output file, and final output file.
```
python untranslated.py deu eng links.csv sentences.csv adjacency.csv untranslated.csv
```
