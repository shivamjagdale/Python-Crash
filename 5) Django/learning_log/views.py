from django.shortcuts import render

from . models import Topic, Entry

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request=request, template_name="learning_log/index.html")

"""------------------------------------------------------------------------"""

# To display only topic names 
@login_required
def topics(request):

    # Get the individual topics 
    topics = Topic.objects.filter(owner = request.user).order_by("date_added")

    # context 
    context = {"topics":topics}

    # render 
    return render(request, "learning_log/topics.html", context)

"""------------------------------------------------------------------------"""
# To display topic and it's entries 

from django.http import Http404

@login_required
def topic(request, topic_id):

    # get the topic 
    topic = Topic.objects.get(id=topic_id)
    
    # Make sure the topic belongs to the current owner
    if topic.owner != request.user:
        raise Http404

    # get the entries 
    entries = topic.entry_set.order_by("-date_added")

    # context 
    context = {"topic":topic, "entries":entries}

    # render 
    return render(request, "learning_log/topic.html", context)

"""------------------------------------------------------------------------"""
# Topic Form 
from django.shortcuts import render, redirect
from . forms import TopicForm

@login_required
def new_topic(request):

    # Check the request method 
    if request.method != "POST":
        # create a blank form 
        form = TopicForm()
    else:
        # User has submitted something POST
        form = TopicForm(data=request.POST)

        # validate the submitted info
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_log:topics")

    # make the form available to the html
    context = {"form":form}
    return render(request, "learning_log/new_topic.html", context)

"""------------------------------------------------------------------------"""

# Entry Form 
from . forms import TopicForm, EntryForm

@login_required
def new_entry(request, topic_id):

    # Get the topic 
    topic = Topic.objects.get(id=topic_id)

    # check what type of request it is 
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return redirect('learning_log:topic', topic_id=topic_id)

    # context and render 
    context = {"topic":topic, "form":form}
    return render(request, 'learning_log/new_entry.html', context)

"""------------------------------------------------------------------------"""
# Edit Entry Function

from . models import Topic, Entry

@login_required
def edit_entry(request, entry_id):

    # Find existing entry 
    entry = Entry.objects.get(id=entry_id)

    # Find which topic the entry belongs to 
    topic = entry.topic

    # Make sure the entry belongs to the current owner
    if topic.owner != request.user:
        raise Http404

    # Check what type of request it is 
    if request.method != "POST":
        # Prefilling the form with existing data 
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data = request.POST)

        if form.is_valid():
            form.save()
            return redirect("learning_log:topic", topic_id = topic.id)

    # Context and render 
    context = {"entry":entry, "topic":topic, "form":form}
    return render(request, "learning_log/edit_entry.html", context)