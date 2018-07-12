

class IOUtil(object):

    @staticmethod
    def write_file(path, content):
        #TODO
        pass
    
    @staticmethod
    def read_file(path):
        f = open(path, 'r') 
        data =  f.read()
        f.close()
        return data
        