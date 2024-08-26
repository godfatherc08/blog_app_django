from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            print("post successful")
            return redirect('home')
    else:
        form = PostForm()
        return render(request, 'post.html', {'form': form})


def view_post(request):
    return render(request, "view.html")
"""jf"""