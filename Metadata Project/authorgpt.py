from langchain_community.chat_models import ChatOpenAI
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
#pip install langchain_openai
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv
import os
import openai
import numpy as np
from langchain_openai import ChatOpenAI
#pip install PyPDF2 sentence-transformers faiss-cpu
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
from main import *

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

client = openai.OpenAI(api_key="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")

#import requests
load_dotenv()

##replaced openai with client. perhaps try this 
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

article_txt=open("test_authorless_works.txt","r")
article_str = article_txt.read()

loader = TextLoader(file_path="test_authorless_works.txt")
documents = loader.load()


texts = article_str.strip().split('\n') #this might have half the elements as a '\n' character
texts = [paragraph for paragraph in texts if paragraph]

# final_prompt = """I have compiled a string of analyses from a series of paragraphs in an 
#                 article, where each analysis addresses the tone and potential bias 
#                 of each paragraph. Summarize this analysis. Make sure to highlight 
#                 potentially important information and potential patterns.
#                 Do not use any other information other than this article: 
#                 1. """

author_prompt = """Given only the title of a metadata field, please find the author who wrote it, output only the 
                name of the author. Otherwise output "I can't find the author."
                """

author_list = []

f = open('authorless_output.txt', 'w')
for i in texts:
    chat_prompt = str(i) + author_prompt
    response = str(AIGeneration(chat_prompt))
    response = formatting(response)
    author_list.append(response)

iterator = 0
refined_author_list = []
for i in author_list:
    response = "test"
    chat_prompt = texts[iterator] + author_prompt
    if (i == "I can't find the author."):
        response = str(AIGeneration(chat_prompt))
        response = formatting(response)
        #PRINT NEW RESPONSE
        print(response + "\n")
        f.write(response + '\n')
    else:
        response = i
        print(response + "\n")
        f.write(response + '\n')
    iterator += 1

    response = formatting(response)

    matching_obj = None
    if(response != "I can't find the author."):
        for obj in unique_works:
            if obj[11] == i:
                matching_obj = obj
                break
        if(matching_obj != None):
            index = unique_works.index(matching_obj)
            unique_works[index].author = response + " AI generated"
            #printing AI generated author field
            print(unique_works[index].author + " \n")
    refined_author_list.append(response)
    #print(refined_author_list)
    
    #f.write(response + '\n')
