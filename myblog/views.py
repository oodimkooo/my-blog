# coding: utf8
from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView
from myblog.models import BlogPost,RiderPost,MyTask,SliderPost,PostCategory
from myblog.forms import PostForm #,RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator,EmptyPage
from datetime import datetime
import json


#Для поиска
from django.db.models import Q
import operator
from functools import reduce


#декораторы нужны для "оборачивания" функций с целью изменения их поведения
#user_passes_test() takes a required argument: a callable that takes a User object and returns True if the user is allowed to view the page
#The user_passes_test decorator whether the user is admin or not. If not, it will redirect the user to login page
from django.contrib.auth.decorators import user_passes_test,login_required


# Список постов
class PostListView(ListView):
    context_object_name = 'list'
    # для generic вью задавать шаблон явно необязательно, они ожидают найти Model_list (в данном случае)
    # в данном случае щаблон укажем для унификации имен
    template_name = 'blogpost_list.html'
    queryset = BlogPost.objects.all()
    paginate_by = 5

    def get_queryset(self):
        postlist=super(PostListView,self).get_queryset()
        return postlist.filter(published_date__isnull = False)

    def get_context_data(self, **kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        # Для доступа к нескольким моделям в рамках представления:
        context['posts'] = BlogPost.objects.all()
        #context['slider_post'] = SliderPost.objects.all()
        #context['tasks'] = MyTask.objects.all()
        context['categories'] = PostCategory.objects.all()
        #context['slider_range'] = range(1,SliderPost.objects.all().count() + 1)
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
        return render(request, 'myblog/blogpost_list.html', {'form': form})

class PostDetailView(DetailView):
    model = BlogPost

    def get(self, request, **kwargs):
        self.object = self.get_object()
        if self.request.path != self.object.get_absolute_url():
            return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

    def rating(self):
        self.object = self.get_object()
        postRating = self.object.userUpVotes.all().count() - self.object.userDownVotes.all().count()
        return postRating

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        # context['tasks'] = MyTask.objects.all()
        context['categories'] = PostCategory.objects.all()
        return context

#Поиск
class CategoryListView(ListView):
    queryset = BlogPost.objects.all()
    paginate_by = 5
    template_name = 'blogpost_category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        context['categories'] = PostCategory.objects.all()
        return context

    def get_queryset(self):
        category_title = self.kwargs['category']
        category = PostCategory.objects.select_related().get(title = category_title)
        postlist = category.blogpost_set.all()
        return postlist.filter(published_date__isnull = False)

class SearchByTextListView(ListView):
    queryset = BlogPost.objects.all()
    paginate_by = 5
    template_name = 'blogpost_search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchByTextListView, self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        context['categories'] = PostCategory.objects.all()
        return context

    def get_queryset(self):
        result = super(SearchByTextListView, self).get_queryset()
        print(self.request)
        query = self.request.GET.get('text')
        if query:
            query_list = query.lower().split()
            #reduce - применить функцию-первый аргумент к списку - второму элементу
            result = result.filter(
                #Q объекты представляют куски sql в виде python объектов
                # operator.and_ - стандартная обертка для логических операторов, аналогична return a & b
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(shortcontent__icontains=q) for q in query_list))
            )
        return result

class SearchByTagListView(ListView):
    queryset = BlogPost.objects.all()
    paginate_by = 5
    template_name = 'blogpost_search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchByTagListView, self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        context['categories'] = PostCategory.objects.all()
        return context

    def get_queryset(self):
        tag = self.kwargs['tag']
        return BlogPost.objects.filter(tags__name__in=[tag])

#Список черновиков
class DraftListView(ListView):
    model = BlogPost
    paginate_by = 10

    def get_queryset(self):
        postlist=super(DraftListView,self).get_queryset()
        return postlist.filter(published_date__isnull = True)

    def get_context_data(self, **kwargs):
        context = super(DraftListView,self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        context['tasks'] = MyTask.objects.all()
        return context

class TaskDetailView(DetailView):
    model = MyTask
    def get_context_data(self, **kwargs):
        context = super(TaskDetailView,self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        context['tasks'] = MyTask.objects.all()
        return context
'''
def register_user(request):
    context = RequestContext(request) #получить контекст запроса для последующего определения типа
    #контекст - словарь с найденными в процессе компиляциии страницы переменными
    registered = False # переменная для проверки успешности регистрации
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid:
            user = form.save()
            user.set_password(user.password)
            user.save
            registered = True
            #login(request,user)
            return HttpResponseRedirect("/blog/login/")
        else:
            print(form.errors)
            return HttpResponse("Failed")
    else:
        form = RegistrationForm()
    return render_to_response("myblog/register.html",{"form" : form,"registered" : registered},context)

def login_user(request):
    context = RequestContext(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/blog/")
            else:
                return HttpResponse("Disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'myblog/login.html',{},context)
'''
@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/blog/")

#реализуем через самописный view, т.к. данный подход предоставит больше гибкости, в том числе и в шаблонах
@login_required
def add_post(request):
    if request.POST:
        if 'my_return' in request.POST:
            print("Redirect to main")
            return HttpResponseRedirect("/blog/")
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                BlogPost = form.save(commit=False) #не сохранять сразу, т.к. обновится автор
                BlogPost.author = request.user
                if 'my_publish' in request.POST:
                    print("Publish")
                    BlogPost.published_date = datetime.now()
                BlogPost.save()
                form.save_m2m()
                print("Save")
                return redirect(BlogPost)
    else:
        form = PostForm()
    return render(request,'myblog/add_post.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_post(request,pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        if 'my_publish' in request.POST:
            print("Publish")
            post.published_date = datetime.now()
        post.save()
        form.save_m2m()
        print("Save")
        return redirect("detail", pk=post.pk)
    return render(request, 'myblog/add_post.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_post(request,pk):
    post = get_object_or_404(BlogPost,pk=pk).delete()
    return HttpResponseRedirect('/blog/')

@login_required
def post_vote(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    print(pk)
    curUserUpVote = post.userUpVotes.filter(id=request.user.id).count()
    curUserDownVote = post.userDownVotes.filter(id=request.user.id).count()
    vote_type = request.POST.get('type')
    vote_action = request.POST.get('action')
    if vote_action == "vote":
        print("User votes")
        if curUserUpVote == 0 and curUserDownVote == 0:
            print("User votes")
            if (vote_type == 'up'):
                post.userUpVotes.add(request.user)
                print("User upvotes")
            if (vote_type == 'down'):
                post.userDownVotes.add(request.user)
                print("User downvotes")
    currentVotesSum = post.userUpVotes.count() - post.userDownVotes.count()
    return HttpResponse(currentVotesSum)

@login_required
def task_action(request):
    task_id = request.POST.get('id')
    task_action = request.POST.get('action')
    task=get_object_or_404(MyTask,pk=task_id)
    print(task.title)
    print(task.is_completed)
    if request.method == "POST":
        print('Method Post')
        if task_action == "complete":
            task.is_completed = True
            print('completed')
        if task_action == "delete":
            task.is_deleted = True
            print('deleted')
        task.save()
        print('Save')
        print(task.is_completed)
        return HttpResponse("success")
