from django.shortcuts import render, redirect
from .models import DiaryEntry, Category
from .forms import DiaryEntryForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'diary/register.html', {'form': form})

@login_required
def index(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    show_archived = request.GET.get('archived') == '1'

    entries = DiaryEntry.objects.filter(user=request.user, is_archived=show_archived)

    if query:
        entries = [e for e in entries if query.lower() in e.get_content().lower() or query.lower() in e.title.lower()]

    if category_filter:
        entries = [e for e in entries if e.category and e.category.name == category_filter]

    categories = Category.objects.all()
    return render(request, 'diary/index.html', {
        'entries': entries,
        'categories': categories,
        'query': query,
        'category_filter': category_filter,
        'show_archived': show_archived
    })

@login_required
def add_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.set_content(form.cleaned_data['content'])
            entry.save()
            return redirect('index')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/add_entry.html', {'form': form})
