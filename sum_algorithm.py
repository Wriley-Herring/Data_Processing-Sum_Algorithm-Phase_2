'''
Created on Jun 13, 2020

@author: wrileyherring
'''

# heap sort functions

#create heap function
def heap(array,n,i):
        
    #set root and child variables 
    largest = i
    left = 2 * i + 1
    right = 2 * i +2
    
    # check if left child is larger than root
    if left < n and array[i] < array[left]:
        largest = left
    
    # check if right child is larger than root
    if right < n and array[largest] < array[right]:
        largest = right
    
    # swap child and root if neccessary   
    if largest != i:
            
        array[i],array[largest] = array[largest],array[i]
        
        #continue build with root
        heap(array, n, largest)

#define heap sort function
def heapSort(array):
    
    #set length of array
    n = len(array)
    
    #create maxheap
    for i in range(n//2 -1, -1, -1):
        heap(array,n,i)
    
    #pull elements one at a time   
    for i in range(n-1,0,-1):
        array[i],array[0] = array[0], array[i]
        heap(array,i,0)





#Declare number of input files
fileNums = ['1','2','3','4','5']


#Perform the Sum of K algorithm on all files
for num in fileNums:
    
    #Declare Input and Output Files
    filenameIn = 'in'+num+'.txt'
    filenameOut = 'out'+num+'.txt'
    
    #Read input file into algorithm
    f = open(filenameIn,'r')
    lines = f.readlines()
    target = int(lines[1])
    outputList = lines[2]
    listOfNumbers = lines[2].split(" ")
    listOfNumbers.pop()
    sortList = list(map(int,listOfNumbers))
    
    #Sort list of numbers
    
    heapSort(sortList)

    #declare answer variables
    answer1 = 0
    answer2 = 0
    
    #iterate through list to see if sum values exist
    
    #set parameters
    Valid = True
    i=0
    j=len(sortList)-1
    
    
    while Valid:
        
        #check if current values sum equals target and set to answer variables
        if sortList[i]+sortList[j] == target:
            answer1 = str(sortList[i])
            answer2 = str(sortList[j])
            Valid = False
            
        #if current values sum is larger than target move j pointer to the left     
        if sortList[i] + sortList[j] > target:
            j -= 1
            
        #if current values sum is smaller than target move i pointer to the right
        if sortList[i] + sortList[j] < target:
            i += 1
            
        #if  j pointer has passed i pointer there is no solution    
        if i > j:
            Valid = False
            
    #check if the algorithm found an answer
    
    sortList = " ".join(str(x)for x in sortList)
    #If it did not then write a no response to the output file   
    if answer1 == 0 and answer2 ==0:
        outputFile = open(filenameOut,"w+")
        outputFile.write(str(target))
        outputFile.write('\n')
        outputFile.write(outputList)
        outputFile.write(sortList)
        outputFile.write('\n')
        outputFile.write('No')
        
    #if it did find an answer then write a yes response to the output file
    else:
        outputFile = open(filenameOut,"w+")
        outputFile.write(str(target))
        outputFile.write('\n')
        outputFile.write(outputList)
        outputFile.write(sortList)
        outputFile.write('\n')
        outputFile.write('Yes')
        outputFile.write('\n')
        outputFile.write(answer1+'+'+answer2+'='+str(target))