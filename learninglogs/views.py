from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for learning log"""
    print(request.content_type)
    return render(request, 'learninglogs/index.html')

def topics(request):
    """The topics page for learning log"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learninglogs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic page, with all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # the minus sign before 'date_added' sorts in reverse order
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learninglogs/topic.html', context)

def new_topic(request): # essentially a multi_purpose view; the same URL does two things. one, it can return a blank form if a GET request
                        # is sent (standard browser request) OR it can save the filled form to the database if a POST request is sent,
                        # as it is from the html doc under the <form></form> tag.
    """The page for creating a new topic"""
    if request.method != 'POST': # this usually means it's a GET request
        # no data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST) #instantiate TopicForm with the necessary data, contained in the POST request
        if form.is_valid(): # checks things like whether the name is within the model's char limit
            form.save() # saves the form to the database
            return HttpResponseRedirect(reverse('learninglogs:topics')) # reverse is similar to the url template tag

    context = {'form': form} # context is a dictionary full of variables representing data that can be used in a template tag
    return render(request, 'learninglogs/new_topic.html', context)

def new_entry(request, topic_id):
    """The page for creating a new topic entry"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data submitted, create a blank form
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # <-- this tells Django to create a new entry object and store it in new_entry without
                                                # commiting it to the database yet
            new_entry.topic = topic # sets the new entry's topic attribute to the topic we just pulled from the database
            new_entry.save()
            return HttpResponseRedirect(reverse('learninglogs:topic',
                                        args=[topic_id])) # this works because the url topics/(topic_id) accepts an argument.
    context = {'topic': topic, 'form': form}
    return render(request, 'learninglogs/new_entry.html', context)

def edit_entry(request, entry_id):
    """The page for editing an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        #Initial request: pre_fill form with current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted: process entry
        form = EntryForm(instance=entry, data=request.POST) # creates a new instance of EntryForm, updated with the relevant data from
                                                            # the POST request
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learninglogs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learninglogs/edit_entry.html', context) # render is a shortcut function which combines the template (html doc)
                                                                    # with the context to provide an HtmlResponse
