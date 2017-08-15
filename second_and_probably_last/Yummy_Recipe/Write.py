
"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

"""


import time
import os
import Analysis as stat
from Presets import facMeat, facFish, facVeggi

# write general data about this generation to a file
class WriteGen(object):
    """
    Writing a textual class representation of this Generation to a file
    """

    def __init__(self,genPath,countGenUp,agentArr,SGArrs,winGenRecArr,WinningArrsOverGenerations,agentsOverAllDict,agentsOverGenerations):

        f = open(genPath+"Gen_and_SocGrps_{:03}.txt".format(countGenUp),'w')
        f.write("\n")
        f.write("Yummy Recipe Report:\n")
        f.write("==============================\n")
        f.write("\n")
        f.write("Author: Ali Fazeli\n")
        f.write("Date  : {}\n".format(time.strftime("%Y-%m-%d at ") + time.strftime("[%H:%M:%S]")))
        f.write("\n")
        f.write("\n")
        f.write("Generation Overview\n")
        f.write("===================\n")
        f.write("\n")
        f.write("\n")
        f.write("Number of Agents       : {:03}\n".format(agentArr.__len__()))
        f.write("Number of Social Groups: {:03}\n".format(SGArrs.__len__()))
        f.write("Number of Meat eaters  : {:03}\n".format(facMeat))
        f.write("Number of Fish eaters  : {:03}\n".format(facFish))
        f.write("Number of Vegetarians  : {:03}\n".format(facVeggi))
        f.write("\n")
        f.write("\n")
        f.write("Social Groups:\n")
        f.write("--------------\n")
        for sg in SGArrs:
            f.write("SG Number: {:02}\n".format(SGArrs.index(sg)))
            for agnt in sg:
                f.write("   Agent         : {:03}\n".format(agnt.getIDA()))
            f.write("   Winning recipe: {}, {} likes\n".format(winGenRecArr[SGArrs.index(sg)].title, winGenRecArr[SGArrs.index(sg)].score))
            f.write("\n")

        f.write("Sum of all agents so far            : {}\n".format(agentsOverGenerations.__len__()))
        f.write("size of agentsOverAllDict           : {}\n".format(agentsOverAllDict.__len__()))
        f.write("and in the current generation:\n")
        for agnt in agentsOverAllDict[countGenUp]:
            f.write("   Agent {}\n".format(agnt.getIDA()))
        f.write("\nsize of WinningArrsOverGenerations  : {}\n\n\n".format(WinningArrsOverGenerations.__len__()))

        f.write("\nOverview over all Generations:\n")
        f.write("==============================\n\n")
        f.write("All recipes contained: \n")
        
        n = 1
        for reclst in WinningArrsOverGenerations:
            f.write("\nGeneration " + str(n) + ":\n")
            f.write("------   ------   ------\n")
            for rec in WinningArrsOverGenerations[reclst]:
                f.write("   RecName: {:>40}, {:>3} likes\n".format(rec.title, rec.score))
            n += 1
        f.close()


class WriteAgent(object):
    """
    Writing a textual class representation of this Agent to a file
    """

    def __init__(self,genPath,agnt):
        f = open(genPath+"Agent_{:03}.txt".format(agnt.getIDA()),'w')
        f.write("\n")
        f.write("Cultural Evolution Simulation:\n")
        f.write("==============================\n")
        f.write("\n")
        f.write("Author: Ali FZL\n")
        f.write("Date  : {}\n".format(time.strftime("%Y-%m-%d at ") + time.strftime("[%H:%M:%S]")))
        f.write("\n")
        f.write("\n")
        f.write("Agent Overview\n")
        f.write("==============\n")
        f.write("\n")
        f.write("ID        : {:>6}\n".format(agnt.getIDA()))
        f.write("Preference: {:>6}\n".format(agnt.preference))
        f.write("\n")
        f.write("Recipe    : {}\n".format(agnt.getRec().title))
        f.close()


class WriteStatistics(object):
    """
    Writing a textual class representation of Statistics 
    """

    def __init__(self, P, lstOfGenerationsNumbers):

        outputPath = os.path.dirname(os.path.realpath(__file__)) + "/"
        f = open(outputPath+"Stats.txt","w")
        f.write(" ====================================================== \n")
        f.write("||                                                    ||\n")
        f.write("||   Statistical Properties of this simulation run    ||\n")
        f.write("||                                                    ||\n")
        f.write(" ====================================================== \n\n\n")

        f.write("Number of Agents                 : {:>5}\n".format(P.numberAgents))
        f.write("Maximum size of social groups    : {:>5}\n".format(P.maxSocSize))
        f.write("Maximum number of Generations    : {:>5}\n".format(P.generations))
        f.write("Number of individual CultEvo runs: {:>5}\n\n\n\n".format(P.numberOfSimulationRuns))

        f.write("Values:\n")
        f.write("=======\n\n")

        f.write("Averages and measures of central location\n")
        f.write(".........................................\n\n")

        f.write("mean        : {:>6.2f}\n".format(stat.mean(lstOfGenerationsNumbers)))
        f.write("median      : {:>6.2f}\n".format(stat.median(lstOfGenerationsNumbers)))
        f.write("mean_low    : {:>6.2f}\n".format(stat.median_low(lstOfGenerationsNumbers)))
        f.write("mean_high   : {:>6.2f}\n".format(stat.median_high(lstOfGenerationsNumbers)))
        f.write("mean_grouped: {:>6.2f}\n".format(stat.median_grouped(lstOfGenerationsNumbers)))
        try:
            f.write("mode        : {:>6.2f}\n\n\n\n".format(stat.mode(lstOfGenerationsNumbers) ))
        except :
            f.write("mode        : two equal values found\n")

        f.write("Measures of spread\n")
        f.write("..................\n\n")

        f.write("Population standard deviation of data: {0:>6.2f}\n".format(stat.pstdev(lstOfGenerationsNumbers)))
        f.write("Population variance of data          : {0:>6.2f}\n".format(stat.pvariance(lstOfGenerationsNumbers)))
        f.write("Sample standard deviation of data    : {0:>6.2f}\n".format(stat.stdev(lstOfGenerationsNumbers)))
        f.write("Sample variance of data              : {0:>6.2f}\n".format(stat.variance(lstOfGenerationsNumbers)))
        f.close()