import sys

def main(argv):
    print  sys.argv[1:]
    
    
def readFile(file_path):
    f = open(file_path, 'r') 
    data =  f.read()
    f.close()
    return data
 
if __name__ == "__main__":
    main(sys.argv)