
import os
from Chain import *
from praw import *

# Important!!!
# Have the Praw module installed and fill in the OAuth2 authorization information below

Client_id = ''
Client_secret = ''
User_agent = ''
Password = ''
Username = ''


def toLetters(text):
    output = ''
    for x in text:
        n = ord(x)
        if n==32 or n==46 or 47<n<58 or 64<n<91 or 96<n<123:
            output += x
    return output

class RedditMarkov:
    def __init__(self, subreddit, numPosts=20):
        self.subreddit = subreddit
        self.filteredPosts = ''
        self.lettersAndNumsOnly = True

        if self.subreddit[:2] == 'T_':
            self.useCommentData = False
            self.subreddit = self.subreddit[2:]
            self.numPosts = 60
        else:
            self.useCommentData = True
            self.numPosts = numPosts

    def generate(self, genAmount):
        reddit = Reddit(client_id=Client_id, client_secret=Client_secret, password=Password,
                        user_agent=User_agent, username=Username)
        reddit.read_only = True # makes the program like 2x faster

        sub = reddit.subreddit(self.subreddit)
        posts = sub.top(limit = self.numPosts)

        chain = Chain()

        for post in posts:
            if not post.stickied and not post.title in self.filteredPosts and not 'battleforthenet' in post.url:
                # print(post.title)

                if not self.useCommentData:
                    post = toLetters(post.title)
                    chain.add_words(post)
                    continue

                comments = post.comments
                for i, comment in enumerate(comments):
                    if i>=6: break
                    comment = comment.body.replace('\n', ' ')
                    if self.lettersAndNumsOnly:
                        comment = toLetters(comment)
                    if not 'https' in comment:
                        # print(30*'-')
                        # print(comment)
                        chain.add_words(comment)

        filename = 'r_' + self.subreddit + '.xml'
        output = open(filename, 'w+')

        if self.useCommentData:
            output.write('r_'+self.subreddit)
        else:
            output.write('T r_' + self.subreddit)

        # print(30*'=')
        for x in range(genAmount):
            output.write('\n'+chain.gen_messge())
            # print(message)

    def addFilter(self, filteredPosts):
        self.filteredPosts = ' '.join(filteredPosts)

    def open(self):
        os.startfile('r_'+self.subreddit+'.xml', 'open')
