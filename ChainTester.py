
from Chain import *

# Sample data can be anything
# This is a paragraph from Edgar Allen Poe's "The Tell-Tale Heart"
data = """
Now this is the point. You fancy me mad. Madmen know nothing. But you should have seen me. You should have seen how wisely I proceeded --with what caution --with what foresight --with what dissimulation I went to work! I was never kinder to the old man than during the whole week before I killed him. And every night, about midnight, I turned the latch of his door and opened it --oh so gently! And then, when I had made an opening sufficient for my head, I put in a dark lantern, all closed, closed, that no light shone out, and then I thrust in my head. Oh, you would have laughed to see how cunningly I thrust it in! I moved it slowly --very, very slowly, so that I might not disturb the old man's sleep. It took me an hour to place my whole head within the opening so far that I could see him as he lay upon his bed. Ha! would a madman have been so wise as this, And then, when my head was well in the room, I undid the lantern cautiously-oh, so cautiously --cautiously (for the hinges creaked) --I undid it just so much that a single thin ray fell upon the vulture eye. And this I did for seven long nights --every night just at midnight --but I found the eye always closed; and so it was impossible to do the work; for it was not the old man who vexed me, but his Evil Eye. And every morning, when the day broke, I went boldly into the chamber, and spoke courageously to him, calling him by name in a hearty tone, and inquiring how he has passed the night. So you see he would have been a very profound old man, indeed, to suspect that every night, just at twelve, I looked in upon him while he slept.
"""

# Create a new Chain object (a new Markov chain) with the given data
sampleMarkov = Chain(data)

# You can add more data to the Chain object after it is created if necessary
# Use the "add_words" method
#
# newData = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
# sampleMarkov.add_words(newData)


# Print information about the new Chain object
# all the Markov chain data
print(sampleMarkov.chain)
# the words that are used to start new sentences
print(sampleMarkov.chainStart)
# words that end sentences
print(sampleMarkov.chainEnd)


# create 10 new sentences using the given data
numberOfGeneratedSentences = 10

for i in range(numberOfGeneratedSentences):
    print( sampleMarkov.gen_messge() )
