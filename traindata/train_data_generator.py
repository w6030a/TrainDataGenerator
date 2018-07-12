#coding=utf-8

import sys
import json
from log_processor.log_processor_factory import LogProcessorFactory
from util.io_util import IOUtil
from util.config import Config

def main(argv):
    print 'argv = {}'.format(argv[1:])
    
    #TODO: arg 1 for input
    #TODO: arg 2 for output
    Config().set_output_path(u"")
    
    #process_log('C:\Users\pc\Desktop\pokerLog\common.log.game1_event.log')
    process_log(r'C:\Users\peter_chen\Documents\PokerGameLog\output\battle_20180313_event.log')
    
    
def process_log(file_path):
    lines = IOUtil.read_file_line_by_line(file_path)
        
    for line in lines:
        line = line[line.index('{'):]
        json_obj = json.loads(line)
            
        log_processor = LogProcessorFactory.get_processor(json_obj)
        log_processor.process()

if __name__ == "__main__":
    main(sys.argv)