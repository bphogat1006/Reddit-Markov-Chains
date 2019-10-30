# Markov Chains implementation with Reddit API

Markov chains are a very basic form of machine learning. It is a process that uses any given text (eg. An Edgar Allen Poe story) to generate new sentences. The Markov chain finds patterns of what words commonly follows others, and uses that information to construct completely new sentences.

## Project Info

### Chain.py
This module contains the Chain class which takes one parameter, called 'data.' It implements the Markov process to generate new sentences using the sample text from the 'data' parameter. The Chain class can be used in any Markov chain project you want.

### RedditMarkov.py
A creative use of Markov Chains is creating human-like comments. My inspiration for this came from a similar project found [here](https://www.reddit.com/r/SubredditSimulator/comments/3g9ioz/what_is_rsubredditsimulator/). The website Reddit.com has many communities called 'Subreddits,' where people discuss different topics, ranging from [world news](https://www.reddit.com/r/worldnews/) to [stapling bread on trees](https://www.reddit.com/r/BreadStapledToTrees/). The variety of topics makes it interesting to apply the Markov process to different Subreddits. This module uses Markov chains to analyze hundreds of existing comments on a specific Subreddit, and generate hundred of new ones.
RedditMarkovTester.py is an example of how to use this module. It asks the user for the Subreddit name and then generates new comments from it. The generated comments are created in an xml file in the same directory after the program finishes.

It can take up to a minute to run this program, depending on your internet connection.

## Instructions

### Chain.py
For an example of how to use this module, see "ChainTester.py"
The Chain class constructor takes one parameter, called 'data.' The Markov Chain uses the text you put in for this parameter to generate new sentences.
To add more data after you create an instance of the Chain class, use the method 'add_words.'
The method 'gen_message' returns one auto-generated sentence from the given data using the Markov process.

### RedditMarkov.py
#### Setup
Important!!!
For this module to work:

First, have the "Praw" python package installed. Use pip for an easy installation.
`pip install praw`

Next, you have to set up your Reddit API so Praw has a way to get the data
Go to https://www.reddit.com/ and sign in
Next, go to https://www.reddit.com/prefs/apps/
Scroll down and press "create another app"
Give it a name, and enter "http://localhost:8080" in the "redirect uri" text box
Press create app

**In RedditMarkov.py, fill in the five variables at the beginning of the program with the necessary information, as described below**

###### (retrieved from the Praw documentation)
```
client_id:          The client ID is the 14 character string listed just under “personal use script” for the desired developed application
client_secret:      The client secret is the 27 character string listed adjacent to secret for the application.
user_agent:         The name you gave your application
password:           The password for the Reddit account used to register the script application.
username:           The username of the Reddit account used to register the script application.
```

#### How to use it
Import the RedditMarkov module. Create a new instance of the RedditMarkov class, which takes in the Subreddit name as a parameter. When typing the Subreddit name, exclude the "r/" from it. Then use the "generate" method to generate new comments based on that subreddit. The generate method takes a genAmount parameter, which is the number of new comments to be generated.
For an example of how to use this module, see "RedditMarkovTester.py"

## Author

**Bhavya Phogat** - https://github.com/bphogat1006



