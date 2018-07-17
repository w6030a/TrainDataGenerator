from __future__ import division
from card.card import Card
from card.score import Score
from holdem import holdem_calc
from holdem import holdem_argparser
from util.config import Config

class Record:

    def __init__(self):
        pass
        
    def set_table_info(self, table_info):
        self.table_id = table_info['tableNumber']
        self.stage = table_info['roundName']
        self.round_count = table_info['roundCount']
        self.raise_count = table_info['raiseCount']
        self.bet_count = table_info['betCount']
        self.total_bet = table_info['totalBet']
        self.init_chips = table_info['initChips']
        self.max_reload_count = table_info['maxReloadCount']
        self.board_card = table_info['board']
        self.small_blind = table_info['smallBlind']
        self.big_blind = table_info['bigBlind']
        
    def set_player_info(self, player_name, player_info):
        self.player_name = player_name
        self.player_info = player_info
        
        # set info for record owner
        for player in player_info:
            if self.player_name == player['playerName']:
                self.chips = player['chips']
                self.folded = player['folded']
                self.allin = player['allIn']
                self.cards = player['cards']
                self.card1 = Card(self.cards[0])
                self.card2 = Card(self.cards[1])
                self.is_survive = player['isSurvive']
                self.reload_count = player['reloadCount']
                self.round_bet = player['roundBet']
                self.bet = player['bet']
                self.isOnline = player['isOnline']
                self.isHuman = player['isHuman']

    def set_action_info(self, action_info):
        self.action_info = action_info
    
    def get_action_info(self):
        return self.action_info
        
    def get_table_id(self):
        return self.table_id
    
    def get_player_info(self):
        return self.player_info
    
    def get_player_name(self):
        return self.player_name
    
    def get_round_bet(self):
        return self.round_bet
    
    def get_bet(self):
        return self.bet
    
    def get_money_won(self):
        return self.money_won
    
    def set_money_won(self, money_won):
        self.money_won = money_won
        
    def set_action_history(self, action_history):
        self.action_history = action_history
        
    def to_feature_string(self):
        features = []
        
        ## record owner info
        features.append(self._get_chips_in_hand())
        features.append(self._get_total_round_bet())
        features.append(self._get_current_bet())
        features.append(self._get_chips_remain())
        features.extend(self._get_action_columns())
        features.append(self._is_small_blind())
        features.append(self._is_big_blind())
        features.append(self._get_hand_score())
        features.extend(self._get_set_possibility_and_win_possibility_columns())
        
        ## table info
        features.extend(self._get_round_stage_columns())
        features.append(self._get_bet_on_table())
        features.append(self._get_num_of_raises())
        features.append(self._get_num_of_bets())
        features.append(self._get_small_blind())
        features.append(self._get_big_blind())
                        
        ## opponent info 
        features.append(self._get_most_raise_count_from_one_opponent())
        features.append(self._get_most_amount_raised_from_opponent())
        features.append(self._get_most_portion_raised_from_opponent())
        features.append(self._get_most_amount_bet_from_opponent())
        features.append(self._get_most_portion_bet_from_opponent())
        features.extend(self._get_unfolded_opponent_raise_count_histogram_column())
        features.extend(self._get_unfolded_opponent_call_count_histogram_column())
        features.append(self._get_num_of_unfolded_opponent())
        features.append(self._get_num_of_allin_opponent())
        features.append(self._get_num_of_survive_opponent())
        features.append(self._get_num_of_online_opponent())
        
        ## game info
        features.extend(self._get_game_stage_column())

        ## reward
        features.append(self._get_reward())
        
        return ', '.join(str(e) for e in features)
    
    ## record owner info
    def _get_chips_in_hand(self):
        return self._normalize(self.chips)
        
    def _get_total_round_bet(self):
        return self._normalize(self.round_bet)
        
    def _get_current_bet(self):
        return self._normalize(self.bet)
        
    def _get_chips_remain(self):
        chips_in_hand = self.chips
        chips_can_reload = (self.max_reload_count - self.reload_count) * self.init_chips
        return self._normalize(chips_in_hand + chips_can_reload)
    
    def _get_action_columns(self):
        action_columns = [0, 0, 0, 0, 0, 0]
        
        #call, bet, raise, allin, fold
        action = self.action_info['action']
        if action == 'call':
            action_columns[0] = 1 
        elif action == 'bet':
            action_columns[1] = 1
        elif action == 'raise':
            action_columns[2] = 1
        elif action == 'allin':
            action_columns[3] = 1
        elif action == 'fold':
            action_columns[4] = 1
        elif action == 'check':
            action_columns[5] = 1            
        else:
            raise Exception('unrecognized action: [{}]'.format(action))
        
        return action_columns
    
    def _is_small_blind(self):
        return 1 if self.player_name == self.small_blind['playerName'] else 0
    
    def _is_big_blind(self):
        return 1 if self.player_name == self.big_blind['playerName'] else 0
    
    def _get_hand_score(self):
        return Score.get_chen_formula_score(self.card1, self.card2)
    
    def _get_set_possibility_and_win_possibility_columns(self):
        # holdem_functions.hand_rankings
        set_possibility_column = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        win_possibility_column = [0]
        
        if self.stage == 'Deal':
            pass
        elif self.stage == 'Turn' or self.stage == 'River' or self.stage == 'Flop':
            player_cards = []
            card1 = '{}{}'.format(self.card1.get_value(), self.card1.get_suit().lower())
            card2 = '{}{}'.format(self.card2.get_value(), self.card2.get_suit().lower())
            player_cards.append(card1)
            player_cards.append(card2)
            
            if self.stage != 'Flop':
                player_cards.append('?')
                player_cards.append('?')
            
            community_cards = []
            board_cards = self.board_card
            for card in board_cards:
                temp = ""
                temp += card[0]
                temp += card[1].lower()
                community_cards.append(temp)
            
            hole_cards, board = holdem_argparser.parse_cards(player_cards, community_cards)
            rounds = Config.get_num_of_monte_carlo_rounds()
            exact = Config.get_exact_holdem_calculation()
            verbose = Config.get_verbose_holdem_lib()
            
            #print 'hole_card=[{}], board=[{}], rounds=[{}], exact=[{}], verbose=[{}],'.format(hole_cards, board, rounds, exact, verbose)
            win_possibility, set_histogram, winner_list = holdem_calc.run(hole_cards, rounds, exact, board, None, verbose)
            
            if self.stage != 'Flop':
                win_possibility_column[0] = win_possibility[1]

            float_iterations = float(sum(winner_list))
            # only care about record owner's set histogram
            for index, occurrence in enumerate(set_histogram[0]):
                set_possibility_column[index] = occurrence / float_iterations
            
        else:
            raise Exception('unrecognized stage: [{}]'.format(self.stage))  
        
        #print "stage={} hand={} board={} win_pos={} set_pos={}".format(self.stage, self.cards, self. board_card, win_possibility_column, set_possibility_column)

        set_possibility_column.extend(win_possibility_column)
        return set_possibility_column
    
    ## table info
    def _get_round_stage_columns(self):
        round_stage_columns = [0, 0, 0, 0]
        
        #deal, flop, turn, river
        stage = self.stage
        if stage == 'Deal':
            round_stage_columns[0] = 1
        elif stage == 'Flop':
            round_stage_columns[1] = 1
        elif stage == 'Turn':
            round_stage_columns[2] = 1
        elif stage == 'River':
            round_stage_columns[3] = 1
        else:
            raise Exception('unrecognized stage: [{}]'.format(stage))
        
        return round_stage_columns
    
    def _get_bet_on_table(self):
        return self._normalize(self.total_bet)
    
    def _get_num_of_raises(self):
        return self.raise_count
    
    def _get_num_of_bets(self):
        return self.bet_count
    
    def _get_small_blind(self):
        return self._normalize(self.small_blind['amount'])
    
    def _get_big_blind(self):
        return self._normalize(self.big_blind['amount'])
    
    ## opponent info
    def _get_most_raise_count_from_one_opponent(self):
        opponent_raise_count = {}
        
        for action in self.action_history:
            if self.player_name == action['playerName']:
                continue
            
            if action['action'] != 'raise':
                continue
            
            if action['playerName'] not in opponent_raise_count:
                opponent_raise_count[action['playerName']] = 1
            else:
                opponent_raise_count[action['playerName']] += 1
        
        if len(opponent_raise_count) == 0:
            return 0
        
        return opponent_raise_count[max(opponent_raise_count, key=opponent_raise_count.get)]
        
    def _get_most_amount_raised_from_opponent(self):
        max_raised = 0
        
        for action in self.action_history:
            if self.player_name == action['playerName']:
                continue
            
            if action['action'] == 'raise' and action['amount'] > max_raised:
                max_raised = action['amount']
                
        return self._normalize(max_raised)
    
    def _get_most_portion_raised_from_opponent(self):
        max_raised = 0
        max_raised_player_chips_in_hand = 0
        
        for action in self.action_history:
            if self.player_name == action['playerName']:
                continue
            
            if action['action'] == 'raise' and action['amount'] > max_raised:
                max_raised = action['amount']
                max_raised_player_chips_in_hand = action['chips']
               
        
        if max_raised_player_chips_in_hand == 0:
            return 1
        
        return max_raised / (max_raised + max_raised_player_chips_in_hand)
        
    def _get_most_amount_bet_from_opponent(self):
        max_round_bet = 0
        
        for player in self.player_info:
            if self.player_name == player['playerName']:
                continue
            
            if player['roundBet'] > max_round_bet:
                max_round_bet = player['roundBet']
                
        return self._normalize(max_round_bet)
    
    def _get_most_portion_bet_from_opponent(self):
        max_round_bet = 0
        max_round_bet_player_chips_in_hand = 0
        
        for player in self.player_info:
            if self.player_name == player['playerName']:
                continue
            
            if player['roundBet'] > max_round_bet:
                max_round_bet = player['roundBet']
                max_round_bet_player_chips_in_hand = player['chips']
                
        if max_round_bet_player_chips_in_hand == 0:
            return 1
        
        return max_round_bet / (max_round_bet + max_round_bet_player_chips_in_hand)
    
    def _get_unfolded_opponent_raise_count_histogram_column(self):
        opponent_raise_count_histogram = [0, 0, 0, 0, 0]
        opponent_raise_count = {}
        
        # fill dictionary with opponent name and raise count
        for action in self.action_history:
            if self.player_name == action['playerName']:
                continue
            
            if action['action'] != 'raise':
                continue
            
            if action['playerName'] not in opponent_raise_count:
                opponent_raise_count[action['playerName']] = 1
            else:
                opponent_raise_count[action['playerName']] += 1
        
        # increment histogram with raise counts
        for value in opponent_raise_count.itervalues():
            if value == 1:
                opponent_raise_count_histogram[0] += 1
            elif value == 2:
                opponent_raise_count_histogram[1] += 1
            elif value == 3:
                opponent_raise_count_histogram[2] += 1
            elif value == 4:
                opponent_raise_count_histogram[3] += 1
            else:
                opponent_raise_count_histogram[4] += 1
                
        return opponent_raise_count_histogram
    
    def _get_unfolded_opponent_call_count_histogram_column(self):
        opponent_call_count_histogram = [0, 0, 0, 0]
        opponent_call_count = {}
        
        # fill dictionary with opponent name and call count
        for action in self.action_history:
            if self.player_name == action['playerName']:
                continue
            
            if action['action'] != 'call':
                continue
            
            if action['playerName'] not in opponent_call_count:
                opponent_call_count[action['playerName']] = 1
            else:
                opponent_call_count[action['playerName']] += 1
        
        # increment histogram with call counts
        for value in opponent_call_count.itervalues():
            if value == 1:
                opponent_call_count_histogram[0] += 1
            elif value == 2:
                opponent_call_count_histogram[1] += 1
            elif value == 3:
                opponent_call_count_histogram[2] += 1
            else:
                opponent_call_count_histogram[3] += 1
                
        return opponent_call_count_histogram
    
    def _get_num_of_unfolded_opponent(self):
        folded_count = 0
        
        for player in self.player_info:
            if self.player_name == player['playerName']:
                continue
            
            if player['folded']:
                folded_count +=1
                
        return self._get_num_of_survive_opponent() - folded_count
    
    def _get_num_of_allin_opponent(self):
        count = 0
        
        for player in self.player_info:
            if self.player_name == player['playerName']:
                continue
            
            if player['allIn']:
                count +=1
                
        return count
    
    def _get_num_of_survive_opponent(self):
        count = 0
        
        for player in self.player_info:
            if self.player_name == player['playerName']:
                continue
            
            if player['isSurvive']:
                count +=1
                
        return count
    
    def _get_num_of_online_opponent(self):
        count = 0
        
        for player in self.player_info:
            if self.player_name == player['playerName']:
                continue
            
            if player['isOnline']:
                count +=1
                
        return count
    
    ## game info
    def _get_game_stage_column(self):
        game_stage_columns = [0, 0, 0]
        
        # num of rounds / # of initial players (early if < 1, mid if < 2, late if else)
        ratio = self.round_count / len(self.player_info)
        if ratio <= 1:
            game_stage_columns[0] = 1
        elif ratio <= 2:
            game_stage_columns[1] = 1
        else:
            game_stage_columns[2] = 1
            
        return game_stage_columns
    
    ## reward    
    def _get_reward(self):
        if self.folded == 'true':
            return 0
        
        reward = self.money_won - self.round_bet - self.bet
        return self._normalize(reward)
        
    def _normalize(self, amount):
        return amount / (self.init_chips * self.reload_count * len(self.player_info))