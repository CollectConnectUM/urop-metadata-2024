'''''''''''''''''''''
    main file
'''''''''''''''''''''
import IPython
from IPython.display import display
import pandas as pd

'''''''''''''''''''''
Class Declaration
'''''''''''''''''''''
#author
#title
#publication date
#time it was uploaded (?)
#bool duplicate - true if there exists multiple works - false otherwise
#output: file with good metadata + statement of how many faulty works

#Roles:
#Parsing: MJ
#Comparing/Bucketing: Yatin
#Output/AI: Ivan & Mason

from dataclasses import dataclass


#example datastructure
@dataclass
class Work:
    author: str
    title: str
    publication: str
    isDuplicate: bool
p = Work(1.5, 2.5)

print(p)  # Point(x=1.5, y=2.5, z=0.0)


#AI

#parse data
with open('hathi_full_20240301.txt') as f:
    lines = f.readlines() # list containing lines of file
    #for line in lines:
        #bucketing
    
#save relevant fields into class
#save classes into list
'''
use pandas somehow lol (store author, title, and place of publication into 3 lists)
create a data structure to store class objects(author, title, publication, isDup)
1) create object
2) append to list
use a list.append()
'''


'''
======OUTPUT======

def output(takes in list from bucketing){
    for work in list:
        call to UMGPT AI() //not sure how this works but call AI with some prompt 
        and accuracy tester (wiki/loc/other verifier we mentioned)
        if work is deemed accurate, (author/title/publication date 
        -> push current work in list to output.txt
        
}

strictly for testing purposes, we want to make sure that the outout file does not contain any duplicates
bool isDuplicate(work1, work2){
    if work1.author == work2.author:
        return false
    if work1.title == work2.title:
        return false;
    if work1.publication == work2.publication:
        return false;
    return true;
}
'''

def main():
    print("hello")
    #parse
    #bucket
    #output

if __name__ == "__main__":
    main()