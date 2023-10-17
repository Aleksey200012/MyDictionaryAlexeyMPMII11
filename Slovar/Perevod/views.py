from django.shortcuts import render, redirect

from .forms import AddWordForm
from .Perevod_utils import filerw


def home(request):
    template_name = 'home.html'

    return render(request, template_name)


def words_list(request):
    template_name = 'words_list.html'

    words_ru, words_en = filerw.get_words()
    words = zip(words_ru, words_en)

    context = {
        'words': words
    }

    return render(request, template_name, context=context)


def add_word(request):
    template_name = 'add_word.html'

    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            filerw.add_words(form.cleaned_data['word_en'], form.cleaned_data['word_ru'])
            return redirect('home')
    else:
        form = AddWordForm()

    context = {
        'form': form
    }

    return render(request, template_name, context=context)

# Create your views here.
