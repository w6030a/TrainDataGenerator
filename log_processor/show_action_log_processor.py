from abstract_log_processor import AbstractLogProssor
from record.record import Record
from record.record_warehouse import RecordWarehouse

class ShowActionLogProcessor(AbstractLogProssor):

    def __init__(self, log):
        self.log = log
        
    def process(self):
        ## prepare data for record obj
        data = self.log['data']
        table_info = data['table']
        player_info = data['players']
        action_info = data['action']
        
        record = Record()
        record.set_table_info(table_info)
        record.set_player_info(player_info)
        record.set_action_info(action_info)
        
        ## push record to record_warehouse
        RecordWarehouse.append(record)
