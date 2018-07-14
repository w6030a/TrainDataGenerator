#coding=utf-8

import sys
from os import walk
import json
from log_processor.log_processor_factory import LogProcessorFactory
from util.io_util import IOUtil
from util.config import Config
import time

def main(argv):
    print 'argv = {}'.format(argv[1:])
    start = time.time()
    
    Config().set_input_path(argv[0])
    Config().set_output_path(argv[1])
    
    files = []
    for (dirpath, dirnames, filenames) in walk(Config.get_input_path()):
        print '[{}] [{}] [{}]'.format(dirpath, dirnames, filenames)
        for filename in filenames:
            files.append('{}\{}'.format(dirpath, filename))

    for f in files:
        print 'Processing file: {}'.format(f)
        process_log(f)
    
    print "\nTime elapsed(seconds): ", time.time() - start
    
def process_log(file_path):
    lines = IOUtil.read_file_line_by_line(file_path)
        
    for line in lines:
        try:
            line = line[line.index('{'):]
            json_obj = json.loads(line)
            
            log_processor = LogProcessorFactory.get_processor(json_obj)
            log_processor.process()
        except ValueError:
            #print 'ValueError Exception occur in line: [{}]'.format(line)
            pass
        
            
if __name__ == "__main__":
    main(sys.argv)