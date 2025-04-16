from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, DiaryEntryForm
from .models import DiaryEntry, Category

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'diary/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'diary/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index_view(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    show_archived = request.GET.get('archived') == '1'

    entries = DiaryEntry.objects.filter(user=request.user)
    if not show_archived:
        entries = entries.filter(is_archived=False)
    if category_filter:
        entries = entries.filter(category__name=category_filter)
    if query:
        entries = [e for e in entries if query.lower() in e.get_content().lower() or query.lower() in e.title.lower()]

    categories = Category.objects.all()
    return render(request, 'diary/index.html', {
        'entries': entries,
        'query': query,
        'category_filter': category_filter,
        'show_archived': show_archived,
        'categories': categories
    })

@login_required
def add_entry_view(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('index')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/add_entry.html', {'form': form})

@login_required
def edit_entry_view(request, entry_id):
    entry = get_object_or_404(DiaryEntry, pk=entry_id, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('index')
    else:
        form = DiaryEntryForm(initial={
            'title': entry.title,
            'content': entry.get_content(),
            'category': entry.category,
            'is_archived': entry.is_archived,
        }, instance=entry)
    return render(request, 'diary/add_entry.html', {'form': form})