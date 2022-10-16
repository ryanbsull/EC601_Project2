import api_keys
import requests
import json
import os

def analyze_text(content):
    
    return os.popen('.{} ml language analyze-sentiment --content="{}"'.format(api_keys.GCLOUD_LOCATION, content)).read()


def get_tweets(query,tweet_fields,bearer_token = api_keys.BEARER_TOKEN, max_results = 10):

    header = {"Authorization": "Bearer {}".format(bearer_token)}
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&max_results={}".format(
        query, tweet_fields, max_results
    )
    ret = requests.request("GET", url, headers=header)

    if(ret.status_code != 200):
        print("AHHH")
        raise Exception(ret.status_code, ret.text)

    return ret.json()

def test_get_tweets():
    example = get_tweets("Liverpool", "tweet.fields=text", max_results=20)
    print(json.dumps(example, indent=4, sort_keys=True))
    return 0

def test_analyze_test():
    example = "I feel bad today"
    annotations = json.loads(analyze_text(example))
    print(annotations)
    print(type(annotations))
    magnitude = annotations["documentSentiment"]["magnitude"]
    score = annotations["documentSentiment"]["score"]
    print("Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude))

# TESTING FUNCTIONS FOR TWITTER AND GOOGLE NLP

#test_get_tweets()

#test_analyze_test()
