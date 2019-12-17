import collections,time
from datetime import date

def checkYear(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False
    
def round_robin1(teams, rounds,d,m,y):
    dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    dic1 = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if len(teams) % 2:
        teams.append(None)

    schedule = []
    for turn in range(rounds):
        pairings = []
        for i in range(len(teams) // 2):
            if teams[i] == None or teams[len(teams) - i - 1] == None:
                continue
            else:
                pairings.append(('Team '+str(teams[i]),'Team '+ str(teams[len(teams) - i - 1])))
                pairings.append( str(d)+'/'+str(m)+'/'+str(y) )
                if checkYear(y) == False:
                    if d+1 <= dic[m]:
                        d+=1
                    else:
                        m = m + 1
                        if m == 13:
                            m = 1
                            y+=1
                        d=1
                else:
                    if d+1 <= dic1[m]:
                        d+=1
                    else:
                        m = m + 1
                        if m == 13:
                            m = 1
                            y+=1
                        d=1
        teams.insert(1, teams.pop())
        schedule.append(pairings)

    return schedule

l = [1,2,3,4]
k = len(l)-1
if k%2 == 0:
    k+=1
    
today = date.today()
d1 = today.strftime("%d/%m/%Y")
d = int(today.strftime("%d"))
m = int(today.strftime("%m"))
y = int(today.strftime("%Y"))
#print(d1)
#print(d2,d1)
#print(type(y))
print(round_robin1(l,k,d,m,y))
