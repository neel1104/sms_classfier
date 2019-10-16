import nltk
from nltk.tokenize import sent_tokenize # sentence tokenisation
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

import matplotlib.pyplot as plt

# nltk.download('punkt') # need to be run only once

text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""

# tokenized_text = sent_tokenize(text)
# print(tokenized_text)

tokenized_word = word_tokenize(text)

# fdist = FreqDist(tokenized_word)
# print(fdist.most_common(2))

# fdist.plot(30,cumulative=False)
# plt.show()

# nltk.download('stopwords') # need to be run only once
stop_words = set(stopwords.words('english'))
# print(stop_words)
# print(tokenized_word)

filtered_sent = []
for w in tokenized_word:
  if w not in stop_words:
    filtered_sent.append(w)

# print("filtered sentence: ", filtered_sent)
ps = PorterStemmer()

stemmed_words = []
for w in filtered_sent:
  stemmed_words.append(ps.stem(w))

# print("filtered sentence: ", filtered_sent)
# print("stemmed sentence:", stemmed_words)

# nltk.download('wordnet')  # need to be run only once

lem = WordNetLemmatizer()
stem = PorterStemmer()

word = "flying"
print("Lemmatized word", lem.lemmatize(word))
print("Stemmed word", stem.stem(word))