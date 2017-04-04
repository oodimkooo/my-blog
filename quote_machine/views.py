from quote_machine.models import quotesMain
from quote_machine.forms import QuoteForm
from random import choice
from django.views.generic import ListView
from django.core import serializers
from django.http import JsonResponse
import json

class QuoteView(ListView):
	model = quotesMain
	template_name = 'quotes.html'
	
	def get_context_data(self, **kwargs):
		context = super(QuoteView, self).get_context_data(**kwargs)
		context['quote'] = quotesMain.objects.get(pk=choice(sorted([i.pk for i in quotesMain.objects.all()])))
		return context

def get_next_quote(request):
	if request.method == "GET":
		current_pk = int(request.GET.get('current_pk'))
		myObj = quotesMain.objects.filter(pk=choice([i.pk for i in quotesMain.objects.all() if i.pk != current_pk]))
		return JsonResponse(serializers.serialize('json', myObj), safe = False)

def set_new_quote(request):
	if request.method == "POST" and request.is_ajax():
		f = QuoteForm(request.POST)
		newQuote = f.save()
		return JsonResponse(serializers.serialize('json', quotesMain.objects.filter(pk=newQuote.pk)), safe = False)
