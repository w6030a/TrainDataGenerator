class RecordWarehouse:
#TODO: dictionary of list for records
    record_bucket = {}
    
    @staticmethod
    def append(record):
        RecordWarehouse.record_bucket[record.get_table_id()] = record
        print 'record appended for table {}'.format(record.get_table_id())
        print 'keys in bucket {}'.format(RecordWarehouse.record_bucket.keys())
    
    @staticmethod
    def round_clear(record):
        print 'record end event for table {}'.format(record.get_table_id())
        #TODO: do calculation
        #TODO: write log
        del RecordWarehouse.record_bucket[record.get_table_id()]
        print 'keys in bucket {}\n'.format(RecordWarehouse.record_bucket.keys())