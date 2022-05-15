from solution import SOLUTION
import copy
import constants as c

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
    
    def Evolve(self):
        self.parent.Evaluate("DIRECT");
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
    
    def Mutate(self):
        self.child.Mutate();
        # print(self.parent.weights)
        # print(self.child.weights)

    def Select(self):
        # print(self.parent.fitness)
        # print(self.child.fitness)
        if(self.parent.fitness>self.child.fitness):
            self.parent=self.child
    
    def Print(self):
        print("\n---->\nparent fitness:",self.parent.fitness, " / child fitness:", self.child.fitness,"\n")
    
    def Show_Best(self):
        self.parent.Evaluate("GUI")
