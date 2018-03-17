import urllib2
import random
import time
c = random.randint(0,9)
i=1
while(i!=0):
    req = urllib2.Request('http://www.techno.somee.com/Default2.aspx?ab='+str(c))
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
    time.sleep(1000)
    print "sleeping"

