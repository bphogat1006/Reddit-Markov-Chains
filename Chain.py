
import random
import re

class Chain:
    def __init__(self, text=''):
        self.chain = {}
        self.chainStart = []
        self.chainEnd = []
        self.add_words(text)

    def add_words(self, text):

        text += '.'
        sentences = [x for x in text.replace('\n', '').split('.') if x != '']

        for sent in sentences:
            # sentence = re.sub(r'\b\n\n\b', 'robert', sentence)
            words = [x for x in sent.split(' ') if x != '']

            for i, v in enumerate(words):
                if not v in self.chain:
                    self.chain[v] = []

                if i==0:
                    self.chainStart.append(v)
                else:
                    self.chain[ words[i-1] ].append(v)

            if len(words) != 0:
                lastWord = words[-1]
                self.chainEnd.append(lastWord)
                self.chain[lastWord].append('')

    def gen_messge(self):
        message = [random.choice(self.chainStart)]

        while True:
            previousWord = message[len(message)-1]
            try:
                message.append( random.choice( self.chain[ previousWord ] ) )
                if message[-1] == '':
                    break
            except IndexError:
                break

        message[0] = message[0].capitalize()
        del message[-1]
        return ' '.join(message) + '.'