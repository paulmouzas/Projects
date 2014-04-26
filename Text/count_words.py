class Words(object):
    def __init__(self, words):
        self.words = words
    def count(self):
        return len(self.words.split())
        
words = Words('here are a bunch or words')
count = words.count()
print count