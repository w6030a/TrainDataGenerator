class Card(object):

    def __init__(self, value, suit):
        #TODO parse
        self.value = value
        self.suit = suit
        
    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    @staticmethod
    def parse(string):
        pass