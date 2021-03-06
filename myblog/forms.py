from django.forms import ModelForm,TextInput,Textarea
from myblog.models import BlogPost,PostCategory
from django.contrib.auth.models import User
from taggit.forms import TagField

class PostForm(ModelForm):
    tags = TagField(label="Теги")
    class Meta:
        model = BlogPost
        exclude = ['author','creation_date','userUpVotes','userDownVotes','published_date']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control','required':'true'}),
            'shortcontent': Textarea(attrs={'class': 'form-control'}),
            'fulltext': Textarea(attrs={'class': 'form-control'}),
            'tags': TextInput(attrs={'class': 'form-control'}),
        }
    class Media:
        js=('/static/myblog/js/tiny_mce/tiny_mce.js','')

class CategoryForm(ModelForm):
    class Meta:
        model = PostCategory
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'description': Textarea(attrs={'class': 'form-control'}),
        }
    class Media:
        js = ('/static/myblog/js/tiny_mce/tiny_mce.js', '')

'''
class RegistrationForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    #Чтобы не передавать в бд в открытом виде
    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password','email')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }
'''