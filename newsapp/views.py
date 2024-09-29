from django.shortcuts import render
from pathlib import Path
import requests
import environ

env = environ.Env()
env.read_env(".env")

MEDIA_API_KEY = env.get_value("MEDIA_API_KEY", str)


def get_news(category):
    r = requests.get(
        f"http://api.mediastack.com/v1/news?access_key={MEDIA_API_KEY}&categories={category}"
    )
    res = r.json()
    data = res["data"]
    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i["title"])
        description.append(i["description"])
        image.append(i["image"])
        url.append(i["url"])
    news = zip(title, description, image, url)
    return news


def index(request):
    news = get_news("general")
    return render(request, "newsapp/index.html", {"news": news})


# Create your views here.
def sports(request):
    news = get_news("sports")
    return render(request, "newsapp/sports.html", {"news": news})


def science(request):
    news = get_news("science")
    return render(request, "newsapp/science.html", {"news": news})
