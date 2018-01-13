'''
@Author : NONO SAHA Cyrille

Generate a random number between [0,1] using the evolution function 

'''
from ROOT import *
import array
import matplotlib.pyplot as plt
import numpy as np

def vonNeumann(x) :
        return (2/np.pi)*np.arcsin(np.sqrt(x)) 
        
        
       
def evolution(lamda, x) : 
        return 4*lamda*x*(1-x)      


def main() : 
        lamda = 1
        x= 0.7
        N = 1000000
        list_x = array.array('d')
        list_y = array.array('d')
        i = 0
        while i < N:
                list_x.append(x)
                y = evolution(lamda,x)
                list_y.append(y)
                x = evolution(lamda,x)
                i = i+1
                x = y
                
                
        for i in range(10) : 
                print "(", list_x[i], list_y[i], ")"
        print len(list_x), len(list_y)
        
        
        
        #canvas for drawing
        c   = TCanvas("c","c",200,200)
        c.Divide(1,2)
        
        
        #make initial histogram of the distances
        h1 = TH1F("hdata","Logistic On 1D",100,0,1)
        for val in list_x:
                 hdata.Fill(val)
    
        #draw the data histogram
        c.cd(1)
        h1.SetLineColor(2)
        h1.SetMinimum(0)
        h1.Draw("same")
        
        #Remove the statistic box on histograms
        h1.SetStats(kFALSE)
       
        #Transform the logistic equation applying von Neuman function
        list_yn = (2/np.pi)*np.arcsin(np.sqrt(list_x))
        h2 = TH1F("Neumann","Neumann on 1D",100,0,1)
        for yn in list_yn : 
                h2.Fill(yn)
        h2.SetLineColor( 3)
        h2.SetStats(kFALSE)
        h2.SetMinimum(0)
        h2.Draw("same")
        
        #2D ploting Histogram 
        h2D = TH2F("2DH","Logistic 2D",100,0,1,100,0,1)
        h2DV = TH2F("2DHV","Logistic 2D",100,0,1,100,0,1)
        
        for i in range(len(list_y)) : 
                h2D.Fill(list_x[i],list_y[i])
                h2DV.Fill(vonNeumann(list_x[i]),vonNeumann(list_y[i]))
        
        # label the axes
        h2D.GetXaxis().SetTitle( 'x axis label' )
        h2D.GetYaxis().SetTitle( 'y axis label' )
        h2DV.SetLineColor( 3)
        h2D.SetStats(kFALSE)
       
        c.cd(2)
        h2D.Draw("colz")
        h2DV.Draw("same")
        
        c.SaveAs("logistic-histogram.eps")
        
        
if __name__=="__main__" : 
        main()
