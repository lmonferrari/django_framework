from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm
from .models import Person


def person_list(request):
    persons = Person.objects.all()
    return render(request, 'lista.html', {'persons': persons})


def person_create(request):
    # tenta preencher com algo, caso seja um form novo
    # envia em branco
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'pessoa.html', {'form': form})


def person_edit(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None,
                      request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'pessoa.html', {'form': form})


def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('list')
