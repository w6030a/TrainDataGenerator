import sys
import json
from log_processor.log_processor_factory import LogProcessorFactory

def main(argv):
    print 'argv = {}'.format(sys.argv[1:])
    process_log('C:\Users\peter_chen\Documents\PokerGameLog\output\common.log.game1_event.log')
    
def read_file(file_path):
    f = open(file_path, 'r') 
    data =  f.read()
    f.close()
    return data

def process_log(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        
        for line in lines:
            line = line[line.index('{'):]
            json_obj = json.loads(line)
            
            log_processor = LogProcessorFactory.get_processor(json_obj)
            log_processor.process()

if __name__ == "__main__":
    main(sys.argv)