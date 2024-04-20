'''''''''''''''''''''
    main file
'''''''''''''''''''''
import IPython
from IPython.display import display
import pandas as pd
from fuzzywuzzy import fuzz 
import openai

client = openai.OpenAI(api_key="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")

def formatting(response):
    response = response[161:]
    for index, char in enumerate(response):
        if response[index:index + 4] == "role":
            response = response[:index - 3]
            break
    return response

def AIGeneration(chat_prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": chat_prompt}]
    )
    response = str(response)
    return response

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
works_list_hindi = []
unique_works = []
# total_num_of_works = 0

#FIXED: Input & Total_num_works
class Work:
    def __init__(self, htid, access, rights, ht_bib_key, description, source,
                 source_bib_num, oclc_num, isbn, issn, lccn, title, imprint,
                 rights_reason_code, rights_timestamp, us_gov_doc_flag,
                 rights_date_used, pub_place, lang, bib_fmt, collection_code,
                 content_provider_code, responsible_entity_code,
                 digitization_agent_code, access_profile_code, author, isDuplicate, index):
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
        self.index = index

    #print(p)  # Point(x=1.5, y=2.5, z=0.0)
    def print_work(self) -> str:
        all = str(self.htid + '\t' +
        self.access + '\t' +
        self.rights + '\t' +
        self.ht_bib_key + '\t' +
        self.description + '\t' +
        self.source + '\t' +
        self.source_bib_num + '\t' +
        self.oclc_num + '\t' +
        self.isbn + '\t' +
        self.issn + '\t' +
        self.lccn + '\t' +
        self.title + '\t' +
        self.imprint + '\t' +
        self.rights_reason_code + '\t' +
        self.rights_timestamp + '\t' +
        self.us_gov_doc_flag + '\t' +
        self.rights_date_used + '\t' +
        self.pub_place + '\t' +
        self.lang + '\t' +
        self.bib_fmt + '\t' +
        self.collection_code + '\t' +
        self.content_provider_code + '\t' +
        self.responsible_entity_code + '\t' +
        self.digitization_agent_code + '\t' +
        self.access_profile_code + '\t' +
        self.author)
        return all
    #AI

    #parse data
            #'sample_1.txt'
    #author 25
    #title 11
    #pub place 17
    # lang 18
# my_file = input("Enter file name: ") 
#  open(my_file, "r") 
def parse(file):
    #TODO: (DONE) add user input for file name
    # total_num_of_works = 0
    i = 0
    # file = input('What is the metadata file you wish to clean?\n')
    #print("Username is: " + file)
    f = open('newFile.txt', 'w')
    with open(file) as input:
        lines = input.readlines() # list containing lines of file
        for line in lines:
            elem = line.split('\t',25) #array of all information until next work
            #print(elem[17])
            #print(line)
            #nested loop for rest of elements
            work = Work(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], 
                        elem[7], elem[8], elem[9], elem[10], elem[11], elem[12], elem[13],
                        elem[14], elem[15], elem[16], elem[17], elem[18],elem[19],elem[20], 
                        elem[21],elem[22],elem[23],elem[24],elem[25], False, i) #replace False with isDupe() func
            works_list.append(work)
            work.isDuplicate = i
            i+=1
            #print(total_num_of_works)
            #total_num_of_works += 1
            # if (work.lang == 'hin'):
            #     f.write(str(line)) #to test if it actually writes
            #     works_list_hindi.append(work) #list of hindi works
            # # print(i)
            # i = i + 1
            #bucketing
            #line.split('\t') is used for splitting by tabs
    # print(len(works_list_hindi))
    # total_num_of_works = len(works_list)
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
    if (fuzz.ratio(work1.author, work2.author) > 90 and 
        fuzz.ratio(work1.title, work2.title) > 90):
        #fuzz.ratio(work1.rights_timestamp, work2.rights_timestamp) > 0.50
        return True
    else: 
        return False

#TODO: print in original metadata form (not just author/title)
def printUniqueList(list, num_unique, total_num_of_works):
    f = open("Unique_gpt.txt", "w")
    #total_num_works is not working correctly
    #print(total_num_of_works)
    #list.sort(key=lambda x: (x.isDuplicate)) #sort based on index in original list
    f.write("From " + str(total_num_of_works) + " to " + str(num_unique) + ' works.\n')
    list.sort(key=lambda x: (x.index))
    for n in list:
        # print(list[n].htid)
        #in progress
        f.write(n.print_work())
    # for n in range(len(list)):
        #f.write(list[n].author + '\t' + list[n].title + '\n')

