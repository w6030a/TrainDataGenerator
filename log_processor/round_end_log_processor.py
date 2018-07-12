from abstract_log_processor import AbstractLogProssor
from record.record import Record
from record.record_warehouse import RecordWarehouse

class RoundEndLogProcessor(AbstractLogProssor):

    def __init__(self, log):
        self.log = log
        
    def process(self):
        ## prepare data for round_end_record obj
        data = self.log['data']
        table_info = data['table']
        player_info = data['players']
        
        round_end_record = Record()
        round_end_record.set_table_info(table_info)
        
        ## calculate reward
        rewards = self._get_rewards(player_info);
        
        ## append reward to records
        record_list = RecordWarehouse.pop_records(round_end_record.get_table_id())
        for record in record_list:
            player_name = record.get_player_name()
            record.set_reward(rewards[player_name])
            
        ## write log
        
    def _get_rewards(self, player_info):
        rewards = {}
        
        for player in player_info:
            player_name = player['playerName']
            reward = player['winMoney']
            rewards[player_name] = reward
            
        return rewards
        