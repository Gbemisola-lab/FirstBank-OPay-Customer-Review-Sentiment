"""
Project: Fintech vs Traditional Bank Sentiment Analysis
Description: Scrapes and analyzes Google Play reviews for First Bank and OPay apps.
Author: Gbemisola Abolade
Date: 2025-05-20
"""

from google_play_scraper import reviews, Sort
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

print("Scraping reviews...")

firstbank_reviews, _ = reviews(
    'com.firstbank.firstmobile',  # First Bank app package name
    lang='en',
    country='ng',
    sort=Sort.NEWEST,
    count=300,
)

opay_reviews, _ = reviews(
    'team.opay.pay',
    lang='en',
    country='ng',
    sort=Sort.NEWEST,
    count=300,
)

firstbank_df = pd.DataFrame(firstbank_reviews)
opay_df = pd.DataFrame(opay_reviews)

print("\nFirst Bank Columns:", firstbank_df.columns)
print("OPay Columns:", opay_df.columns)

positive_keywords = ['easy', 'great', 'good', 'fast', 'love', 'excellent', 'awesome', 'quick']
negative_keywords = ['bad', 'poor', 'slow', 'worst', 'terrible', 'issue', 'problem', 'blocked', 'error']

def classify_sentiment(text):
    text = str(text).lower()
    if any(word in text for word in positive_keywords):
        return 'Positive'
    elif any(word in text for word in negative_keywords):
        return 'Negative'
    else:
        return 'Neutral'

if 'content' in firstbank_df.columns:
    firstbank_df['sentiment'] = firstbank_df['content'].apply(classify_sentiment)
else:
    print("\n❌ First Bank data is missing or doesn't have the 'content' column.")

if 'content' in opay_df.columns:
    opay_df['sentiment'] = opay_df['content'].apply(classify_sentiment)

if 'sentiment' in firstbank_df.columns:
    print("\nFirst Bank Sentiment Breakdown:")
    print(firstbank_df['sentiment'].value_counts())

if 'sentiment' in opay_df.columns:
    print("\nOPay Sentiment Breakdown:")
    print(opay_df['sentiment'].value_counts())

if 'sentiment' in firstbank_df.columns:
    firstbank_df['sentiment'].value_counts().plot(kind='bar', title='First Bank Review Sentiment', color='orange')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.show()
    plt.close()

if 'sentiment' in opay_df.columns:
    opay_df['sentiment'].value_counts().plot(kind='bar', title='OPay Review Sentiment', color='green')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.show()
    plt.close()

if 'content' in firstbank_df.columns:
    firstbank_text = ' '.join(firstbank_df['content'].dropna().astype(str))
    firstbank_wc = WordCloud(width=800, height=400, background_color='white').generate(firstbank_text)
    plt.imshow(firstbank_wc, interpolation='bilinear')
    plt.title('First Bank Word Cloud')
    plt.axis('off')
    plt.show()
    plt.close()

if 'content' in opay_df.columns:
    opay_text = ' '.join(opay_df['content'].dropna().astype(str))
    opay_wc = WordCloud(width=800, height=400, background_color='white').generate(opay_text)
    plt.imshow(opay_wc, interpolation='bilinear')
    plt.title('OPay Word Cloud')
    plt.axis('off')
    plt.show()
    plt.close()


firstbank_df.to_csv('firstbank_reviews_with_sentiment.csv', index=False)
opay_df.to_csv('opay_reviews_with_sentiment.csv', index=False)

print("\n✅ Reviews and sentiment analysis complete. CSVs saved.")

