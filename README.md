# Language Classifier for English, French, German, Italian, and Spanish

This trigram-based language classifier is built *without importing libraries* for English (en), French (fr), German (de), Italian (it), and Spanish (es). Text normalization involves only lowercasing and removing digits and puncutations. The classifcation predicts also a 6th category, i.e. Other.

## Training
The trigram dictionary is built based on 
the latest Wikipedia size 10k corpus from the download page
https://wortschatz.uni-leipzig.de/en/download/
provided by the Leipzig Corpora Collection. When necessary, run ```python trigram_dictionary.py``` to create a dicionary give text files in the training folder.

## Development
The UE langauge policy statements of 24 langauges for developing/testing can be found in folder dev. 
The English version for example is available at https://www.europarl.europa.eu/factsheets/en/sheet/142/language-policy. 

## Classification
Execute ```python lang_classifier.py```. 
Should the dict.txt file not be found, execute ```python trigram_dictionary.py``` to re-create it.
