from django.shortcuts import render
from pathlib import Path
import requests
import environ

env = environ.Env()
env.read_env(".env")

MEDIA_API_KEY = env.get_value("MEDIA_API_KEY", str)


def get_news(category=None, country=None):
    if not category and not country:
        raise ValueError("カテゴリーまたは国名のどちらかを指定してください。")

    params = {"access_key": MEDIA_API_KEY, "limit": 9}
    if category:
        params["categories"] = category
    if country:
        params["countries"] = country

    r = requests.get("http://api.mediastack.com/v1/news", params=params)
    res = r.json()
    data = res.get("data", [])

    title = []
    description = []
    image = []
    url = []
    for i in data:
        title.append(i.get("title", ""))
        description.append(i.get("description", ""))
        image.append(i.get("image", ""))
        url.append(i.get("url", ""))
    news = zip(title, description, image, url)
    return news


def index(request):
    news = get_news(category="general")
    # featured_news = get_featured_news()
    return render(
        request,
        "newsapp/index.html",
        {"news": news},
    )


# Create your views here.
def sports(request):
    news = get_news(category="sports")
    return render(
        request,
        "newsapp/sports.html",
        {"news": news},
    )


def science(request):
    news = get_news(category="science")
    return render(
        request,
        "newsapp/science.html",
        {"news": news},
    )


def jp(request):
    news = get_news(country="jp")
    return render(
        request,
        "newsapp/jp.html",
        {"news": news},
    )


def fr(request):
    news = get_news(country="fr")
    return render(
        request,
        "newsapp/fr.html",
        {"news": news},
    )
