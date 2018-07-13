class Score(object):

    @staticmethod
    def get_chen_formula_score(self, card1, card2):
        score = 0
        
        card1_value = card1.get_value()
        card2_value = card2.get_value()
        
        card1_suit = card1.get_suit()
        card2_suti = card2.get_suit()
        
        high_value = max(card1_value, card2_value)
        if high_value == 14:
            score += 10
        elif high_value == 13:
            score += 8
        elif high_value == 12:
            score += 7
        elif high_value == 11:
            score += 6
        else:
            score += (high_value/float(2))
        
        # min score for a pair is 5
        if card1_value == card2_value:
            score *= 2
            if score < 5:
                score = 5
        
        if card1_suit == card2_suti:
            score += 2
        
        
        diff = abs(card1_value - card2_value)
        if diff == 1:
            score += 1
        elif diff == 2:
            score -= 1
        elif diff == 3:
            score -= 2
        elif diff == 4:
            score -= 4
        else:
            score -= 5
            
        return score