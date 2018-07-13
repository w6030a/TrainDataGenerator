class RecordWarehouse:
    record_bucket = {}
    
    @staticmethod
    def append(key, record):
        if key not in RecordWarehouse.record_bucket:
            record_list = []
            RecordWarehouse.record_bucket[key] = record_list
        
        RecordWarehouse.record_bucket[key].append(record)
        
        #print 'record appended for table {}'.format(key)
        #print 'keys in bucket {}'.format(RecordWarehouse.record_bucket.keys())
    
    @staticmethod
    def pop_records(key):
        temp = RecordWarehouse.record_bucket[key];
        del RecordWarehouse.record_bucket[key]
        #print 'keys in bucket {}\n'.format(RecordWarehouse.record_bucket.keys())
        return temp