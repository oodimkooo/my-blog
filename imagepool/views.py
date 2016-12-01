from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.core.paginator import Paginator,InvalidPage
from imagepool.models import ImagePool,ImageAlbum
from django.core.urlresolvers import reverse
from django.views.generic import ListView,DetailView,FormView
from django.template import RequestContext
from .forms import ImageUploadForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
import json

# Create your views here.
class Image_List(ListView):
    model = ImagePool
    template_name = 'imagepool_list.html'

    def get_context_data(self, **kwargs):
        context = super(Image_List,self).get_context_data(**kwargs)
        context['images'] = ImagePool.objects.all()
        context['albums'] = ImageAlbum.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(None, request.POST)
            if form.is_valid():
                print('checked CBV post')
                login(request, form.get_user())
                response = {'status': 1, 'message': "Ok"}
                print('OK')
            else:
                response = {'status': 0, 'message': "Fail"}
                print('Fail')
            return HttpResponse(json.dumps(response), content_type='application/json')
        return render(request, 'imagepool/image_index.html', {'form': form})



class Image_Detail(DetailView):
    model = ImagePool
    template_name = 'imagepool_detail.html'


class Album_list(ListView):
    model = ImageAlbum
    template_name = 'imagepool_base.html'


class Image_Upload(FormView):
    form_class = ImageUploadForm
    template_name = 'imagepool_upload.html'
    def post(self,request,*args,**kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files=request.FILES.getlist('file_to_upload')
        if form.is_valid():
            for i in files:
                image = ImagePool(user=request.user, image=i,title = i.name,is_commentable=True)
                image.save()
            response =  {'status':1,'message':"Ok"}
        else:
            print('Form invalid')
            response =  {'status': 0, 'message': "Form invalid"}

        return HttpResponse(json.dumps(response),content_type='application/json')

def delete_image(request,pk):
    try:
        ImagePool.objects.get(pk=pk).image.delete()
        ImagePool.objects.get(pk = pk).delete()
    except ImagePool.DoesNotExist:
        pass
    return HttpResponseRedirect('/imagepool/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/imagepool/")



