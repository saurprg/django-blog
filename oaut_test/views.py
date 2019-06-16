from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import LoginForm
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request , 'oaut_test/post_list.html',{'posts' : posts})

def next_page(request):

    if request.method == 'POST':
        
        form = LoginForm(request.POST)

    else :
        form = LoginForm()

    return render(request,'oaut_test/nextpage.html',{'form' : form})

def new_post(request):
    Post.objects.create(author=User.objects.get(username='saur_prg'), title=request.GET.get('title'), text=request.GET.get('txt'))   
    Post.objects.get(title = request.GET.get('title')).publish()
    return post_list(request)