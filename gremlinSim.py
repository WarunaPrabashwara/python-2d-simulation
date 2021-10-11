
import matplotlib.pyplot as plt
import numpy as np
import random
import math 
import asyncio
#from playsound import playsound

MAXROW = 20
MAXCOL = 30

def processline(line1):
    newlist = [(int(l.split(",")[0]),int(l.split(",")[1])) for l in line1[1:]]
    return newlist
    
def read_data(filename):
    file = open(filename,'r')
    data = file.readlines()
    lists = []
    for line in data:
        new_list = processline(line.split(":"))
        lists.append(new_list)
    #print("Array prints here to test ", lists)
    wlist = lists [0]
    flist = lists [1]
    livingPlaceofCatAbysinian = lists [2]
    livingPlaceofCatBobtall = lists [3]
    livingPlaceofCatBeliness = lists [4]
    return wlist, flist,livingPlaceofCatAbysinian,livingPlaceofCatBobtall,livingPlaceofCatBeliness
    
def move_em(current, moves , far):
    nextgrid = np.zeros(current.shape, dtype="int16")
    
    for row in range(MAXROW):
        for col in range(MAXCOL):
            for g in range(current[row,col]):
                nextrow = row + random.choice(moves)
                nextcol = col + random.choice(moves)
                #print("Newpos = ", nextrow, nextcol)
                if nextrow < 0:
                    nextrow = 0
                if nextcol < 0:
                    nextcol = 0
                if nextrow >= MAXROW:
                    nextrow = MAXROW - 1
                if nextcol >= MAXCOL:
                    nextcol = MAXCOL - 1
                far = far + math.sqrt(abs(nextrow)**2 + abs(nextcol)**2 )
                nextgrid[nextrow, nextcol] += 1
    return nextgrid , far

