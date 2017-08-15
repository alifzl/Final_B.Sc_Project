"""
    Cultural Evolution Simulation (Yummy_Recipe)

    Ali Fazeli

    Final Project of B.sc Level in Computer Engineering

    Task:           Simulate changes in recipes within a population of Agents over several
                    generations depending on different rule sets.

    Module Descr.:  General setup of our simulation with GUI implementation

"""


import os
from Tkinter import *
from tkMessageBox import askokcancel


# ==================================
# generations: Amount of Generations

# =============================================
# numberAgents: Amount of Agents per Generation

# ==================================================================
# facMeat, facFish, facVeggi: Percentages of our main recipe classes

# ==============================================================
# maxSocSize: Maximum size of social groups/ groups of 'friends'
# maxSocSize shall not be smaller than 3!

# ====================================================================================
# numberOfSimulationRuns: How often should we repeat the individual CultEvo simulation

# ==========================
# do_mutate: Toggle mutation

# =================================================================================================
# Thresholds for what is considered a long/medium/short recipe ingredient list/ preparation time
from skimage.viewer.utils import canvas

timeDic = {"short":"0:25","medium":"1:00"}  # more than 1:00 implicates long
recDic = {"short":5,"medium":10}            # more than 10 elements implicates a long list

parameter = []

defaultsPath = os.path.dirname(os.path.realpath(__file__)) + "/"

if os.path.isfile(defaultsPath+".defaults.txt"):
    defaults = []
    f = open(defaultsPath+".defaults.txt","r")
    for line in f.readlines():
        defaults.append(line.strip())
    f.close()
else:
    defaults = 8, 60, 10, 3,\
              20, 20, 20,\
              "True"

fields = "Number of Generations:", "Number of Agents:", "Max Size of Social Groups:","Number of Simulations:",\
         "Meat Agents %:", "Fish Agents %:", "Veggi Agents %:",\
         "Mutate:"


# ===================================
#           Presets - GUI
# ===================================

class StartWindow(Frame):                          
    def __init__(self, parent=None):           
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='2. START Simulation', command=self.start)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def start(self):
        answer = askokcancel('', "Values set and ready to run?")
        if answer: Frame.quit(self)

def run(input):
    global parameter
    parameter = [x.get() for x in input]
    generations     = int(parameter[0])
    numberAgents    = int(parameter[1])
    maxSocSize		= int(parameter[2])
    numberOfSimulationRuns = int(parameter[3])
    facMeat         = int(parameter[4])
    facFish         = int(parameter[5])
    facVeggi        = int(parameter[6])
    do_mutate       = bool(parameter[7])
    print(parameter)

def create(root, fields):
    form = Frame(root)                              
    left = Frame(form)
    right = Frame(form)
    form.pack(fill=X) 
    left.pack(side=LEFT, padx = 5, pady = 5)
    right.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    default = 0
    for field in fields:
        lab = Label(left, text=field)
        ent = Entry(right)
        lab.pack(side=TOP, anchor=E)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        
        var.set(defaults[default])
        variables.append(var)

        default += 1
    return variables


root = Tk()
root.title("Cultural Evolution simulator (Yummy Recipe)")
root.geometry("480x250")
root.iconbitmap(default='icon.ico')
# TODO : fix this to plain freakin text
T = Text(root, height=1, width=500)
T.pack(side=TOP)
T.insert(END, "Cooking Recipe Evolution Simulator, Powered by Ali Fazeli !")

vars = create(root, fields)
Button(root, text='1. Accept Values', command=(lambda v=vars: run(v))).pack(side=LEFT)

StartWindow(root).pack(side=RIGHT)
root.bind('<Return>', (lambda event, v=vars: run(v)))   
root.mainloop()

if len(parameter) != 0:
    generations     = int(parameter[0])
    numberAgents    = int(parameter[1])
    maxSocSize		= int(parameter[2])
    numberOfSimulationRuns = int(parameter[3])
    facMeat         = int(parameter[4])
    facFish         = int(parameter[5])
    facVeggi        = int(parameter[6])
    do_mutate       = bool(parameter[7])
    
    f = open(defaultsPath+".defaults.txt","w")
    f.write(parameter[0])
    for set_par in parameter[1:]:
        f.write("\n"+set_par)
    f.close()
else:
    sys.exit("Cultural Evolution Simulator is closed.")