import agentpy as ap
import numpy as np
import seaborn as sns




#Las clases seran los agentes pero se tiene que heredar 
#de la libreria lo de ap.agent para que si sea
class WealthAgent(ap.Agent):
    def setup(self):
        self.wealth = 1
    def wealth_transfer(self):
        if self.wealth > 0:
            partner = self.model.agents.random()
            partner.wealth += 1
            self.wealth -= 1
            
class WealthModel(ap.Model):
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, WealthAgent)
        pass
        
    def step(self):
        self.agents.wealth_transfer()
        pass
    
    def update(self):
#        self.record('Gini Coefficient', gini(self.agents.wealth))
        pass
    
    def end(self):
        self.agents.record('wealth')
        pass 