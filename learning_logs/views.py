from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
# defined as python functions

def index(request):
    return render(request, 'learning_logs/index.html')

#get all topics
def topics(request):
    topics = Topic.objects.order_by('date')
    
    context = {'topics':topics} #use template tags/variables in template file

    return render(request, 'learning_logs/topics.html', context)

#get individual topics
def topic(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added') #- puts date in descending order, so newest entries show up on top

    context = {'topic':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)

#get: read data from DB, post: send data to DB

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else: #request is not blank
        form = TopicForm(data=request.POST)
    
        if form.is_valid(): #checks to see if all required fields have been filled
            form.save() #knows to save to topic b/c forms.py shows model = Topic
            
            return redirect('learning_logs:topics')

    context = {'form':form}

    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else: #request is not blank
        form = EntryForm(data=request.POST)
    
        if form.is_valid(): #checks to see if all required fields have been filled
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            form.save() #knows to save to topic b/c forms.py shows model = Topic
            
            return redirect('learning_logs:topic',topic_id=topic_id)

    context = {'form':form, 'topic':topic}

    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id) #use .id b/c we are using the topic variable

    context = {'entry':entry, 'topic':topic, 'form':form}
    
    return render(request, 'learning_logs/edit_entry.html', context)