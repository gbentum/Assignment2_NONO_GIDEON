
import random as r
from ROOT import *
import numpy as np


def uniform(a,b) : 
        rn = (b-a)*r.random() + a
        return rn
        
def g(x,mu,sigma) : 
        val = (1./(sigma*np.sqrt(2*np.pi)))*np.exp((-0.5*(x-mu)*(x-mu))/(sigma*sigma)) 
        return val


def main() : 
        list_x = [] 
        list_u = []
        g_x = []
        sigma = 1.4
        mu = 2.0

        for i in range(100000) : 
                x = uniform(-10,10)
                list_x.append(x)
                g_x.append(g(x,mu,sigma))
        
        max_gx = max(g_x)
                
        for i in range(100000)  : 
                u = uniform(0,max_gx)
                list_u.append(u)
        list_accepted_x = []
        
        
        for i in range(len(list_x)): 
                if list_u[i]<g(list_x[i],mu,sigma) : 
                        list_accepted_x.append(list_x[i])
        
        print len(g_x)
        
        
        #canvas for drawing
        c   = TCanvas("c","c",200,200)
        #c.Divide(2,2)

        #make initial histogram of the distances
        h1 = TH1F("h1","h1 1D",100,-10,10)
        for val in list_accepted_x:
                 h1.Fill(val)
    
        #draw the data histogram
        #c.cd(1)
        h1.SetLineColor(2)
        h1.SetMinimum(0)
        h1.Draw("hist")
        
        c.SaveAs("histogram_gauss_number.eps")
        
       

if __name__ == "__main__" : 
        main()
