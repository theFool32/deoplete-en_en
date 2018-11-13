from .base import Base
import json

class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'en_en'
        self.mark = '[en_en]'
        self.min_pattern_length = 1
        self.filetypes = ['tex']
        path = '/'.join(__file__.split('/')[:-1])
        with open(path+'/en-en-dict.json', 'r') as f:
            self.dict = json.load(f)
        self.words = self.dict.keys()

    def gather_candidates(self, context):
        prefix = context['complete_str']
        words = filter(lambda w: w.startswith(prefix), self.words)
        return  [
                {'word': w, 'info': self.dict[w]['description']} for w in words
                ]
