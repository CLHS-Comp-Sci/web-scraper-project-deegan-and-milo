import requests

header = {"X-TBA-Auth-Key": "atFZXBM2LybeAXKkxBelxjn8EgqwnYcFRmSLrVFCEblPpDmDGAZClEStErRMDjQk"}

# response = requests.get("https://www.google.com")


def getTopList(lst):
    return "Score: "+str(lst[0])+", Teams: "+lst[1][0][3:len(lst[1][0])]+", "+lst[1][1][3:len(lst[1][1])]+", "+lst[1][2][3:len(lst[1][2])]

def main():
    
    year = input("Enter a year number: ")
    
    team = input("Enter a team number: ")
    
    url = "https://www.thebluealliance.com/api/v3/team/frc"+team+"/matches/"+year+"/simple"
    
    response = requests.get(url=url,headers=header)

    res = response.json()
    # print(res)
    
    listOfMatches = []
    
    # print(len(res))
    # print(res[0]["alliances"])
    
    for i in range(len(res)):
        tempMatch = res[i]
        
        if(("frc"+team) in tempMatch["alliances"]["blue"]["team_keys"]):
            listOfMatches.append([tempMatch["alliances"]["blue"]["score"],tempMatch["alliances"]["blue"]["team_keys"]])
        else:
            listOfMatches.append([tempMatch["alliances"]["red"]["score"],tempMatch["alliances"]["red"]["team_keys"]])
    
    
    lengthOfTopLists = 10
    
    
    topFive = []
    bottomFive = []
    for i in range(lengthOfTopLists):
        topFive.append([0])
        bottomFive.append([1000])
    
    sum = 0
    
    for i in range(len(listOfMatches)):
        temp = listOfMatches[i]
        for k in range(len(topFive)):
            if(temp[0]>topFive[k][0]):
                topFive.insert(k,temp)
                topFive.pop()
                break
        for k in range(len(bottomFive)):
            if(temp[0]<bottomFive[k][0]):
                bottomFive.insert(k,temp)
                bottomFive.pop()
                break
        sum += temp[0]
    
    print()
    print("Top five: ")
    for i in range(len(topFive)):
        print(str(i+1)+". "+getTopList(topFive[i]))
    print()
    print("Bottom five: ")
    for i in range(len(topFive)):
        print(str(i+1)+". "+getTopList(bottomFive[i]))
    print()
    print("Average match score:")
    print(sum/len(listOfMatches))
    
    

    
    
main()