class Config(object):

    input_path = ""
    output_path = ""
    
    @staticmethod
    def get_input_path():
        return Config.input_path
    
    @staticmethod
    def set_input_path(input_path):
        Config.input_path = input_path
    
    @staticmethod
    def get_output_path():
        return Config.output_path
    
    @staticmethod
    def set_output_path(output_path):
        Config.output_path = output_path