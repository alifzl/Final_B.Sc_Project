"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

"""

import os
import time
import random

import Write
import Generation
import Config as cfg
import Presets as P

random.seed()


class CultEvo(object):

    numOfGenerations = 0


    def __init__(self, ce_id):
        # check if there is "Simulations" folder is already created or not
        self.simulationsPath = os.path.dirname(os.path.realpath(__file__)) + "/Simulations/"
        if os.path.isdir(self.simulationsPath):
            pass
        else:
            os.makedirs(self.simulationsPath)

        # Collection of all CultEvo runs
        # something of the form : ..cwd..\Simulations_2016-03-04_[13_23_06]\
        self.simulationPath = self.simulationsPath + "Sim_{}/".format(ce_id)
        if os.path.isdir(self.simulationPath):
            pass
        else:
            # create folders with specific simulation detail as their name
            os.makedirs(self.simulationPath)

        # individual simulation run paths(holding all its generation folders):
        self.simRunPath = self.simulationPath + "SimRun_000/"

        if os.listdir(self.simulationPath).__len__() == 0:
            os.makedirs(self.simRunPath)

        else:
            # get the highest index of the already existing folders.

            self.simRunPath = self.simulationPath + "SimRun_{:03}/".format(int(sorted(os.listdir(self.simulationPath))[-1].split("_")[1])+1)
            os.makedirs(self.simRunPath)


        # for Generation folders check in Generation.py



        # Variable determining how many generations we wan t toallow
        generations = P.generations

        generation_run = Generation.Generation(P.numberAgents,generations,self.simRunPath)

        self.numOfGenerations = generation_run.countGenUp


lstOfGenerationsNumbers = []

# setting up an unique identifier for each simulation using system time
ce_id = time.strftime("%Y-%m-%d_") + time.strftime("[%H_%M_%S]")

for x in range(P.numberOfSimulationRuns):

    # reset Config values for each individual simulation run
    cfg.config_reset()

    runX = CultEvo(ce_id);

    lstOfGenerationsNumbers.append(runX.numOfGenerations)


# writing statistics
Write.WriteStatistics(P, lstOfGenerationsNumbers)