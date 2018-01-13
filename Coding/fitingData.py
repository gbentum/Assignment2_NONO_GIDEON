'''
@Author 
@email : 

This program tries to fit one set of Data 

'''

import random as r

def f(x,m,b) : 
        return m*x+b
        
def s(f_x,y) : 
        
        i=0
        sum_s=0.0
        print len(f_x)
        while i < len(f_x) :
                print i
                val =(f_x[i]-y[i])
                sum_s = sum_s+(val*val)
                i = i +1
        return sum_s

def uniform(a,b) : 
        rn = (b-a)*r.random() + a
        return rn

def main() : 
        #chosen values of m and b 
        m,b = 0.5,0
        list_x = [1.0,2.2,3.0,3.9,4.8]
        list_y = [0.5,1.1,1.3,2.1,2.6]
        list_s = []
        
        for i in range(10):
                b = uniform(0,0.2)
                m = uniform(0.3,0.5)
                fx = []
                for x in list_x : 
                        fx.append(x*m+b)
                s_val = s(fx,list_y)
                list_s.append(s_val)
                
        print list_s   
        
        
        
        
        
        
        
   
        
if __name__ =="__main__" : 

        main()