#BY TITLE
def removeDupe(list, unique):
    #unique.append(list[0])  # The first element is guaranteed to be unique
    list.sort(key=lambda x: (x.author, x.title))  # Sort the list based on author and title
    
    # Iterate through the sorted list and compare adjacent works
    num = 0
    for i in range(0, len(list)):
        # print(num)
        num+=1
        if not isDupe(list[i], list[i - 1]):
            unique.append(list[i])
        #print(unique[i])
    num_unique = len(unique)
    #print(num_unique)
    total_num_of_works = len(works_list)
    #print(total_num_of_works)
    printUniqueList(unique, num_unique, total_num_of_works)

#BY AUTHOR

chat_prompt = """I have the author and a list of works by the author. There may be identical
                 works with diferent names, signify any identical works with parenthesis and a number 
                 inside. For example, if two works are the same, put a (1) at the end of all identical works. I.e: "Robinson Crusoe (1)" and
                 "The Life and Strange Surprizing Adventures of Robinson Crusoe, of York, Mariner(1)", Output
                 in the same format as the input but with indicators of identical works added to it.
                 Here is the author and the list of their works: """

def remove_duplicates2(works):
    f = open("parse-test.txt", "w")
    unique_works = {}
    for work in works:
        author, title = work.split(":")
        author = author.strip()
        title = title.strip()
        
        if author not in unique_works:
            unique_works[author] = {title}
        else:
            unique_works[author].add(title)
    for author, titles in unique_works.items():
        f.write(f"{author}: {titles}\n") 
        output = formatting(AIGeneration(chat_prompt + str(author) + ", " + str(titles)))
        print(output)
    return 


def main():
    my_file = input("Enter file name: ") 
    parse(my_file)
    removeDupe(works_list, unique_works)
    # testingworks = [
    # "J.K. Rowling: Harry Potter and the Philosopher's Stone",
    # "J.K. Rowling: Harry Potter and the Sorcerer's Stone",
    # "J.K. Rowling: Harry Potter and the Chamber of Secrets",
    # "J.R.R. Tolkien: The Hobbit",
    # "J.R.R. Tolkien: The Lord of the Rings",
    # "Mark Twain: The Adventures of Tom Sawyer",
    # "Mark Twain: The Adventures of Huckleberry Finn",
    # "Mark Twain: The Adventures of Huckleberry Finn",
    # "Mark Twain: The Adventures of Huckleberry Finn",
    # "Mark Twain: The Adventures of Huckleberry Finn",
    # "Mark Twain: The Adventures of Huckleberry Finn",
    # "Daniel Defoe: Robinson Crusoe",
    # "Daniel Defoe: The Life and Strange Surprizing Adventures of Robinson Crusoe, of York, Mariner",
    # ]
    # remove_duplicates2(testingworks)
    
    #TODO: (DONE) add output saying how many duplicates/works left
    #parse
    #bucket
    #output

if __name__ == "__main__":
    main()





# def removeDupe(list, unique): #list is a list of all works (duplicates included), list2 is an empty list of unique works
#     unique.append(list[0]) #the first is guaranteed to be unique
#     f = open("print_statements.txt", "w")
#     num_unique = 0
#     # f.write("1" + '\n')
#     # for n in range(len(list)):  #where c = n + 1
#     #     f.write("2" + '\n')
#     #     for c in range(len(list)):
#     #         f.write("3" + '\n')
#     #         if (n == c or c < n): # c <= n
#     #             f.write("4" + '\n')
#     #             continue
#     #         if (isDuplicate(list[n], list[c])):
#     #             f.write("5" + '\n')
#     #             continue
#     #         elif (not isDuplicate(list[n], list[n - 1]) and n != 0):
#     #             f.write("6" + '\n')
#     #             unique.append(list[n])
        

# def removeDupe(list, unique):
#     #unique.append(list[0])  # The first element is guaranteed to be unique
#     num = 0 #for testing
#     num_unique = 0
#     for item in list:
#         is_duplicate = False
#         print(num)
#         num+=1
#         for unique_item in unique:
#             if isDupe(item, unique_item):
#                 is_duplicate = True
#                 break
#         if not is_duplicate:
#             unique.append(item)
#             num_unique += 1
    
#     printUniqueList(unique, num_unique)
#     return


