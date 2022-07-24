# Tatoeba Tools

These scripts use the sentences.csv and links.csv files, which can be downloaded from [Tatoeba](https://tatoeba.org/en/downloads). The sentences_detailed.csv file can be used instead of the sentences.csv file. Unused lines in these files can be deleted to improve performance.

## Balance

These are scripts that try to create subcorpora of Tatoeba that are more balanced in terms of vocabulary. A language must be specified. Search the internet for frequency lists to create a dictionary file.

### balance-s

`balance-s` requires a language that uses spaces, but doesn't require a dictionary file. The arguments are: language, sentences file, and output file.
```
python balance-s.py eng sentences.csv balanced.csv
```
### balance-ds
`balance-ds` requires a language that uses spaces and requires a dictionary file. The arguments are: language, dictionary file, sentences file, and output file.
```
python balance-ds.py eng dictionary.csv sentences.csv balanced.csv
```
### balance-d
`balance-d` doesn't require a language that uses spaces, but requires a dictionary file. It's slower than the other two scripts. The arguments are: language, dictionary file, sentences file, and output file.
```
python balance-d.py eng dictionary.csv sentences.csv balanced.csv
```
## Untranslated

`untranslated` is a script that lists all sentences in a given language that don't have any direct or indirect translations into some other given language. It also generates an intermediate file to save on memory usage. The arguments are: source language, target language, links file, sentences file, intermediate output file, and final output file.
```
python untranslated.py deu eng links.csv sentences.csv intermediate.csv output.csv
```
