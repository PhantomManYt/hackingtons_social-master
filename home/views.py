from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, manager
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from account.models import CustomUser
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, request
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
)
from .models import Post, Comment, Announce, UserList
from users.models import Profile
from users.filters import OrderFilter

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    if post.likes.filter(id=request.user.id).exists():
       post.likes.remove(request.user)
       liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
   
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        disliked = False
    else:
        post.dislikes.add(request.user)
        disliked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'home/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'link', 'link_title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def save(self, *args, **kwargs):
        if self.image:
            self.image = get_thumbnail(self.image, '250, 250', quality=99, format='JPEG')
        super(image, self).save(*args, **kwargs)


class UserPostListView(ListView):
    model = Post
    template_name = 'home/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    def save(self, *args, **kwargs):
        if self.image:
            self.image = get_thumbnail(self.image, '250, 250', quality=99, format='JPEG')
        super(image, self).save(*args, **kwargs)

    def get_queryset(self):
        user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted') 
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()

        liked = False
        disliked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        if stuff.dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        context["liked"] = liked
        context["disliked"] = disliked 
        return context
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'link', 'link_title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post    
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['name', 'content', 'link', 'link_title']
    
    success_url = '/'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

def error(request):
    return render(request, 'home/error.html')


class AnnounceListView(ListView):
    model = Announce
    template_name = 'home/announce.html' 
    context_object_name = 'announcements'
    ordering = ['-date_posted']
    paginate_by = 10

class AnnounceCreateView(LoginRequiredMixin, CreateView):
    model = Announce
    fields = ['announcement']

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)

class UserListView(ListView):
    model = UserList
    user = CustomUser.objects.all()
    context_object_name = 'users'
    template_name = 'home/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['object_list'] = CustomUser.objects.all()
        return context
    
    


   
    
    
