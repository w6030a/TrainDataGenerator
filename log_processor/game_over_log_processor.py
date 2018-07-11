from abstract_log_processor import AbstractLogProssor

class GameOverLogProcessor(AbstractLogProssor):

    def __init__(self, log):
        self.log = log
        
    def process(self):
        print '__game_over event'
        #TODO
        pass