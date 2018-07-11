from abstract_log_processor import AbstractLogProssor
from record.record import Record
from record.record_warehouse import RecordWarehouse

class RoundEndLogProcessor(AbstractLogProssor):

    def __init__(self, log):
        self.log = log
        
    def process(self):
        ## prepare data for record obj
        data = self.log['data']
        table_info = data['table']
        player_info = data['players']
        
        record = Record()
        record.set_table_info(table_info)
        record.set_player_info(player_info)
        
        ## push record to record_warehouse
        RecordWarehouse.round_clear(record)
        
        ## calculate reward
        
        ## clean old records for table_id in record_warehouse