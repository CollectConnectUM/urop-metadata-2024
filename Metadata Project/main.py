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

  
def parse(file):
    #TODO: (DONE) add user input for file name
    
    i = 0
   
    f = open('newFile.txt', 'w')
    with open(file) as input:
        lines = input.readlines() # list containing lines of file
        for line in lines:
            elem = line.split('\t',25) #array of all information until next work
            
            #nested loop for rest of elements
            work = Work(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6], 
                        elem[7], elem[8], elem[9], elem[10], elem[11], elem[12], elem[13],
                        elem[14], elem[15], elem[16], elem[17], elem[18],elem[19],elem[20], 
                        elem[21],elem[22],elem[23],elem[24],elem[25], False, i) #replace False with isDupe() func
            works_list.append(work)
            work.isDuplicate = i
            i+=1
            
    f.close()

def isDuplicate(work1, work2):
    if work1.author == work2.author and work1.title == work2.title:
        return True
    return False

def isDupe(work1, work2):
    #Comparing the Title, Author name, and place of publication
    #0.95 means 95% similar
    if (fuzz.ratio(work1.author, work2.author) > 90 and 
        fuzz.ratio(work1.title, work2.title) > 90):
        return True
    else: 
        return False

#TODO: print in original metadata form (not just author/title)
def printUniqueList(list, num_unique, total_num_of_works):
    f = open("Unique_gpt.txt", "w")
    f.write("From " + str(total_num_of_works) + " to " + str(num_unique) + ' works.\n')
    list.sort(key=lambda x: (x.index))
    for n in list:
        f.write(n.print_work())

#BY TITLE
def removeDupe(list, unique):

    list.sort(key=lambda x: (x.author, x.title))  # Sort the list based on author and title
    
    # Iterate through the sorted list and compare adjacent works
    num = 0
    for i in range(0, len(list)):
        # print(num)
        num+=1
        if not isDupe(list[i], list[i - 1]):
            unique.append(list[i])

    num_unique = len(unique)
    total_num_of_works = len(works_list)
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
    

if __name__ == "__main__":
    main()

