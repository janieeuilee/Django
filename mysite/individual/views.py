from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from individual.models import Post, Individual
from django.db.models import Q
from django.views.generic.edit import FormView, CreateView

from mysite.views import LoginRequiredMixin
from django.urls import reverse_lazy
from individual.models import Individual


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = "individual/post_all.html" # post_list.html
    context_object_name = "posts" # object_list

    #paginate_by = 2s
class   IndividualCreateView(LoginRequiredMixin, CreateView):
    model = Individual
    fields = ['user_name', 'enterprise_name', 'additional']
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(IndividualCreateView, self).form_valid(form)


   


# post_detail.html
class PostDV(DetailView): # select * from where blog_post where slug=?
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'    

# class SearchFormView(FormView):
#     form_class = PostSearchForm # forms.py에 생성
#     template_name = "individual/post_search.html"
    
#     def form_valid(self, form): # self.request
#         schWord = '%s' % self.request.POST['search_word']
        
#         post_list = Post.objects.filter(Q(title__icontains=schWord) | 
#         Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
        
#         context = {}
#         context['form'] = form
#         context['search_keyword'] = schWord
#         context['search_list'] = post_list

#         return render(self.request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content']
    initial = {'slug': 'auto-filling-by-title'}
    success_url = reverse_lazy('individual:index')

    def form_valid(self, form): # self.request
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

# class PostChangeLV(LoginRequiredMixin, ListView):
#     template_name = "blog/post_change_list.html"

#     def get_queryset(self):
#         return Post.objects.filter(owner = self.request.user)

# class PostUpdateView(LoginRequiredMixin, UpdateView):    
#     model = Post
#     fields = ['title', 'slug', 'description', 'content']
#     success_url = reverse_lazy('blog:index')

# class PostDeleteView(LoginRequiredMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:index')

class IndividualCreateView(LoginRequiredMixin, CreateView):
    model = Individual
    fields = ['user_name', 'enterprise_name', 'additional']
    success_url = reverse_lazy('individual:back')
    def form_valid(self, form):
        print(form)
        form.instance.owner = self.request.user
        return super(IndividualCreateView, self).form_valid(form)
