from django.shortcuts import render
from pathlib import Path
import requests
import environ

env = environ.Env()
env.read_env(".env")

MEDIA_API_KEY = env.get_value("MEDIA_API_KEY", str)


# Create your views here.
def index(request):
    r = requests.get(
        f"http://api.mediastack.com/v1/news?access_key={MEDIA_API_KEY}&categories=sports"
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
    return render(request, "newsapp/index.html", {"news": news})
