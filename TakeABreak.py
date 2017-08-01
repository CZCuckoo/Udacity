import webbrowser
import time

takebreak = 1

print("This program started on "+time.ctime())




while takebreak <= 3:
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    print('This is break number')
    print(takebreak)
    takebreak = takebreak + 1



