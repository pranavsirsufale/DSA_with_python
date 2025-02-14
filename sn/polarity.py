from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk


###??? Download VADER lexicon ( required for the first time )
nltk.download('vader_lexicon')

def polarity_textblob(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity 



def polarity_vader(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    return score['compound']


texts = [
    'I love this product ! It\'s absolutely amazing. ',
    "this is the worst movie I have ever seen.",
    "The food was okay, nothing Special ",
    "I am so happy today!",
    'The service was not good , but the staff was friendly'
]









