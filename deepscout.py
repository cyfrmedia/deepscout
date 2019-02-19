import tbapy
import csv
tba = tbapy.TBA('5dZk9TNOXQwwP01zeMbhWWpe2Nq5KwGNnBWcxN4zlpVDt3ESE6VdnSOYYG0LchNm')

#set up variables for data storage
cadateams = [100, 1056, 1072, 1323, 1458, 1678, 199, 2085, 2141, 2204, 2367, 2551, 2839, 3013, 3189, 3250, 3257, 3482, 3598, 3615, 3669, 3859, 3880, 4135, 4643, 4698, 4904, 5250, 5274, 5419, 5430, 5458, 5480, 5496, 5507, 5871, 5875, 5940, 6174, 6238, 6305, 6358, 6474, 6612, 6619, 6644, 6657, 6662, 6883, 6918, 6926, 6981, 701, 7137, 7229, 7529, 7663, 7802, 7870, 973]
cafrteams = [1072,1280,1323,1351,1388,1422,1662,1671,1678,1967,2085,2135,2489,2813,2854,3189,3257,3303,3495,3669,3970,4135,4698,5026,5102,5104,5134,5274,5458,5461,5728,5817,5852,6241,6305,6506,6657,6711,6804,6884,6926,6981,701,7057,7229,751,7524,7589,766,7663]
bothcomps = []
allteams = []
attending = {

}
att_sans_cada = {

}
att_sans_cafr = {

}
att_sans_both = {

}


i = 0
#add davis teams to list of all teams
while i < len(cadateams):
    current_team = cadateams[i]
    allteams.append(current_team)
    i += 1

i = 0
#add fresno teams to list of all teams, removing those already on list from davis
while i < len(cafrteams):
    current_team = cafrteams[i]
    if current_team in allteams
        bothcomps.append(current_team)
    if current_team not in allteams
        allteams.append(current_team)
    i += 1

i = 0
print(allteams)
while i < len(allteams):
    current_team = allteams[i]
    #fill out attendance dictionaries
    attending[current_team] = tba.team_events(current_team, 2019, keys=True)
    #print(current_team, end = " ")
    #print(tba.team_events(current_team, 2019, keys=True))
    i += 1

#print("Enter the team you'd like to search: ")
#result = attending.get(input())
#print(result)
print(attending)

for x, y in attending.items():
    if '2019cafr' in attending.get(x):
        attending.get(x).remove('2019cafr')
    if '2019cada' in attending.get(x):
        attending.get(x).remove('2019cada')
    if len(attending.get(x)) != 0:
        evlist = attending.get(x)
        print(tba.event(evlist[1], simple=True))
        print(x, y)


#Calling methods on your TBA client will be slower than using variables already loaded, because each call makes a request to TBA's web API (specifically https://thebluealliance.org/api/v3/<some URL>). In places where you call the same method with the same arguments twice, like lines 29 and 30 or 46 and 52, storing tba.team_events(current_team, 2019, keys=True) in a variable and then using it from there should make the script significantly faster.

#tba.event(attending.get(current_team), simple=True)
