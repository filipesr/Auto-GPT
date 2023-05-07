"""A module that contains a command to send a tweet."""
import os

import tweepy

from autogpt.commands.command import command

def send_tweet(tweet_text):
    consumer_key = os.environ.get("TW_CONSUMER_KEY")
    consumer_secret = os.environ.get("TW_CONSUMER_SECRET")
    access_token = os.environ.get("TW_ACCESS_TOKEN")
    access_token_secret = os.environ.get("TW_ACCESS_TOKEN_SECRET")
    bearer_token = os.environ.get("TW_BEARER_TOKEN")
    # Authenticate to Twitter
    client = tweepy.Client(bearer_token=bearer_token,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
    # Send tweet
    try:
        client.create_tweet(text=tweet_text)
        print("Tweet sent successfully!")
    except tweepy.TweepyException as e:
        return f"Error sending tweet: {e.reason}"
