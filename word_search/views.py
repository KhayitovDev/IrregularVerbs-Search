from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Q 
from django.urls import reverse_lazy
from .models import Word



class Login(LoginView):
    template_name='registration/login.html'
    authentication_form=AuthenticationForm
    success_url='admin-dashboard.html'

def admin(request):
    words=Word.objects.all()
    context={'words':words}
    return render(request, 'folder/admin-dashboard.html', context)

def search_page(request):
    words=Word.objects.all().order_by('first_form')[:8]
    word_search=request.GET.get('search')
    if word_search:
        words=Word.objects.filter(Q(first_form__icontains=word_search)|Q(second_form__icontains=word_search)|Q(third_form__icontains=word_search))
    context={"words":words}
    return render(request, 'folder/index.html', context)


def detail_page(request, pk):
    data=Word.objects.get(id=pk)
    context={"data":data}
    return render(request, 'folder/detail.html', context)

class Create(CreateView):
    model=Word
    fields='__all__'
    template_name='folder/create.html'
    success_url=reverse_lazy('admin-view')

class Update(UpdateView):
    model=Word
    fields=['first_form', 'second_form','third_form', 'example_first', 'example_second', 'example_third']
    template_name='folder/create.html'
    success_url=reverse_lazy('admin-view')

class Delete_View(DeleteView):
    model=Word
    template_name='folder/delete.html'
    success_url=reverse_lazy('admin-view')


