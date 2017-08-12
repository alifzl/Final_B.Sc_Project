"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  Collection of methods for quick testing purposes
"""


import Recipe as REx
import Config as cfg


def CntTest(agentArr):
    """
    Print the Agent ID, the Agents preference and the ingredient list for the
    Agents own recipe for all Agents of one specific Generation
    :param agentArr: List containing all Agents in a specific Generation
    :return: Printed out visual representation of the Agents in the Generation
    """
    mCnt = 0
    fCnt = 0
    vCnt = 0
    for x in agentArr:
        if x.getPref() == "meat":
            mCnt += 1
        elif x.getPref() == "fish":
            fCnt += 1
        else:
            vCnt += 1

        print str(x.getIDA())+ " " + x.getPref()
        RecTest(x)

    print
    print "mCnt: " + str(mCnt)
    print "fCnt: " + str(fCnt)
    print "vCnt: " + str(vCnt)

def RecTest(agent):
    """
    Print the ingredient list for the Agents own recipe
    :param agent: An Agents instance
    :return: Printed out visual representation of the ingredients in the Agents recipe
    """
    print agent.getRec().ingredients

def RetAllGenAgents(agentsArray):
    """
    Same as CntTest(agentArr) but being fed a list containing all Agents ever created
    up to the point of calling ( + Preference + Ingredients of Recipe )
    :param agentsArray: List of all Agents created up to the point of calling the method
    :return: Printed out visual representation of the Agents created so far
    """
    mCnt = 0
    fCnt = 0
    vCnt = 0
    for x in agentsArray:
        if x.getPref() == "meat":
            mCnt += 1
        elif x.getPref() == "fish":
            fCnt += 1
        else:
            vCnt += 1

        print str(x.getIDA())+ " " + x.getPref()
        RecTest(x)

    print
    print "mCnt: " + str(mCnt)
    print "fCnt: " + str(fCnt)
    print "vCnt: " + str(vCnt)

def RetAllAgents():
    """
    Similar to RetAllGenAgents(agentsArray) but it accesses the global dictionary Generation.agentsOverAllDict
     goes through all Generations and prints the Agents, their preferences and the ingredients list of the recipe
    :return: Printed out visual representation of the Agents created so far
    """
    mCnt = 0
    fCnt = 0
    vCnt = 0
    print cfg.agentsOverAllDict.__len__()
    for alst in cfg.agentsOverAllDict:
        for x in cfg.agentsOverAllDict[alst]:
            if x.getPref() == "meat":
                mCnt += 1
            elif x.getPref() == "fish":
                fCnt += 1
            else:
                vCnt += 1

            print str(x.getIDA())+ " " + x.getPref()

    print
    print "mCnt: " + str(mCnt)
    print "fCnt: " + str(fCnt)
    print "vCnt: " + str(vCnt)

def getRecipies(start,end):
    """
    Assuming we expand the Recipes an Agent can hold and work with to more than one, this method
    would return a visual representation of the Recipes of a certain range in the list that holds them
    :param start: First Recipe to visually return = list index position
    :param end: Last Recipe to visually return = list index position
    :return: Visual representation of all Recipes between and including 'start' and 'end'
    """
    for recipe in REx.recipes[start:end]:
        print
        print("Category: " + recipe.category.split("\\")[-1])
        print("Title: " + recipe.title)
        print("PrepTime: " + recipe.rel_prep_time)
        print("Ingreds: ")
        print(recipe.ingredients)
        print("Ing Size: " + str(recipe.ing_size))
        print("Score: " + str(recipe.score))

def RetAllRec():

    for recipe in REx.recipes:
        print
        print("Category: " + recipe.category.split("\\")[-1])
        print("Title: " + recipe.title)
        print("PrepTime: " + recipe.rel_prep_time)
        print("Ingreds: ")
        print(recipe.ingredients)
        print("Ing Size: " + str(recipe.ing_size))
        print("Score: " + str(recipe.score))

def RetDciFromArray(array):
    dict = {}
    for x in array:
        rname = x.getRec().title

        x.getRec().counter += 1
        dict1 = {rname:x.getRec().counter}
        dict.update(dict1)

    for x in dict:
        print x + " - " + str(dict[x])

def RetGenRecArr(index):

    for rec in cfg.ArraysOverGenerations[index]:
        print
        print (rec.title)
        print ("Score: " + str(rec.score))

def RetWinGenRecArr(index):

    print cfg.WinningArrsOverGenerations.__len__()
    print cfg.WinningArrsOverGenerations[index].__len__()

    for rec in cfg.WinningArrsOverGenerations[index]:
        print "Score {:4}   -  Cat.: {:>5}  -   Title: {}".format(rec.score,rec.category,rec.title)

def RetSGArrs(index):
    """

    :return: All Agents in their 'social environment' for the indexed generation plus the score of their recipe
    """
    counter = 0
    for SGarr in cfg.SocialGroups[index]:
        print
        print "new Group: Size: " + str(SGarr.__len__() )
        for agnt in SGarr:
                print " AgentSGID: {:3} | AgentID {:3}  |   RecScore: {:3}  |  RecCateg: {:6}  |  #Ingreds: {:3}".format(agnt.sgID,agnt.getIDA(),
                                   agnt.getRec().score,agnt.getRec().category, agnt.getRec().ing_size)
                if agnt.ancestors != 0:
                    print " Parent: {:3}".format(agnt.ancestors)
                counter += 1
        print


    print ("----------")
    print ("Sum of Agents: " + str(counter))

def RetSGArrsRec(index):
    """
    Same as RetSGArrs(index) = All Agents in their 'social environment' for the indexed generation
    plus the score of their recipe plus the name of the recipe
    :return:

    """
    counter = 0
    for SGarr in cfg.SocialGroups[index]:
        print
        print "new Group: Size: " + str(SGarr.__len__() )
        for agnt in SGarr:
                print " AgentSGID: {:3} | AgentID {:3}  |   RecScore: {:3}  |  RecCateg: {:6}  |  #Ingreds: {:3}  |  Name: {:35}".format(agnt.sgID,agnt.getIDA(),
                                   agnt.getRec().score,agnt.getRec().category, agnt.getRec().ing_size, agnt.getRec().title)
                if agnt.ancestors != 0:
                    print " Parent: {:3}".format(agnt.ancestors)
                counter += 1
        print

    print ("----------")
    print ("Sum of Agents: " + str(counter))