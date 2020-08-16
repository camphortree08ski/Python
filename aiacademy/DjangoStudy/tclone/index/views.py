from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    tweets = NewTweet.objects.values_list('tweet', flat=True)
    f = {
        'tweet': tweets,
        }
    return render(request,'index/index.html', f)

def new(request):
    new_tweet = NewTweetForm(request.POST or None)
    if new_tweet.is_valid():
        new_tweet = new_tweet.cleaned_data
        new_tweet = new_tweet['tweet']
        tweet = NewTweet(tweet=new_tweet)
        tweet.save()
        return redirect('/')
    else:
        new_tweet = new_tweet.as_table()
        f = {
                'new_tweet': new_tweet,
            }
        return render(request, 'index/new.html', f)
