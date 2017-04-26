from django.shortcuts import render, render_to_response
from .models import Event
from django.core import serializers
from django.http import JsonResponse
from .forms import EventForm
from django.template.loader import render_to_string


def index(request):
    return render_to_response('calendar.html')

def get_events(request):
    if request.method == "GET":
        myMonth = int(request.GET.get("month")) + 1
        myYear = int(request.GET.get("year"))
        if Event.objects.count() > 0:
            myQuery = Event.objects.filter(startDate__month = myMonth, startDate__year = myYear)
            return JsonResponse(serializers.serialize('json', myQuery), safe = False)
        else:
            return False


def set_event(request):
    data = {}
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
            data['errors'] = {f: e.get_json_data() for f, e in form.errors.items()}
    else:
        form = EventForm

    context = {'form': form}
    data['html_form'] = render_to_string('booking/create_event.html', context, request = request)
    return JsonResponse(data)