"""
Aurelio Amparo
2021-03-15
program: chatlog parsing
"""
import re
def Main():
    logDic = {}
    
    actions = {"+":"login", "-":"logout"}
    users = {}
    with open('Chatlog\chatlog.txt',"r") as file:
        data = file.read()
    data = data.split("\n")
    for row in data:
        # our regex patterns we are looking for
        matches = re.match('(\d{2}:\d{2}:\d{2})([+,-]).*?(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', row, re.I)
        row = row.split(" ")
        if matches:
            userName = row[1]
            action = matches.group(2)
            ipAddress = matches.group(3)
            users[userName]= ipAddress
            #if userName key doesnt exist, add new key
            if((userName in logDic) == False):
                logDic[userName] = {"login":0, "logout":0}
                #to keep track of our login and logout
                logDic[userName][actions[action]] += 1
            else:
                logDic[userName][actions[action]] += 1     
            
    for i in users:
        print("User: " + i + "\n"+"IP Address: " +users[i])
        print("Login: " + str(logDic[i]["login"]))
        print("Logout: " + str(logDic[i]["logout"])+ "\n")

Main()