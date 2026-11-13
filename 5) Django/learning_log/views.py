from django.shortcuts import render

from . models import Topic

# Create your views here.

def index(request):
    return render(request=request, template_name="learning_log/index.html", )

def topics(request):

    # get all the topics and order them by date 
    topics = Topic.objects.order_by("date_added")

    # context 
    context = {"topics":topics}

    # render 
    return render(request, 'learning_log/topics.html', context)

def topic(request, topic_id):

    # Get individual topic 
    topic = Topic.objects.get(id=topic_id)

    # entries 
    entries = topic.entry_set.order_by("-date_added")

    # context 
    context = {"topics":topic, "entries":entries}

    # render 
    return render(request, 'learning_log/topic.html', context)