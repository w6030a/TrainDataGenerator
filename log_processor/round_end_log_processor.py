from abstract_log_processor import AbstractLogProssor
from record.record import Record
from record.record_warehouse import RecordWarehouse
from util.io_util import IOUtil
from util.config import Config

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
        
        record_history = RecordWarehouse.pop_records(round_end_record.get_table_id())
        self._assign_money_won(player_info, record_history)
        self._assign_action_history(record_history)
        
        ## write log from record
        log = []
        for record in record_history:
            log.append(record.to_feature_string())
        
        IOUtil.write_file_line_by_line(Config.get_output_path(), log)
        
    def _get_money_won(self, player_info):
        money_won = {}
        for player in player_info:
            player_name = player['playerName']
            winMoney = player['winMoney']
            money_won[player_name] = winMoney
            
        return money_won
    
    def _assign_money_won(self, player_info, record_history):
        money_won = self._get_money_won(player_info);
        for record in record_history:
            player_name = record.get_player_name()
            record.set_money_won(money_won[player_name])
            
    def _assign_action_history(self, record_history):
        action_history = []
        for record in record_history:
            action_history.append(record.get_action_info())
            record.set_action_history(action_history)
        