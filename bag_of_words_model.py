import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

df = pd.read_csv('./data/train.tsv', sep='\t', na_filter=False)
# Sentiment_count = df.groupby('Sentiment').count()

# plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
# plt.xlabel('Review Sentiments')
# plt.ylabel('Number of Review')
# plt.show()
token = RegexpTokenizer(r'[a-zA-Z0-0]+')
cv = CountVectorizer(lowercase=True, stop_words='english', tokenizer=token.tokenize, ngram_range= (1,1))
text_counts = cv.fit_transform(df['Phrase'])

X_train, X_test, y_train, y_test = train_test_split(text_counts, df['Sentiment'], test_size=0.3, random_state=1)

clf = MultinomialNB().fit(X_train, y_train)
predicted = clf.predict(X_test)
print("MultinomialNB Accuracy:", metrics.accuracy_score(y_test, predicted))
