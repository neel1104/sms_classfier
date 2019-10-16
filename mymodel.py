import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from wordcloud import WordCloud

df = pd.read_csv('sanitizedata.txt', '\t', nrows=203)
# Sentiment_count = df.groupby('Sentiment').count()

# plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
# plt.xlabel('Review Sentiments')
# plt.ylabel('Number of Review')
# plt.show()

tf = TfidfVectorizer()
text_tf = tf.fit_transform(df['message'])

X_train, X_test, y_train, y_test = train_test_split(text_tf, df['debit'], test_size=0.3, random_state=1)

clf = MultinomialNB().fit(X_train, y_train)
predicted = clf.predict(X_test)
print("MultinomialNB Accuracy:", metrics.accuracy_score(y_test, predicted))

