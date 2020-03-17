'''
This trigram dictionary is built based on 
the latest Wikipedia size 10k corpus from the download page
https://wortschatz.uni-leipzig.de/en/download/
provided by the Leipzig Corpora Collection.
'''
punctuation = set('''!()-[]{};:'",<>./?@#$%^&*_~''') #or import string.punctuation

# Given a filename with extension performs a simple tokenization
def tokenize(filename):
    lang = []
    with open(filename, encoding='utf-8', mode = 'r') as file:
        text = file.read()
    text = ''.join(ch for ch in text if ch not in punctuation)
    return [token.lower() for token in text.split() if token.isalpha() and len(token) > 2] #preparing for trigrams
# Given a list of tokens returns a list of present trigrams
def to_trigrams(token_list):
    trigrams = []
    for token in token_list:
        for i in range(len(token)-2): #language: lan, ang, ..., age
            trigrams.append(token[i:i+3])
    return trigrams

# Acquire types only to save training time
en = set(tokenize('training/eng_wikipedia_2016_10K-sentences.txt'))
fr = set(tokenize('training/fra_wikipedia_2010_10K-sentences.txt'))
de = set(tokenize('training/deu_wikipedia_2016_10K-sentences.txt'))
it = set(tokenize('training/ita_wikipedia_2016_10K-sentences.txt'))
es = set(tokenize('training/spa_wikipedia_2016_10K-sentences.txt'))

en_grams = to_trigrams(en) #0
fr_grams = to_trigrams(fr) #1
de_grams = to_trigrams(de) #2
it_grams = to_trigrams(it) #3
es_grams = to_trigrams(es) #4

grams = set(en_grams + fr_grams + de_grams + it_grams + es_grams) #vocabulary = set of trigram types
vocabulary = {}
for gram in grams: #going through each trigram and record occurences
	counts = [en_grams.count(gram), fr_grams.count(gram), de_grams.count(gram), it_grams.count(gram), es_grams.count(gram)]
	if sum(counts) > 3: #prevent foreign texts
		vocabulary[gram] = counts

# Save the built dictionary for the classifier
f = open('dict.txt', encoding='utf-8', mode = 'w')
f.write(str(vocabulary))
f.close()