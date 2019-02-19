import tbapy
import csv
tba = tbapy.TBA('5dZk9TNOXQwwP01zeMbhWWpe2Nq5KwGNnBWcxN4zlpVDt3ESE6VdnSOYYG0LchNm')

#turn csv event team list into array
#cadateams = []
#with open("2019cada_teams.csv") as csvfile:
#    reader = csv.reader(csvfile)
#    for row in reader: # each row is a list
#        cadateams.append(row)

#increment through list
cadateams = [100, 1056, 1072, 1323, 1458, 1678, 199, 2085, 2141, 2204, 2367, 2551, 2839, 3013, 3189, 3250, 3257, 3482, 3598, 3615, 3669, 3859, 3880, 4135, 4643, 4698, 4904, 5250, 5274, 5419, 5430, 5458, 5480, 5496, 5507, 5871, 5875, 5940, 6174, 6238, 6305, 6358, 6474, 6612, 6619, 6644, 6657, 6662, 6883, 6918, 6926, 6981, 701, 7137, 7229, 7529, 7663, 7802, 7870, 973]
cafrteams = [1072,1280,1323,1351,1388,1422,1662,1671,1678,1967,2085,2135,2489,2813,2854,3189,3257,3303,3495,3669,3970,4135,4698,5026,5102,5104,5134,5274,5458,5461,5728,5817,5852,6241,6305,6506,6657,6711,6804,6884,6926,6981,701,7057,7229,751,7524,7589,766,7663]
i = 0
bothcomps = []
while i < len(cadateams):
    current_team = cadateams[i]
    if current_team in cafrteams:
            print("BOTH COMPS")
            bothcomps.append(current_team)
    print(current_team)
    print(tba.team_events(current_team, 2019, keys=True))
    i += 1
i = 0
while i < len(cafrteams):
    current_team = cafrteams[i]
    if current_team in cadateams:
            bothcomps.append(current_team)
    if current_team not in bothcomps:
            print(current_team)
            print(tba.team_events(current_team, 2019, keys=True))
    i += 1
