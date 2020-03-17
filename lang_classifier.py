'''
This language classifier is built without importing libraries
for English, French, German, Italian, and Spanish.
The UE langauge policy statements of 24 langauges for testing can be found in folder dev. 
The English version for example is available at 
https://www.europarl.europa.eu/factsheets/en/sheet/142/language-policy.
Text normalization involves only lowercasing and removing digits and puncutations.
The classifcation also predicts a 6th category, i.e. other.
Should the dict.txt file not be found, execute python trigram_dictionary.py to re-create it.
'''
punctuation = set('''!()-[]{};:'",<>./?@#$%^&*_~''') #or import string.punctuation
vocabulary = {}
with open('dict.txt', encoding='utf-8', mode = 'r') as dictionary:
    vocabulary = eval(dictionary.read())

total_weights = [0 for _ in range(5)]
for gram in vocabulary:
    for i in range(5):
        total_weights[i] += vocabulary[gram][i]
avg_weight = sum(total_weights) / 5 #across languages
total_max = 0
for key in vocabulary:
    total_max += max(vocabulary[key])
avg_max = total_max / len(vocabulary) #across trigrams

# Given a list of tokens returns a list of present trigrams
def to_trigrams(token_list):
    trigrams = []
    for token in token_list:
        for i in range(len(token)-2):
            trigrams.append(token[i:i+3])
    return trigrams

# Given a list of numbers returns a softmax-normalized one 
def softmax(scores):
    denominator = 0
    e = 2.72 #or import numpy.exp
    for score in scores:
        denominator += e**(score*10/sum(scores)) #preventing overflow
    return [round(e**(score*10/sum(scores))/denominator, 3) for score in scores]    
# Loads a text file and returns it as a string
def read_text(filename):
    with open(filename, encoding='utf-8', mode = 'r') as file:
        return file.read()
# Given a string returns predictions across 5 languages + 1 other
def predict(text):
    text = ''.join(ch for ch in text if ch not in punctuation)
    text_tokens = [token.lower() for token in text.split() if token.isalpha() and len(token) > 2] #simple tokenization
    text_grams = to_trigrams(text_tokens)
    scores = [0 for _ in range(6)]
    for gram in set(text_grams): #going through unique present trigrams in the given text
        #divisor: normalize across languages; assume the avg. when trigram is OOV
        for i in range(5):
            scores[i] += vocabulary.get(gram, [0 for _ in range(5)])[i]*text_grams.count(gram) / total_weights[i] 
        if vocabulary.get(gram): #pick the second largest weight + 1/5 of its difference to the largest       
            counts = sorted(vocabulary[gram]) #across the 5 languages as an opposing force
            scores[5] += ((counts[-1] - counts[-2])/5 + counts[-2]) * text_grams.count(gram) / avg_weight
        else: 
            scores[5] += 5 * avg_max * text_grams.count(gram) / avg_weight 
            # five times the average max weight
    return softmax(scores)

print('Predict the document language as English, French, German, Italian, Spanish, or Other.')
while True:
	print('Enter a document file name with extention to predict its language (type \'q\' to quit):')
	filename = input()
	if filename.lower() == 'q':
	    break
	try:
	    text = read_text(filename)
	except OSError:
	    print ("Could not open/read file:", filename)
	    continue

	categories = ['EN', 'FR', 'DE', 'IT', 'ES', 'Other']
	print(*categories, sep = '\t')
	scores = predict(text)
	print(*scores, sep = '\t')
	lang_score = max(scores) 
	lang_index = 5 #assume other
	#or use: panda.idxmax(); numpy.argmax()
	for i in range(5):
		if lang_score == scores[i]:
			lang_index = i
			break #exit when argmax found
	print('The most likely langauge is:', categories[lang_index])
	print('The chance of being other langauge is:', scores[5])
