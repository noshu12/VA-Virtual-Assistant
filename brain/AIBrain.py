 #API key
fileopen = open("database\\api.txt",'r')
API = fileopen.read()
fileopen.close()

import openai #pip isntall openai
from dotenv import load_dotenv
# from httpx import ASGITransport

#Coding

openai.api_key = API
load_dotenv()
# completion = openai.completions()

def Replybrain(question,chat_log = None):
    FileLog = open("database\\chat_log.txt",'r')
    chat_log_template = FileLog.read()
    FileLog.close() 
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nFarady : '
    response = openai.completions.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_tempelate_update = chat_log_template + f"\nYou: {question} \nFarady : {answer}"
    FileLog = open("database\\chat_log.txt",'w')
    FileLog.write(chat_log_tempelate_update)
    FileLog.close
    return answer

# while True:
#     kk = input("Enter : ")
#     print(f"Farady : {Replybrain(kk)}")
