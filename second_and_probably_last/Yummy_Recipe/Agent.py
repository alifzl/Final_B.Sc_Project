"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

"""

import copy
import random
import Generation

from Recipe import *
import Recipe as REx
import Config as cfg


random.seed()


class Agent(object):

    inPref = []
    timePref = "none"

    preferences = ["meat","fish","veggi"]

    recipies = []

    def setIDA(self):
        """
        Function to assign each Agent instance a easy to read ID for quick testing purposes

        :return:
        """

        self.idA = cfg.idA
        cfg.idA += 1

    def getIDA(self):
        """
        Read out the easy to read ID provided by Agent.setIDA()
        :return:
        """
        return self.idA

    def getRec(self):

        '''
        :return: The Recipies that this agent uses
        '''

        # ReviewMe : giving back only the 1st one at the moment
        return self.recipies[0]

    def mutate(self):
        
        if do_mutate:

            recipe = self.recipies[0]
            actions = ["none", "add", "delete", "substitute"]
            random_number = random.randrange(len(actions))
        
            action = actions[random_number]

            if action == "delete" and recipe.retLength() >= 3:

                x = random.randrange(recipe.retLength())
                ingr = recipe.ingredients.pop(x)
                recipe.mutate_history.append([self.idA,"deleted " + ingr])

            elif action == "add":

                x = random.randrange(len(all_ingredients))
                recipe.ingredients.append(all_ingredients[x])
                recipe.mutate_history.append([self.idA,"added " + all_ingredients[x]])

            elif action == "substitute" and recipe.retLength() >= 3:

                x = random.randrange(recipe.retLength())
                y = random.randrange(len(all_ingredients))

                ingr1 = recipe.ingredients.pop(x)
                recipe.ingredients.append(all_ingredients[y])
                recipe.mutate_history.append([self.idA,"substituted " + ingr1 + " with " + all_ingredients[y]])

            else:

                recipe.mutate_history.append([self.idA,"none"])


    def __init__(self, pref,parent,GenPath):


        # each Agent will eventually be assigned to a social group, we may want to know
        # to which one later on:
        self.sgID = None

        # start with empty list of recipies for each Agent, ReviewMe self.recipies = [] should be correct
        self.recipies = []

        # List of IDs of ancestor agents, in order (oldest at [0] - direct parent at [__len__()-1]),
        self.ancestors = []

        if ( isinstance(parent,Agent)):
            # Adding the parent element of each Agent of a Generation different than
            # the first Generation to this Agents ancestry
            # ReviewMe: actually using two agents as 'parents', right now we have a very modern single parent society

            self.parent = parent

            if self.parent.ancestors.__len__() == 0 :
                self.ancestors.append(self.parent.idA)
            else:
                self.ancestors += self.parent.ancestors
                self.ancestors.append(self.parent.idA)



        # check if Agent has a valid preference
        if (isinstance(pref,str) and any(pref in x for x in self.preferences) ):
            self.preference = pref

            self.setIDA()

            # ReviewMe: differentiation between Agents in the 1st Gen and the following ones, just use number of Agents as threshold
            # an 'Original' Agent or not?
            if self.ancestors.__len__() > 0:

                # every agent should get the recipe assigned that was the winner in his parents social group
                # the parent ID is:     self.ancestors[self.ancestors.__len__()-1]]
                # the Agent instance for that ID can be found (in constant time) under:
                #                       Generation.agentsOverGenerations[self.ancestors[self.ancestors.__len__()-1]]

                # ReviewMe: copying of Recipes as DEEPCOPYs, otherwise we will constantly add to the same object instance, not individual ones
                index_gen = cfg.agentsOverGenerations[self.ancestors[self.ancestors.__len__()-1]].sgID[0]
                index_socLst = cfg.agentsOverGenerations[self.ancestors[self.ancestors.__len__()-1]].sgID[1]
                self.recipies.append(copy.deepcopy(cfg.WinningArrsOverGenerations[index_gen][index_socLst]))
                # ReviewMe: accumulate score or not? FixMe
                self.recipies[0].score = 0

            else:
                if self.preference == "meat":
                    self.thelist = REx.recipesMeat
                elif self.preference == "fish":
                    self.thelist = REx.recipesFish
                elif self.preference == "veggi":
                    self.thelist = REx.recipesVeggi

                # only use the main preference to randomly pick recipe
                self.recipies = random.sample(copy.deepcopy(self.thelist),1)
                # determine what time is acceptable for this Agent
                self.timePref = self.recipies[0].rel_prep_time

        else:
            print("Agent.__init__() - error: false parameters at instantiation")

        self.mutate()


    def __eq__(self,other):
        # test for equality according to our definition
        # question arises: when are two recipes equal = ReviewMe
        if type(self)==type(other):
            if (self.getIDA() == other.getIDA()):
                return True
            else:
                return False
        else:
            return "Agent.__eq__() : Wrong type! Need 'Agent' type to compare."


    def getPref(self):
        return self.preference
    
    
    def judgeMyRec(self,agentOb):

        # ReviewMe: Balancing of the points assigned to the individual Recipe score
        # if each ingred gets one point we have a bias for recipies with many
        # ingreds (not necessarily a bad thing), but we have to adjust the time too
        # by using margins as discussed, e.g., fast - medium - long and respective points

        self.judgeSc = 0

        if not type(agentOb) is Agent:
            sys.exit("Agent.judgeMyRec() - object not of type Agent")
        else:
            #print()
            #print("Agent: " + str(agentOb.getIDA()))
            if self.getPref() == agentOb.getPref():
                self.getRec().score += 4
                self.judgeSc += 4
            if self.timePref == agentOb.getRec().rel_prep_time:
                self.getRec().score += 2
                self.judgeSc += 2
            for i in agentOb.getRec().ingredients:
                if i in  self.getRec().ingredients:
                    self.getRec().score += 1
                    self.judgeSc += 1


    def setSocGrp(self,genCounter,sgID):
        """
        Sets the ID for this Agents Social Group
        :param genCounter: Generation in which this Agent occurred
        :param sgID: Social Group in which this Agent occurred
        :return: nothing
        """
        self.sgID = [genCounter,sgID]

    def getSocGrp(self):
        """
        A textual representation of the SocialGroup this Agent belongs to
        :return: String holding information about this Agents SocialGroup
        """
        return "Gen-{:2} SG-{:2}".format(self.sgID[0],self.sgID[1])