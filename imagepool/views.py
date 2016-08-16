from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.core.paginator import Paginator,InvalidPage
from imagepool.models import ImagePool,ImageAlbum
from django.core.urlresolvers import reverse
from django.views.generic import ListView,DetailView,FormView
from django.template import RequestContext
from .forms import ImageUploadForm
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
        #print('Post call')
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files=request.FILES.getlist('file_to_upload')
        #print(len(files))
        if form.is_valid():
            for i in files:
                #print('Image uploaded')
                image = ImagePool(user=request.user, image=i,title = i.name)
                image.save()
            #print('Form valid') #Необходимо возвращать объект httpresponse для корректной работы редикрект
            #return self.form_valid(form)
            response =  {'status':1,'message':"Ok"}
        else:
            print('Form invalid')
            response =  {'status': 0, 'message': "Form invalid"}

        return HttpResponse(json.dumps(response),content_type='application/json')
        #return render(request, 'imagepool/imagepool_upload.html', {'form': form},RequestContext(request))


def delete_image(request,pk):
    try:
        ImagePool.objects.get(pk=pk).image.delete()
        ImagePool.objects.get(pk = pk).delete()
    except ImagePool.DoesNotExist:
        pass
    #return HttpResponse(json.dumps({'status':1}),content_type='application/json')
    return HttpResponseRedirect('/imagepool/')




