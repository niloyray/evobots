from solution import SOLUTION
import copy
import constants as c
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for currentParent in range(c.populationSize):
            self.parents[currentParent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        # self.parent = SOLUTION()
    
    def Evolve(self):
        self.Evaluate(self.parents, "DIRECT");
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children,"DIRECT")
        self.Print()
        self.Select()
    
    def Spawn(self):
        self.children = {}
        for currentParent in range(c.populationSize):
            self.children[currentParent] = copy.deepcopy(self.parents[currentParent])
            self.children[currentParent].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1
        
        # for currentParent in range(c.populationSize):
        #     print(self.children[currentParent]) 

    def Mutate(self):
        for currentParent in range(c.populationSize):
            self.children[currentParent].Mutate();
        # print(self.parent.weights)
        # print(self.child.weights)
    
    def Evaluate(self, solutions, directOrGUI):
        for currentParent in range(c.populationSize):
            solutions[currentParent].Start_Simulation(directOrGUI)
        for currentParent in range(c.populationSize):
            solutions[currentParent].Wait_For_Simulation_To_End()

    def Select(self):
        # print(self.parent.fitness)
        # print(self.child.fitness)
        for currentParent in range(c.populationSize):
            if(self.parents[currentParent].fitness>self.children[currentParent].fitness):
                self.parents[currentParent]=self.children[currentParent]
    
    def Print(self):
        print("\n")
        for currentParent in range(c.populationSize):
            print("\n>>> Parent fitness:",self.parents[currentParent].fitness, " / Child fitness:", self.children[currentParent].fitness)
        print("\n")
        
    
    def Show_Best(self):
        parentForMaxFitness = 0
        maxFitness = 0
        for currentParent in range(c.populationSize):
            if(self.parents[currentParent].fitness < maxFitness):
                maxFitness = self.parents[currentParent].fitness
                parentForMaxFitness = currentParent
        self.parents[parentForMaxFitness].Start_Simulation("GUI")
