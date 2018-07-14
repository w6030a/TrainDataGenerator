#coding=utf-8

class IOUtil(object):

    @staticmethod
    def write_file(path, content):
        pass
    
    @staticmethod
    def write_file_line_by_line(path, content):
        f = open(path, 'a')
        for line in content:
            line += "\n"
            f.write(line)  # python will convert \n to os.linesep
        f.close() 
    
    @staticmethod
    def read_file(path):
        f = open(path, 'r') 
        data =  f.read()
        f.close()
        
        return data
        
    @staticmethod
    def read_file_line_by_line(path):
        with open(path) as f:
            lines = f.readlines()
            
        return lines
        