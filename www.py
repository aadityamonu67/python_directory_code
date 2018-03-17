import requests
import time

ipaddr= ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
i=0;
while i<=len(ipaddr):
    try:
        link='https://'+ipaddr[i]+'/events'
        r = requests.get(link,timeout=0.50)
        print "working ip"
    except:
        print "deleting ip"+link
        i=i+1
    
