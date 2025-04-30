from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForms, EntryForms
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    '''Página principal do LLog'''
    return  render(request, "LLog/index.html")

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, "LLog/topics.html", context)

def topic(request, topic_id):
    """Mostra um único tópico"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}

    return render(request,  'LLog/topic.html', context)

def new_topic(request):
    '''Adiciona um novo tópico'''
    if request.method != 'POST':
        form = TopicForms()
    else:
        form = TopicForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render(request, 'LLog/new_topic.html', context)

def add_entry(request, topic_id):
    
    topic = Topic.objects.get(id = topic_id)
    
    if request.method != 'POST':
        form = EntryForms()
    else:
        form = EntryForms(data=request.POST)
        if form.is_valid():
            add_entry = form.save(commit=False)
            add_entry.topic = topic
            add_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic':topic, 'form': form}
    return render(request, 'LLog/add_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForms(instance=entry)
    else:
        form = EntryForms(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
        
    context = {'entry': entry, 'topic':topic, 'form': form}
    return render(request, 'LLog/edit_entry.html', context)