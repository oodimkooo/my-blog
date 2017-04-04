from django.forms import ModelForm,TextInput
from quote_machine.models import quotesMain

class QuoteForm(ModelForm):
    class Meta:
        model = quotesMain
        fields = ['content', 'author','publisher']
        
        widgets = {
            'content': TextInput(attrs={'class': 'quote-form', 'required': 'true'}),
            'author': TextInput(attrs={'class': 'quote-form','required': 'true'}),
            'publisher': TextInput(attrs={'class': 'quote-form'}),
        }
        