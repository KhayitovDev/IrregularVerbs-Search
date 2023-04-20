from django.shortcuts import render
from django.db.models import Q 
from .models import Word


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