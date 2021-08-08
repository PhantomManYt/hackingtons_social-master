from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .filters import OrderFilter
from home.models import Post

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def BootstrapFilterView(request):
    qs = Post.objects.all()
    title_contains_query = request.GET.get('title_contains')
    ordering = ['-date_posted']
    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)

    context = {
        'queryset': qs
    }
    return render(request, "users/search_user.html", context)

