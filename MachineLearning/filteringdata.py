#
#  FILTERINGDATA.py
#
#  Code file for the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#
#  JCK: I implemented the Euclidean and CompareDistances functions
#  and replaced users with decks
#  data obtained from http://yugioh.tcgplayer.com/db/deck_search_result.asp

from math import sqrt

decks = {"MonarchA": {"Mobius": 3, "Thestalos": 3, "Zaborg": 2, "Jinzo": 0, "GravekeepersSpy": 2, "Merchant": 0, "Dekoichi": 3, "DDAssailant": 1, "Cyber Dragon": 3, "ApprenticeOldMan": 0, "Tomato":0, "Exiled": 1, "Asura": 0},
         "MonarchB": {"Mobius": 0, "Thestalos": 3, "Zaborg": 3, "Jinzo": 1, "GravekeepersSpy": 2, "Merchant": 1, "Dekoichi": 2, "DDAssailant": 0, "Cyber Dragon": 2, "ApprenticeOldMan": 0, "Tomato":0, "Exiled": 0, "Asura": 1},
         "MonarchC": {"Mobius": 0, "Thestalos": 1, "Zaborg": 2, "Jinzo":0, "GravekeepersSpy": 2, "Merchant": 1, "Dekoichi": 3, "DDAssailant": 0, "Cyber Dragon":3, "ApprenticeOldMan":0, "Tomato":0, "Exiled":1,"Asura":0},
         "MonarchD": {"Mobius": 1, "Thestalos": 3, "Zaborg": 2, "Jinzo":0, "GravekeepersSpy": 0, "Merchant": 0, "Dekoichi": 3, "DDAssailant": 0, "Cyber Dragon":3, "ApprenticeOldMan":4, "Tomato":2, "Exiled":0,"Asura":0},
         "MonarchE": {"Mobius": 0, "Thestalos": 3, "Zaborg": 3, "Jinzo":0, "GravekeepersSpy": 0, "Merchant": 0, "Dekoichi": 3, "DDAssailant": 0, "Cyber Dragon":3, "ApprenticeOldMan":4, "Tomato":0, "Exiled":0,"Asura":0},
         "MonarchF": {"Mobius": 0, "Thestalos": 0, "Zaborg": 2, "Jinzo":0, "GravekeepersSpy": 0, "Merchant": 0, "Dekoichi": 0, "DDAssailant": 1, "Cyber Dragon":3, "ApprenticeOldMan":0, "Tomato":3, "Exiled":2,"Asura":2},
         "MonarchG": {"Mobius": 1, "Thestalos": 0, "Zaborg": 2, "Jinzo":0, "GravekeepersSpy": 0, "Merchant": 0, "Dekoichi": 2, "DDAssailant": 0, "Cyber Dragon":3, "ApprenticeOldMan":0, "Tomato":2, "Exiled":2,"Asura":1},
         "MonarchH": {"Mobius": 0, "Thestalos": 1, "Zaborg": 3, "Jinzo":0, "GravekeepersSpy": 0, "Merchant": 0, "Dekoichi": 2, "DDAssailant": 0, "Cyber Dragon":3, "ApprenticeOldMan":4, "Tomato":2, "Exiled":0,"Asura":0},
         "MobiusA": {"Mobius": 2, "Thestalos": 0, "Zaborg": 0, "Jinzo":0, "GravekeepersSpy": 2, "Merchant": 0, "Dekoichi": 0, "DDAssailant": 2, "Cyber Dragon":0, "ApprenticeOldMan":0, "Tomato":0, "Exiled":1,"Asura":0},
         "MobiusB": {"Mobius": 2, "Thestalos": 2, "Zaborg": 0, "Jinzo":0, "GravekeepersSpy": 0, "Merchant": 0, "Dekoichi": 0, "DDAssailant": 3, "Cyber Dragon":1, "ApprenticeOldMan":0, "Tomato":1, "Exiled":0,"Asura":0},
         "MobiusC": {"Mobius": 2, "Thestalos": 0, "Zaborg": 0, "Jinzo":0, "GravekeepersSpy": 2, "Merchant": 0, "Dekoichi": 0, "DDAssailant": 1, "Cyber Dragon":1, "ApprenticeOldMan":0, "Tomato":1, "Exiled":1,"Asura":0},
         "MobiusD": {"Mobius": 2, "Thestalos": 0, "Zaborg": 0, "Jinzo":0, "GravekeepersSpy": 2, "Merchant": 0, "Dekoichi": 2, "DDAssailant": 2, "Cyber Dragon":2, "ApprenticeOldMan":0, "Tomato":0, "Exiled":0,"Asura":0},
         "Test": {"Mobius": 2, "Dekoichi":2, "DDAssailant":1, "ApprenticeOldMan":4}

        }

def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1 #Indicates no ratings in common

def Euclidean(rating1, rating2):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += pow((rating1[key] - rating2[key]),2)
            commonRatings = True
    if commonRatings:
        return pow(distance, 1/2)
    else:
        return -1 #Indicates no ratings in common

def CompareDistances(rating1, rating2):
    distance = 0
    commonRatings = False
    EuclidDist = Euclidean(rating1, rating2)
    ManhattanDist = manhattan(rating1, rating2)
    print "Euclid: ", EuclidDist, " Manhattan: ",ManhattanDist

def computeNearestNeighbor(deckname, decks):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for deck in decks:
        if deck != deckname:
            distance = manhattan(decks[deck], decks[deckname])
            distances.append((distance, deck))
    # sort based on distance -- closest first
    distances.sort()
    return distances

def recommend(deckname, decks):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(deckname, decks)[0][1]

    recommendations = []
    # now find bands nearestneighbor rated that user didn't
    neighborRatings = decks[nearest]
    deckRatings = decks[deckname]
    for artist in neighborRatings:
        if not artist in deckRatings:
            recommendations.append((artist, neighborRatings[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# examples - uncomment to run
print "Manhattan between A and B", manhattan(decks['MonarchA'], decks['MonarchB'])

print "Recommended for Test",  recommend('Test', decks)
#from the values in users, it is recommended to use
#'Thestalos: 3, Cyber Dragon 3, Tomato 2, Zaborg 2, Asura 0, Jinzo 0, GravekeepersSpy 0, Exiled 0

print "Dist between ", 'MobiusA', "vs ",'MobiusC',"is "
CompareDistances(decks['MobiusA'], decks['MobiusC'])