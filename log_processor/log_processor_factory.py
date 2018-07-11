from round_end_log_processor import RoundEndLogProcessor
from show_action_log_processor import ShowActionLogProcessor
from game_over_log_processor import GameOverLogProcessor

class LogProcessorFactory:

    @staticmethod
    def get_processor(log):
        
        if 'eventName' not in log:
            raise Exception('Not an event log')
        
        event_name = log['eventName']
        
        if event_name == '__show_action':
            return ShowActionLogProcessor(log)
        elif event_name == '__round_end':
            return RoundEndLogProcessor(log)
        elif event_name == '__game_over':
            return GameOverLogProcessor(log)
        else:
            raise Exception('unrecognized event: [{}]'.format(log))                 
