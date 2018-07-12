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
        
    def set_player_info(self, player_info):
        self.player_info = player_info
        
        # set info for record owner
        for player in player_info:
            if self.player_name == player['playerName']:
                self.chips = player['chips']
                self.folded = player['folded']
                self.allin = player['allIn']
                self.cards = player['cards']
                self.is_survive = player['isSurvive']
                self.reload_count = player['reloadCount']
                self.round_bet = player['roundBet']
                self.bet = player['bet']
                self.isOnline = player['isOnline']
                self.isHuman = player['isHuman']

    def set_action_info(self, action_info):
        self.action = action_info['action']
        self.player_name = action_info['playerName']
        self.chips = action_info['chips']
        
        if 'amount' not in action_info:
            self.amount = 0
        else:
            self.amount = action_info['amount']
        
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
        
    def to_feature_string(self):
        features = []
        
        ## record owner info
        features.append(self._get_chips_in_hand())
        features.append(self._get_total_round_bet())
        features.append(self._get_current_bet())
        features.append(self._get_chips_remain())
        features.append(self._get_action_columns())

        ## table info
        features.append(self._get_round_stage_columns())
        features.append(self._get_bet_on_table())
        features.append(self._get_num_of_raises())
        features.append(self._get_num_of_bets())
        features.append(self._get_small_blind())
        features.append(self._get_big_blind())
                        
        ## opponent info 
        features.append(self._get_num_of_unfolded_opponent())
        features.append(self._get_num_of_allin_opponent())
        features.append(self._get_num_of_survive_opponent())
        features.append(self._get_num_of_online_opponent())
        
        ## game info
        features.append(self._get_game_stage_column())

        ## reward
        features.append(self._get_reward())
        
        return features
    
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
        action = self.action
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
    
    ## table info
    def _get_round_stage_columns(self):
        round_stage_columns = [0, 0, 0, 0, 0]
        
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
        return self.total_bet
    
    def _get_num_of_raises(self):
        return self.raise_count
    
    def _get_num_of_bets(self):
        return self.bet_count
    
    def _get_small_blind(self):
        return self._normalize(self.small_blind['amount'])
    
    def _get_big_blind(self):
        return self._normalize(self.big_blind['amount'])
    
    ## opponent info
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
        return reward
        
    def _normalize(self, amount):
        return amount / self.init_chips