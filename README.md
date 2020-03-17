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
The scores are normalized across langauges with respective divisor. Further details can be found in the script for treating out-of-vocabulary trigrams and counting the score for *Other*.

## Dev. Results

## Indo-European
### Romance
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| French  | 0.158 |  **0.285**  | 0.083 |  0.136 |  0.123 |  0.214 |
| Italian  | 0.147 |  0.139  | 0.084  | **0.276** |  0.129 |  0.224 |
| Spanish | 0.125 |  0.135 |  0.075 |  0.165 |  **0.283** |  0.217 |
| Portuguese | 0.13 |  0.147 |  0.078 |  0.172  | 0.224  | **0.249** |
| Romanian | 0.149 |  0.139 |  0.081 |  0.196 |  0.153 |  **0.281** |

### Germanic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| English  | **0.242** |  0.167 |  0.1   |  0.147 |  0.117  | 0.227 |
| German  | 0.09  |  0.094 |  **0.448** |  0.092 |  0.076 |  0.201 |
| Danish | 0.182 |  0.136 |  0.158 |  0.144 |  0.108  | **0.272** |
| Dutch | 0.149 |  0.13  |  0.233 |  0.136 |  0.109  | **0.243** |
| Swedish | 0.177 |  0.133 |  0.14  |  0.154 |  0.109 |  **0.287** |

### Slavic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Polish | 0.075 |  0.08  |  0.067 |  0.094  | 0.09  |  **0.594** |
| Czech | 0.083 |  0.081 | 0.062 |  0.103 |  0.091 |  **0.581** |
| Bulgarian | 0.0  |   0.0  |   0.0  |   0.0   |  0.0  |   **1.0** |
|	Croatian | 0.109  | 0.117  | 0.074  | 0.165  | 0.132 |  **0.402** |
| Slovak | 0.082 |  0.094 |  0.067  | 0.116 |  0.101 |  **0.539** |
|	Slovenian | 0.115 |  0.109 |  0.078 |  0.168 |  0.137 |  **0.393** |

### Greek
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Greek | 0.0  |   0.0  |   0.0  |   0.0   |  0.0  |   **1.0** |

### Baltic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Lithuanian | 0.121 |  0.141 |  0.091 |  0.153 |  0.132 |  **0.362** |
| Latvian | 0.076  | 0.092 |  0.057 |  0.094 |  0.1  |   **0.58** |

### Celtic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Irish | 0.132 |  0.139 |  0.15  |  0.099  | 0.107  | **0.372** |

## Uralic
### Ugric
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Hungarian | 0.072 |  0.088  | 0.07  |  0.102  | 0.082  |  **0.587** |
### Finnic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Finnish | 0.125 |  0.148  | 0.129 |  0.177 |  0.111  |  **0.311** |
| Estonian | 0.152 |  0.137 |  0.114 |  0.159 |  0.141 |  **0.297** |

## Afroasiatic
### Semitic
| Language  | EN   |   FR   |   DE   |   IT   |   ES   |   Other |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Maltese | 0.158 |  0.128 |  0.088 |  0.2   |  0.116  | **0.309** |

