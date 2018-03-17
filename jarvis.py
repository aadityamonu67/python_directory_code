import os
import random
import time

for i in range(1,4):

            a = random.choice(("hi","hey","sup"))
            print(a)
            os.system("say '"+a+"'")
            resp1 = input("")

            if resp1 not in ("hi","hey","sup"):
                GE = random.choice("ok what would you like to do","k whats up what are you going to do","now what","ok fine","what are you gonna do sir")
                print(GE)
                os.system("say '"+GE+"'")
                break                                       

while 1:

            lis = ("jokes","emails","note")
            resp2 = input("")
            esa = ""

            for word in lis:
                        if word in resp2:
                            esa == word

                            if esa == "email":
                                e = random.choice((""))
                                print(e)
                                os.system("say '"+e+"'")
                                break
            
            
