import threading
import os

def dll_mon():
    os.system('python DLL.py')
        

def anti_check():
    os.system('python anti.py')

        

def exten_check():
    os.system('python exten.py')

if __name__ == "__main__":
    t1 = threading.Thread(target=dll_mon)
    t2 = threading.Thread(target=anti_check)
    t3 = threading.Thread(target=exten_check)
    t1.start()
    t2.start()
    t3.start()