async def rule1(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    lightlist.remove((row ,col))
                    print("Abysinian ate a food")  
                    #playsound('foodwaw.wav', False)     

async def Abasiankillcatsrule(pop, cat2 , cat3 , cat2color ,cat3color ):
    print("fff")
    print(cat2)
    print(cat3)
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in cat2:
                for g in range(pop[row,col]):
                    cat2color = "black"
                    print("Abysinian attacked CatBobtall")  
                    #playsound('foodwaw.wav', False)     
            if (row, col) in cat3:
                for g in range(pop[row,col]):
                    cat3color = "black"
                    print("Abysinian aacked Beliness")  
                    #playsound('foodwaw.wav', False)    

async def waterdrinkrule(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    lightlist.remove((row ,col))
                    print("Abysinian drank water")  
                    #playsound('waterwav.wav', False)     

async def rule1Bobtall(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    lightlist.remove((row ,col))
                    print("Bobtall ate the food")  
                    #playsound('foodwaw.wav', False)     

async def waterdrinkruleBobtall(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    lightlist.remove((row ,col))
                    print("Bobtall drank water")  
                    #playsound('waterwav.wav', False)     

async def rule1Beliness(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    lightlist.remove((row ,col))
                    print("Beliness ate the food")  
                    #playsound('foodwaw.wav', False)     

async def waterdrinkruleBeliness(pop, lightlist):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if (row, col) in lightlist:
                for g in range(pop[row,col]):
                    lightlist.remove((row ,col))
                    print("Beliness drank water")  
                    #playsound('waterwav.wav', False)     
                                          
async def abaysiankillsbobtail(pop, waterlist , attackedbobtailarray):
    for row in range(MAXROW):
        for col in range(MAXCOL):
            for k in range(waterlist[row,col]) :
                if  waterlist[row,col] == 1 :
                    for g in range(pop[row,col]):
                        waterlist[row, col] -= 1
                        attackedbobtailarray[row, col] += 1
                        print("abaysian ataacked bobtail so bobtail became black")


def make_feature_scatter(itemlist, colour):
    xlist = []
    ylist = []
    for r,c in itemlist:
        ylist.append(MAXROW - r - 1)  
        xlist.append(c) 
    plt.scatter(xlist,ylist,color=colour, marker='s')
    
def make_gremlin_scatter(pop, colour):
    xlist = []
    ylist = []
    slist = []
    for row in range(MAXROW):
        for col in range(MAXCOL):
            if pop[row,col] > 0:
                ylist.append(MAXROW - row - 1)  
                xlist.append(col) #flip rows/columns to y/x
                slist.append(pop[row,col]*20)
    plt.scatter(xlist,ylist,s=slist,color=colour)
  
def printpart() :
    print("### Water is in blue colour ### Food is in Green colour ")
    print("          ")
    print("### Abysinian cat is in red colour . It is very aggressive behaviour , moves fast .")
    print("          ")
    print("### bob tall cat is in magenta colour . It has a neutral behaviour ")
    print("          ")
    print("### Beliness javanese cat is in orange colour . It has a calm behavious . It doesn't go much away  from living place like othe both cats do It starts near by its house unlike other cats")
    print("          ")
    print("###  abaysian ataacks bobtail then bobtail became black and remain still .")
    print(" (if you didn't see this feature you can increase initpop  of inputs to 10 and  range of inputs to 105 . Rarely , if you get any error pleae re run code )")
    print("          ")
    print("### Their homes have same colours but homes don't move like cats do ### ")
    print("          ")

async def main():

    Abysinianarray = np.zeros((MAXROW,MAXCOL), dtype="int16")
    Bobtallarray = np.zeros((MAXROW,MAXCOL), dtype="int16")
    attackedbobtailarray = np.zeros((MAXROW,MAXCOL), dtype="int16")
    Belinessarray = np.zeros((MAXROW,MAXCOL), dtype="int16")
    cat2color = "magenta"
    cat3color = "orange"
    water, food ,livingPlaceofCatAbysinian ,livingPlaceofCatBobtall ,livingPlaceofCatBeliness = read_data("gremlins.txt")    # read in data
    
    Abysinian_moves  = [-3,-2,-1,0,1,2,3]
    Bobtall_moves  = [-2,-1,0,1,2]
    attackedBobtall_moves  = [0]
    Beliness_moves  = [-1,0,1]
    farofAbysin   = 0
    farofBobtall   = 0
    farofBeliness   = 0
    # Starting population
    printpart()
    initpop = input("Enter initpop value ( normally it should be 1 ) : ")
    rangeval = input("Enter range value ( normally it is about  30 ) : ")
    initpop = int(initpop)
    rangeval = int(rangeval)
    for i in range(initpop):  # add good gremlins to grid
        xposision = livingPlaceofCatBeliness[0][0]
        yposision = livingPlaceofCatBeliness[0][1]  

        minxpos =  xposision -2
        if minxpos < 0 :
            minxpos = 0
        maxxpos =  xposision +2
        if maxxpos > MAXROW - 1  :
            maxxpos = MAXROW - 1
        minypos =  yposision -2
        if minypos < 0 :
            minypos = 0       
        maxypos =  yposision +2
        if maxypos > MAXCOL - 1  :
            maxypos = MAXCOL - 1        
      
        Abysinianarray[random.randint(0,MAXROW-1),random.randint(0,MAXCOL-1)] += 1
        Bobtallarray[random.randint(0,MAXROW-1),random.randint(0,MAXCOL-1)] += 1 
        attackedbobtailarray[random.randint(0,MAXROW-1),random.randint(0,MAXCOL-1)] += 0
        Belinessarray[random.randint(minxpos ,maxxpos),random.randint(minypos,maxypos)] += 1

    # Simulation

    for t in range(rangeval):    # @ 8 hour / timestep = 10 days
        print("        ")
        print("### Timestep  ", t, "###")
        print("### Abysinian walked for ", farofAbysin, "m")
        print("### bob tall walked for ", farofBobtall, "m")
        print("### Beliness javanese walked for ", farofBeliness, "m")
  
        Abysinianarraynext , farofAbysin = move_em(Abysinianarray, Abysinian_moves , farofAbysin)
        Bobtallarraynext , farofBobtall = move_em(Bobtallarray, Bobtall_moves , farofBobtall)
        if t%2 == 0:       # after midnight till 8am        
            Belinessarraynext , farofBeliness = move_em(Belinessarray, Beliness_moves , farofBeliness)
        
  
        await asyncio.gather(rule1(Abysinianarraynext, food))
        await asyncio.gather(waterdrinkrule(Abysinianarraynext, water))
        await asyncio.gather(rule1Bobtall(Bobtallarraynext, food))
        await asyncio.gather(waterdrinkruleBobtall(Bobtallarraynext, water))
        await asyncio.gather(abaysiankillsbobtail(Abysinianarraynext , Bobtallarraynext , attackedbobtailarray))
        await asyncio.gather(rule1Beliness(Belinessarraynext, food))
        await asyncio.gather(waterdrinkruleBeliness(Belinessarraynext, water))

        Abysinianarray = Abysinianarraynext
        Bobtallarray = Bobtallarraynext
        Belinessarray = Belinessarraynext

        make_gremlin_scatter(Abysinianarray, "red")
        make_gremlin_scatter(Bobtallarray, cat2color )        
        make_gremlin_scatter(Belinessarray, cat3color )
        make_gremlin_scatter(attackedbobtailarray , "black" )
        make_feature_scatter(water, "blue")
        make_feature_scatter(food, "g")
        make_feature_scatter(livingPlaceofCatAbysinian, "red")
        make_feature_scatter(livingPlaceofCatBobtall,  cat2color )
        make_feature_scatter(livingPlaceofCatBeliness, cat3color)
        
        plt.title("Gremlin Simulation (time = " + str(t) + ")")
        plt.xlabel("Columns")
        plt.ylabel("Rows")
        plt.xlim(-1,MAXCOL)
        plt.ylim(-1,MAXROW)
        plt.pause(1)
        plt.clf()
    
if __name__ == "__main__":
    asyncio.run(main())
