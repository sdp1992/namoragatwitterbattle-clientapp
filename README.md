# NaMoRaGaTwitterBattle-ClientApp
Sentiment analysis of Tweets for Narendra Modi and Rahul Gandhi refreshed at 15 seconds.
This application demonstrated how people are talikng about them in Twitter.

### Deplyoed at Google App Engine
### Python Version: Python 2.7

### Architecture:
Filtered data from Twitter API -> Push tweets to Kafka topic -> Get sentiment of tweets from trained Tensorflow model -> Aggregate count based on sentiment each 15 seconds

#### Check my other repos for end-to-end pipeline demonstration:

1. https://github.com/sdp1992/TwitterToKafka
2. https://github.com/sdp1992/KafkaToSparkStreaming
https://github.com/sdp1992/SentimentClassifier_TF

