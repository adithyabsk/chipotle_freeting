from YamJam import yamjam

from twitter.stream import TwitterStream
from twitter.oauth import OAuth

import subprocess

S_TWITTER = yamjam()["chipotle"]["twitter"]
CHIPOTLE_SNAME = "ChipotleTweets"
CHIPOTLE_ID = 141341662


def call_msg(code):
    subprocess.check_call(['./SendMessage.sh', '888222', code])


if __name__ == "__main__":
    auth = OAuth(
        S_TWITTER["access_token_key"],
        S_TWITTER["access_token_secret"],
        S_TWITTER["consumer_key"],
        S_TWITTER["consumer_secret"],
    )

    stream = TwitterStream(auth=auth)
    tweet_iter = stream.statuses.filter(follow=CHIPOTLE_ID)
    for tweet in tweet_iter:
        if tweet is not None and tweet.get('text'):
            tweet_txt = tweet['text']
            if (
                ('TERMS' in tweet_txt)
                and (tweet['user']['id'] == CHIPOTLE_ID)
            ):
                code = [s for s in tweet_txt.split(' ') if 'FREE' in s]
                if code:
                    call_msg(code[0])
