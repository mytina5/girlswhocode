import json
#create an empty dictionary




#ceate a list of survey questions
survey = ["What's your name?",
            "How many pets do you own?",
            "What's your favorite color?",
            "What month were you born in?",
            "Do you prefer vanilla or chocolate icecream?"]

#create a list of related keys
key = ["name", "pets", "color", "month", "icecream"]

allUsers = []
done = "no"

#loop through youe list of survey questions and take user input for responses
while done == "no":
    users = {}
    i = 0
    total = 0
    vanillac = 0
    chocolatec = 0
    for questions in survey:
        answers = input(survey[i] + ": ")
        users[key[i]] = answers
        i += 1 #thats what increases index
    allUsers.append(users)
    for v in allUsers:
        total +=1
        vr = v["icecream"]
        if vr == "vanilla":
            vanillac +=1
        if vr == "chocolate":
            chocolatec +=1
    if vanillac > chocolatec:
        print(str(vanillac) + " out of " + str(total) + " prefer vanilla ice cream ")
    elif chocolatec > vanillac:
        print(str(chocolatec) + " out of " + str(total) + " prefer chocolate ice cream ")
    else:
        print("An equal amount of people like chocolate and vanilla icecream.")
    done = input("Are you finished collecting information? (yes or no): ")






#print (allUsers)

#import json
#from survey import*

#dictionaryToJson = json.dumps(allUsers)
#print(dictionaryToJson)
print(allUsers)
with open('survey.json') as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
allUsers.extend(olddata)
f.close()

f = open("survey.json", "w")
json.dump( allUsers ,f)
f.close()
