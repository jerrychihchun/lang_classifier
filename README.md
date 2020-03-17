# Language Classifier
for English, French, German, Italian, and Spanish.

This trigram-based language classifier is built **without importing libraries** for English (en), French (fr), German (de), Italian (it), and Spanish (es). Text normalization involves only lowercasing and removing digits and puncutations. The classifcation predicts also a 6th category, i.e. Other. 

## Training
The trigram dictionary is built based on 
the latest Wikipedia size 10k corpus from the download page
https://wortschatz.uni-leipzig.de/en/download/
provided by the Leipzig Corpora Collection.

When necessary, run ```python trigram_dictionary.py``` to create a dicionary give text files in the training folder.

## Development
The UE langauge policy statements of 24 langauges for developing/testing can be found in folder dev. 
The English version for example is available at https://www.europarl.europa.eu/factsheets/en/sheet/142/language-policy. Details of langauge codes can be found at https://publications.europa.eu/code/en/en-5000800.htm.

## Classification
Execute ```python lang_classifier.py```.
Should the dict.txt file not be found, execute ```python trigram_dictionary.py``` to re-create it.
Given a document file name, the prediction goes through unique present trigrams while accumulating scores for each category.
The scores are normalized across langauges with respective divisor. Further details can be found in the script for treating an out-of-vocabulary trigram and counting the score for *Other*.

## Dev. Results

### Romance
| Language  | Score |
| ------------- | ------------- |
| French  | .285 |
| Italian  | .276 |
| Spanish | .283 |
| Portuguese | .249 (Other) |
| Romanian | .281 (Other) |

### Germanic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- |
| English  | **0.242** |  0.167 |  0.1   |  0.147 |  0.117  | 0.227 |
| German  | 0.09  |  0.094 |  **0.448** |  0.092 |  0.076 |  0.201 |
| Danish | 0.182 |  0.136 |  0.158 |  0.144 |  0.108  | **0.272** |
| Dutch | 0.149 |  0.13  |  0.233 |  0.136 |  0.109  | **0.243** |
| Swedish | 0.177 |  0.133 |  0.14  |  0.154 |  0.109 |  **0.287** |
