'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)

listpolarity = []
listsubjectivity = []

i = 0
for tweet in tweetData:
    blob = TextBlob(tweet["text"])
    listpolarity.append(blob.polarity)
    listsubjectivity.append(blob.subjectivity)
    i += 1
print(listpolarity)
print (listsubjectivity)

total1 = sum(listpolarity)
length1 = len(listpolarity)
avg1 = total1 / length1
print(avg1)

total2 = sum(listsubjectivity)
length2 = len(listsubjectivity)
avg2 = total2 / length2
print(avg2)

badwords = ["and", "or", "not", "to", "this", "they", "when", "why", "https", "too", "then",
            "if", "for"]
#tweets1 = ""
#i = 0
#for i in tweetData:
#    stuff = (i["text"])
#    tweets1 += stuff
#    i += 1

#tb = Textblob(tweets1)
 #for word in tweets1:
    # if word in badwords


plt.title("Polarity Histogram")
plt.xlabel("polarity")
plt.ylabel("amount")
plt.axis([-1.00, 1.00, 0, 60])
plt.grid(True)
plt.hist(listpolarity, bins = 5, linewidth = 1.5, edgecolor = 'black')
plt.show()

plt.title("Subjectivity Histogram")
plt.xlabel("subjectivity")
plt.ylabel("amount")
plt.axis([-1.00, 1.00, 0, 60])
plt.grid(True)
plt.hist(listsubjectivity, bins = 5, linewidth = 1.5, edgecolor = 'black')
plt.show()



plt.scatter(listpolarity, listsubjectivity)
plt.axis([-1.00, 1.50, -0.5, 1.5])
plt.show()

tweets1 = ', '.join(tweet['text']for tweet in tweetData)
tb = TextBlob(tweets1)
filtered_words = []
#print(tweets1)


bigblob = TextBlob(tweets1)
filterd = {}
wordsList = bigblob.words


for word in wordsList:
    if len(word)> 3:
        continue
    if not word.isalpha():
        continue
    if word.lower() in badwords:
        continue

    #(tweet["text"]

    filterd[word] = bigblob.word_counts[word]
wordcloud = WordCloud().generate(tweets1)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
