from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForms, EntryForms
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    '''Página principal do LLog'''
    return  render(request, "LLog/index.html")

@login_required
def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}

    return render(request, "LLog/topics.html", context)

@login_required
def topic(request, topic_id):
    """Mostra um único tópico"""
    topic = Topic.objects.get(id = topic_id)

    if topic.owner != request.user:
        raise(Http404)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic,
               'entries': entries}

    return render(request,  'LLog/topic.html', context)

@login_required
def new_topic(request):
    '''Adiciona um novo tópico'''
    if request.method != 'POST':
        form = TopicForms()
    else:
        form = TopicForms(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render(request, 'LLog/new_topic.html', context)

@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    
    messages.success(request, "Tópico excluído com sucesso")
    return HttpResponseRedirect(reverse('topics'))
    
@login_required
def add_entry(request, topic_id):
    
    topic = Topic.objects.get(id = topic_id)

    if topic.owner != request.user:
        raise(Http404)

    
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

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise(Http404)

    if request.method != 'POST':
        form = EntryForms(instance=entry)
    else:
        form = EntryForms(instance=entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
        
    context = {'entry': entry, 'topic':topic, 'form': form}
    return render(request, 'LLog/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    entry.delete()

    return HttpResponseRedirect(reverse('topic', args=[topic.id]))