class Config(object):

    input_path = ""
    output_path = ""
    
    num_of_monte_carlo_rounds = 100000
    exact_holdem_calculation = False
    verbose_holdem_lib = False
    
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
        
    @staticmethod
    def get_num_of_monte_carlo_rounds():
        return Config.num_of_monte_carlo_rounds
        
    @staticmethod
    def set_num_of_monte_carlo_rounds(rounds):
        Config.num_of_monte_carlo_rounds = rounds
        
    @staticmethod
    def get_exact_holdem_calculation():
        return Config.exact_holdem_calculation
        
    @staticmethod
    def set_exact_holdem_calculation(exact):
        Config.exact_holdem_calculation = exact
        
    @staticmethod
    def get_verbose_holdem_lib():
        return Config.verbose_holdem_lib
        
    @staticmethod
    def set_verbose_holdem_lib(verbose):
        Config.verbose_holdem_lib = verbose