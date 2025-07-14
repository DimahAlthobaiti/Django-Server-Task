from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonForm()

    people = Person.objects.all().order_by('id')
    return render(request, 'users/index.html', {'form': form, 'people': people})

def toggle_status(request, person_id):
    person = Person.objects.get(id=person_id)
    person.status = not person.status
    person.save()
    return JsonResponse({'status': person.status})