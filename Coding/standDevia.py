'''
@author : NONO SAHA Cyrille Merleau     
@email : csaha@aims.edu.gh      

'''

def main() : 
        
        xi = [71, 51, 32, 62, 84, 109, 43, 92, 72, 41, 102, 80, 72, 69, 46, 94, 52, 95, 90, 72, 63, 70, 34, 80, 78, 34, 31, 37,
        26, 41, 42, 107, 33, 108, 108, 75, 66, 23, 90, 53, 24, 70, 26, 41, 93, 24, 71, 39, 48, 66, 97, 107, 77, 71, 67, 39, 38,
        107, 96, 92, 84, 46, 60, 95, 87, 90, 92, 63, 78, 78, 84, 107, 70, 108, 32, 36, 93, 108, 49, 72, 56, 43, 30, 56, 51, 97, 45,
        92, 40, 43, 49, 83, 98, 28, 99, 97, 102, 89, 58, 87]

        #Average of xi
        x_avg = avg_(xi)
        
        print "My len = ", len_(xi)," standard = ", len(xi)
        
        print "My sum = ", sum_(xi)," standard = ", sum(xi)
        
        print "My avg = ", avg_(xi)," standard = ", sum(xi)/float(len(xi))
        
        s = 0
        for x in xi :
                s = s + (x-x_avg) * (x-x_avg) 
        
        #Compute standard deviation 
        sigma = nsqrt(s/len_(xi))
        
        print "The standard deviation of the given list is : ", sigma
                











#Square root 

def nsqrt(n) : 
        
        minsqrt = 0 
        j= n +1
        maxsqrt= perfectSqrt(int(j))
        while maxsqrt ==0 : 
                maxsqrt = perfectSqrt(int(j))
                j+=1
                          
        for i in range(2,int(n+1)) : 
                if perfectSqrt(i) !=0 : 
                        minsqrt = perfectSqrt(i) 
        val = (maxsqrt+minsqrt)/2.
        while maxsqrt-minsqrt >=0.0001: 
                
                if val*val < n : 
                        minsqrt = val
                else : 
                        maxsqrt = val
                val = (maxsqrt+minsqrt)/2.
        
        return maxsqrt
         

            
def perfectSqrt(n) : 
         
        if n == 1 :
                return 1
        for i in range(2,int(n+1)) : 
                if n%i == 0 :
                        if i ==n/i : 
                                return i
        return 0 
         


#Sum of elements for the given list
def sum_(list_) : 
        
        s = 0 
        for val in list_ : 
                s=s+val
        return s

#Length of a given list 
def len_(list_) : 
       l = 0 
       for i in list_ : 
                l = l+1
       return l 
       
 
#Average for the given list 
def avg_(list_) : 
        N = float(len_(list_))
        return sum_(list_)/N
        


if __name__ == "__main__" : 

        main()





