from matplotlib import pyplot as plt
import numpy as np
import random
"""
Mustafa Kağan Yalım
270201090
"""
#I created custom function for each question.
#Experiment 1: 2 values are sampled independently from a standard uniform distribution and summed.
def q1():
    #Function that adds two numbers standart uniform and returns the results to the list.
    listOfq1=[]
    for i in range(200000):
        num1=np.random.uniform()
        num2=np.random.uniform()
        listOfq1.append(num1+num2)
    #Normal distribution's coding.
    # Other functions a liitle bir different but basically I applied the same algorithm.    
    std=np.std(listOfq1)
    mean=np.mean(listOfq1)
    listForNd=listOfq1
    listForNd.sort()
    theoric=np.arange(listForNd[0],listForNd[-1],0.001)
    y_axis = ((1/(np.sqrt(2 * np.pi)*std))*np.exp(-0.5*(1/std*(theoric-mean))**2))

    
    plt.plot(theoric,y_axis,color="#000080",label="Normal Distribution")

    
    
    plt.hist(listOfq1,bins=100,color='#E8421F',label='Histogram',density= True)
    plt.legend()
    plt.title("Experiment 1 ")
    plt.xlabel("Sum of Variables")
    plt.ylabel("Probabilities")
    plt.show()



#Experiment 2: 4 values are sampled independently from a standard uniform distribution and summed.
def q2():
    #The only difference from the 1st question is that we choose 4 numbers instead of 2 numbers.
    listOfq2=[]
    for i in range(200000):
        num1=np.random.uniform()
        num2=np.random.uniform()
        num3=np.random.uniform()
        num4=np.random.uniform()
        listOfq2.append(num1+num2+num3+num4)
    #Normal distribution's coding.
    std=np.std(listOfq2)
    mean=np.mean(listOfq2)
    listForNd=listOfq2
    listForNd.sort()
    theoric=np.arange(listForNd[0],listForNd[-1],0.001)
    y_axis = ((1/(np.sqrt(2 * np.pi)*std))*np.exp(-0.5*(1/std*(theoric-mean))**2))

    
    plt.plot(theoric,y_axis,color="#000080",label="Normal Distribution")
    
    plt.hist(listOfq2,bins=100,color='#E8421F',label='Histogram',density=True)
    plt.legend()
    plt.title("Experiment 2 ")
    plt.xlabel("Sum of Variables")
    plt.ylabel("Probabilities")
    plt.show()
#Experiment 3: 50 values are sampled independently from a standard uniform distribution and summed
def q3():
    #The only difference from the 2nd question is that we choose 50 numbers instead of 2 numbers.

    listOfq3=[]
    
    for i in range(200000):
        temp_list=[]
        for i in range(50):
            
            temp_list.append(np.random.uniform())
        listOfq3.append(sum(temp_list))
    #Normal distribution's coding.
    std=np.std(listOfq3)
    mean=np.mean(listOfq3)
    listForNd=listOfq3
    listForNd.sort()
    theoric=np.arange(listForNd[0],listForNd[-1],0.001)
    y_axis = ((1/(np.sqrt(2 * np.pi)*std))*np.exp(-0.5*(1/std*(theoric-mean))**2))

    
    plt.plot(theoric,y_axis,color="#000080",label="Normal Distribution")

    
    plt.hist(listOfq3,bins=100,color='#E8421F',label='Histogram',density=True)
    plt.legend()
    plt.xlabel("Sum of Variables")
    plt.ylabel("Probabilities")
    plt.title("Experiment 3 ")
    plt.show()


"""
Experiment 4: 50 values are sampled dependently from a uniform distribution and summed.
Dependence is introduced by the following rule: If a value is smaller than 99, the next value is sampled
from a uniform distribution between 0 and 200, otherwise between 99 and 101.
"""
def q4():
    listOfq4=[]
    
    for i in range(200000):
        temp_list=[]
        #I randomly selected the first element of the list
        
        num1=np.random.uniform(0,200)
        temp_list.append(num1)
        #I have 49 elements left to choose so I use range(49) instead range(50)
        for j in range(49):
            #If-Else conditions that determine the range of the next element from each element
            #If current element less than 99,the next element's value between 0 and 200
            if temp_list[-1]<99:
                nextmum=np.random.uniform(0,200)
            #If current element bigger than 99 or equal 99,the next element's value between 98 and 102
            elif temp_list[-1]>=99:
                nextmum=np.random.uniform(98,102)
            temp_list.append(nextmum)
        
        listOfq4.append(sum(temp_list))
    #Normal distribution's coding.
    std=np.std(listOfq4)
    mean=np.mean(listOfq4)
    listForNd=listOfq4
    listForNd.sort()
    theoric=np.arange(listForNd[0],listForNd[-1],0.001)
    y_axis = ((1/(np.sqrt(2 * np.pi)*std))*np.exp(-0.5*(1/std*(theoric-mean))**2))

    
    plt.plot(theoric,y_axis,color="#000080",label="Normal Distribution")
    plt.hist(listOfq4,bins=100,color='#E8421F',label='Histogram',density=True)
    plt.legend()
    plt.xlabel("Sum of Variables")
    plt.ylabel("Probabilities")
    plt.title("Experiment 4 ")
    plt.show()
    


"""
Experiment 5: 50 values are sampled independently from different uniform distributions and summed.
For each value generation, the uniform distribution parameters (a and b-a) should be sampled from a
standard uniform distribution.
"""
def q5():
    #Exactly the same algorithm as the 3rd question.
    
    listOfq5=[]
    for i in range(200000):
        temp_list=[]
        for i in range(50):
            a=np.random.uniform()
            b=np.random.uniform()
            temp_list.append(np.random.uniform(a,b-a))
        listOfq5.append(sum(temp_list))
    #Normal distribution's coding.
    std=np.std(listOfq5)
    mean=np.mean(listOfq5)
    listForNd=listOfq5
    listForNd.sort()
    theoric=np.arange(listForNd[0],listForNd[-1],0.001)
    y_axis = ((1/(np.sqrt(2 * np.pi)*std))*np.exp(-0.5*(1/std*(theoric-mean))**2))

    
    plt.plot(theoric,y_axis,color="#000080",label="Normal Distribution")

    
    plt.hist(listOfq5,bins=100,color='#E8421F',label='Histogram',density=True)
    plt.legend()
    plt.xlabel("Sum of Variables")
    plt.ylabel("Probabilities")
    plt.title("Experiment 5 ")
    plt.show()

key=True
while key:
    #User Interface for launch the functions.
    q_no=input("Welcome! Which function's graph do you want to choose? Write between 1 and 5 (0 for quit) :\n")
    if q_no=="0":
        print("Goodbye.")
        key=False
    elif q_no=="1":
        q1()
    elif q_no=="2":
        q2()
    elif q_no=="3":
        q3()
    elif q_no=="4":
        q4()
    elif q_no=="5":
        q5()
    else:
        print("Invalid entry.")
