import requests
import json
from body.greet import speak


def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e8340605590b498fba55816e19d5e6d4",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=e8340605590b498fba55816e19d5e6d4",
            "health" : "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=e8340605590b498fba55816e19d5e6d4",
            "science" :"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=e8340605590b498fba55816e19d5e6d4",
            "sports" :"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=e8340605590b498fba55816e19d5e6d4",
            "technology" :"ttps://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=e8340605590b498fba55816e19d5e6d4"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop] : ")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

