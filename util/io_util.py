#coding=utf-8

class IOUtil(object):

    @staticmethod
    def write_file(path, content):
        pass
    
    @staticmethod
    def write_file_line_by_line(path, content):
        for line in content:
            print line
        #TODO: content is a list
        pass
    
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
        