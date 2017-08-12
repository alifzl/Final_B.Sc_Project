"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

"""

idA = 0

# All Agents ever created, one consecutive list
agentsOverGenerations = []

# same as above just as a dictionary
# {int_index : [Agent List for the Generation specified by int_index]}
agentsOverAllDict = {}

# a dictionary holding all the recipes for each Generation in an array
# RecListOverGenerations{"int_Index : Recipe"}
RecListOverGenerations = {}

# all the winning recipes in a dictionary
WinningArrsOverGenerations = {}

# The name says it all, Dictionary holding the social groups for each Generation
SocialGroups = {}


def config_reset():
    global SocialGroups
    SocialGroups = {}
    global WinningArrsOverGenerations
    WinningArrsOverGenerations = {}
    global RecListOverGenerations
    RecListOverGenerations = {}
    global agentsOverAllDict
    agentsOverAllDict = {}
    global agentsOverGenerations
    agentsOverGenerations = []
    global idA
    idA = 0
