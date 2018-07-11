import sys
import json
from record import Record
from pprint import pprint

def main(argv):
    print 'argv = {}'.format(sys.argv[1:])
    processLog('C:\Users\pc\Desktop\pokerLog\common.log.game1_event.log')
    
def readFile(file_path):
    f = open(file_path, 'r') 
    data =  f.read()
    f.close()
    return data

def processLog(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        
        for line in lines:
            line = line[line.index('{'):]
            json_obj = json.loads(line)
            
            if 'eventName' not in json_obj:
                raise Exception('Not an event log')
            
            event_name = json_obj['eventName']
            
            if event_name == '__show_action':
                record = process_show_action_event(json_obj)
            elif event_name == '__round_end':
                record = process_round_end_event(json_obj)
            elif event_name == '__game_over':
                record = process_game_over_event(json_obj)
            else:
                print json_obj
                raise Exception('unrecognized event')
        
def process_show_action_event(json_obj):
    record = Record()

    data = json_obj['data']
    player_info = data['players']
    table_info = data['table']
    action_info = data['action']

    table_id = table_info['tableNumber']
    stage = table_info['roundName']
    total_bet = table_info['totalBet']
    init_chips = table_info['initChips']
    max_reload = table_info['max_reload']
    
    board_card = table_info['board']
    #pprint(board_card)

def process_round_end_event(json_obj):
    data = json_obj['data']
    player_info = data['players']
    table_info = data['table']
            
    board_card = table_info['board']
    #pprint(board_card)

def process_game_over_event(json_obj):
    print '__game_over event'

if __name__ == "__main__":
    main(sys.argv)