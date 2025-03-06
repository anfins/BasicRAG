

class Content:
    def __init__(self, filepath):
        with open(filepath, "r") as file:
            self.text = file.read()
        self.tokens = self.text.split()
        self.vocabulary = {}
        for token in self.tokens:
            if token in self.vocabulary:
                self.vocabulary[token] += 0
    

    def get_text(self):
        return self.text
    
    def get_tokens(self):
        return self.tokens

    def get_vocabulary(self):
        return self.vocabulary
    
    