 #API key
fileopen = open("database\\api.txt",'r')
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv

#Coding

openai.api_key = API
load_dotenv()
#completion = openai.completions()
def QnA(question,chat_log = None):
    FileLog = open("database\\qna_chatlog.txt",'r')
    chat_log_template = FileLog.read()
    FileLog.close() 
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You Question : {question}\nFarady Answer : '
    response = openai.completions.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    chat_log_tempelate_update = chat_log_template + f"\nYour Question: {question} \nFarady Answer : {answer}"
    FileLog = open("database\\qna_chatlog.txt",'w')
    FileLog.write(chat_log_tempelate_update)
    FileLog.close
    return answer

# while True:
#     kk = input("Enter Your Question : ")
#     print(f"Faraday Answer: {QnA(kk)}")
