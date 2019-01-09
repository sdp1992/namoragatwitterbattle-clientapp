# NaMoRaGaTwitterBattle-ClientApp
Sentiment analysis of Tweets for Narendra Modi and Rahul Gandhi refreshed at 15 seconds.
This application demonstrated how people are talikng about them in Twitter.

### Deplyoed at Google App Engine
### Python Version: Python 2.7

### Architecture:
Filtered data from Twitter API -> Push tweets to Kafka topic -> Get sentiment of tweets from trained Tensorflow model -> Aggregate count based on sentiment each 15 seconds

