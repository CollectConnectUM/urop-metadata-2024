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
#pip install PyPDF2 sentence-transformers faiss-cpu
from langchain.schema import (
    HumanMessage,
    SystemMessage
)


client = openai.OpenAI(api_key="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")

#import requests
load_dotenv()

##replaced openai with client. perhaps try this 
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

article_txt=open("article1.txt","r")
article_str = article_txt.read() # string of the entire file
#paragraphs = article_str.split('\n\n') #list each paragraph is an element
#embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

loader = TextLoader(file_path="article1.txt")
documents = loader.load()


texts = article_str.strip().split('\n')
texts = [paragraph for paragraph in texts if paragraph]

print()
print()
print()
print(type(texts))
print(len(texts))

# Split and embed the text in the documents
##text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
##texts = text_splitter.split_documents(documents)

final_prompt = """I have compiled a string of analyses from each paragraph in an 
                article, where each analysis addresses the tone and potential bias 
                of each paragraph. Summarize this analysis. Make sure to highlight 
                potentially important information and potential patterns.
                Do not use any other information other than this article: """

text_response = ""


# prompt for LLM
for i in texts:
    prompt = """I have provided a paragraph from a recent article I read. Please
                analyze the tone of the paragraph and identify any indications of 
                bias. By 'tone bias,' I mean any subtle cues in the language that 
                suggest the author's personal feelings or leanings towards the subject 
                matter, which could influence the reader's perception in a non-neutral 
                way. Consider word choice, sentence construction, and any emotionally
                charged language or phrasing when giving your analysis. Here is the 
                paragraph. Make the analysis brief. Do not use any other information other than this article:
                """ + str(i)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    response = str(response)
    response = response[161: len(str(response)) - 254]
    text_response += response + "\n \n \n"
    print(response)
    response = ""

#summary
ending_response = client.chat.completions.create(
      model="gpt-3.5-turbo",
     messages=[{"role": "user", "content": final_prompt+response}]
   )
ending_response = str(ending_response)
ending_response = ending_response[161: len(str(ending_response)) - 254]
print(ending_response)
