
from RedditMarkov import *

subreddit = input("What subreddit would you like to generate comments from?\n(Exclude the \"r/\")\n")

try:
    RedditMarkov(subreddit).generate(1000);
    print('SUCCESS', subreddit)
except Exception as e:
    print('FAILED', e, subreddit)
