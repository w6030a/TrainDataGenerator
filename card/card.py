class Card(object):

    def __init__(self, card_info):
        value, rank, suit = Card.parse(card_info)
        self.value = value
        self.rank = rank
        self.suit = suit
    
    def get_value(self):
        return self.value
    
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit
    
    @staticmethod
    def parse(card_info):
        value = card_info[0]
        rank = Card.value_to_rank(card_info[0])
        suit = card_info[1]
        
        return value, rank, suit
    
    @staticmethod
    def value_to_rank(card_value):
        if card_value == 'A':
            return 14
        elif card_value == 'K':
            return 13
        elif card_value == 'Q':
            return 12
        elif card_value == 'J':
            return 11
        elif card_value == 'T':
            return 10
        else:
            return int(card_value)
        