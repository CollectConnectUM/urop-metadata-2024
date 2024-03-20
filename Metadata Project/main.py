'''''''''''''''''''''
    main file
'''''''''''''''''''''
import IPython
from IPython.display import display
import pandas as pd
from fuzzywuzzy import fuzz 

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

#will be using a list [vector] of classes 

#example datastructure

#@dataclass
works_list = []
works_list_japanese = []
unique_works = []
class Work:
    def __init__(self, htid, access, rights, ht_bib_key, description, source,
                 source_bib_num, oclc_num, isbn, issn, lccn, title, imprint,
                 rights_reason_code, rights_timestamp, us_gov_doc_flag,
                 rights_date_used, pub_place, lang, bib_fmt, collection_code,
                 content_provider_code, responsible_entity_code,
                 digitization_agent_code, access_profile_code, author, isDuplicate):
        self.htid = htid
        self.access = access
        self.rights = rights
        self.ht_bib_key = ht_bib_key
        self.description = description
        self.source = source
        self.source_bib_num = source_bib_num
        self.oclc_num = oclc_num
        self.isbn = isbn
        self.issn = issn
        self.lccn = lccn
        self.title = title
        self.imprint = imprint
        self.rights_reason_code = rights_reason_code
        self.rights_timestamp = rights_timestamp
        self.us_gov_doc_flag = us_gov_doc_flag
        self.rights_date_used = rights_date_used
        self.pub_place = pub_place
        self.lang = lang
        self.bib_fmt = bib_fmt
        self.collection_code = collection_code
        self.content_provider_code = content_provider_code
        self.responsible_entity_code = responsible_entity_code
        self.digitization_agent_code = digitization_agent_code
        self.access_profile_code = access_profile_code
        self.author = author

        self.isDuplicate = isDuplicate

    #print(p)  # Point(x=1.5, y=2.5, z=0.0)

    #AI

    #parse data
            #'sample_1.txt'
    #author 25
    #title 11
    #pub place 17
    # lang 18
def parse():
    f = open('japanese.txt', 'w')
    with open('128MB.txt') as input:
        lines = input.readlines() # list containing lines of file
        for line in lines:
            elem = line.split('\t',25) #array of all information until next work
            #print(elem[17])
            #print(line)
            #nested loop for rest of elements
            work = Work(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], 
                        elem[7], elem[8], elem[9], elem[10], elem[11], elem[12], elem[13],
                        elem[14], elem[15], elem[16], elem[17], elem[18],elem[19],elem[20], 
                        elem[21],elem[22],elem[23],elem[24],elem[25], False) #replace False with isDupe() func
            works_list.append(work)
            if (work.lang == 'jpn'):
                f.write(str(line)) #to test if it actually writes
                works_list_japanese.append(work) #list of japanese works
            # print(i)
            # i = i + 1
            #bucketing
            #line.split('\t') is used for splitting by tabs
    f.close()
    
    
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
            -  create our own dataset of works to compare with
            - give to AI to check
        if work is deemed accurate, (author/title/publication date 
        -> push current work in list to output.txt
        if work is not deemed accurate{
        
        }

        
}

strictly for testing purposes, we want to make sure that the outout file does not contain any duplicates
bool isDuplicate(work1, work2){
    if work1.author == work2.author:
        return false
    if work1.title == work2.title:
        return false;
    return true;
}

def isDupe(work1, work2):
    #Comparing the Title, Author name, and place of publication
    #0.95 means 95% similar
    if (fuzz.ratio(work1.author, work2.author) > 0.95 and 
        fuzz.ratio(work1.title, work2.title) > 0.95 and 
        fuzz.ratio(work1.publication, work2.publication) > 0.95):
        return True
    else: 
        return False
#import fuzzywuzzy will also work as it uses the Levesthein Distance algorithm
#Levesthein distance works if the works are in the same language (as long as both are romanized, it should work)
    #should note that the percentage that is the same will change if the language is romanized
'''

def isDuplicate(work1, work2):
    if work1.author == work2.author and work1.title == work2.title:
        return True
    return False

def isDupe(work1, work2):
    #Comparing the Title, Author name, and place of publication
    #0.95 means 95% similar
    if (fuzz.ratio(work1.author, work2.author) > 0.95 and 
        fuzz.ratio(work1.title, work2.title) > 0.95):
        #fuzz.ratio(work1.rights_timestamp, work2.rights_timestamp) > 0.50
        return True
    else: 
        return False

def printUniqueList(list):
    f = open("Unique_works.txt", "w")
    for n in range(len(list)):
        f.write(list[n].author + '\t' + list[n].title + '\n')

def removeDupe(list, list2): #list is a list of all works (duplicates included), list2 is an empty list of unique works
    list2.append(list[0]) #the first is guaranteed to be unique
    f = open("print_statements.txt", "w")
    f.write("1" + '\n')
    for n in range(len(list)):  #where c = n + 1
        f.write("2" + '\n')
        for c in range(len(list)):
            f.write("3" + '\n')
            if (n == c or c < n): # c <= n
                f.write("4" + '\n')
                continue
            if (isDuplicate(list[n], list[c])):
                f.write("5" + '\n')
                continue
            elif (not isDuplicate(list[n], list[n - 1]) and n != 0):
                f.write("6" + '\n')
                list2.append(list[n])

    printUniqueList(list2)
    #print("7")            
    #print(list2[0].author)

            
def main():
    parse()
    removeDupe(works_list_japanese, unique_works)

    #parse
    #bucket
    #output

if __name__ == "__main__":
    main()
