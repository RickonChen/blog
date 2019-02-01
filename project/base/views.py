from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Tag
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    items = Post.objects.all()
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'base/home.html', { 'items': items, 'title': 'Home' })

def tag(request, slug=None):
    _tag = get_object_or_404(Tag, slug=slug)
    items = Post.objects.filter(tags__slug=slug)
    title = 'Items tagged with "%s"' % _tag
    return render(request, 'base/tag.html', {'items': items, 'tag': _tag, 'title': title})

class Register(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile(request):
    return render(request, 'base/profile.html', { 'title': 'Profile' })
