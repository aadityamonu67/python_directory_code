import webbrowser
import time
import os

print '\t\t\t ######################################'
print '\t\t\t ##                                  ##'
print '\t\t\t ##   Author : Sandeep Saini         ##'
print '\t\t\t ######################################'



url = input("Enter YouTube URL : ")
refresh = input("Enter refresh rate(seconds) : ")
brow = input("Enter your default browser : ")

def OpenUrl():
    print "Successfully Viwed. "
    os.system("TASKKILL /F /IM " + brow + ".exe")
    webbrowser.open(url)
    time.sleep(int(refresh))

for i in range(20) : # Edit 3 with your no. of viwes 
    OpenUrl()
    
        
        
