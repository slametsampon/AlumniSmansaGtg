from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Article, ArticleComment
from .forms import ArticleCreateForm, ArticleCommentCreateForm
from users.models import AlumniSmansaUser

class ArticleHomeView(generic.ListView):
    """
    Generic class-based view for a list of all articless.
    """
    model = Article
    template_name = 'articles/articleList.html'
    context_object_name = 'articleList'
    paginate_by = 5
    
class ArticleListView(generic.ListView):
    """
    Generic class-based view for a list of all articless.
    """
    model = Article
    template_name = 'articles/articleList.html'
    context_object_name = 'articleList'
    paginate_by = 5

class ArticleDetailView(generic.DetailView):
    """
    Generic class-based detail view for a articles.
    """
    template_name = 'articles/articleDetail.html'
    model = Article

from django.shortcuts import get_object_or_404

class ArticleListByAuthorView(generic.ListView):
    """
    Generic class-based view for a list of articless posted by a particular AlumniSmansaUser.
    """
    model = Article
    paginate_by = 5
    template_name ='articles/articleListByAuthor.html'
    
    def get_queryset(self):
        """
        Return list of Article objects created by AlumniSmansaUser (author id specified in URL)
        """
        id = self.kwargs['pk']
        target_author=get_object_or_404(AlumniSmansaUser, pk = id)
        return Article.objects.filter(author=target_author)
        
    def get_context_data(self, **kwargs):
        """
        Add AlumniSmansaUser to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(ArticleListByAuthorView, self).get_context_data(**kwargs)
        # Get the articles object from the "pk" URL parameter and add it to the context
        context['articles'] = get_object_or_404(AlumniSmansaUser, pk = self.kwargs['pk'])
        return context
    
class ArticleCommentCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Form for adding a articles comment. Requires login. 
    """
    model = ArticleComment
    form_class = ArticleCommentCreateForm
    template_name = 'articles/articlesCommentCreateForm.html'

    def get_context_data(self, **kwargs):
        """
        Add associated articles to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(ArticleCommentCreateView, self).get_context_data(**kwargs)
        # Get the articles from id and add it to the context
        context['articles'] = get_object_or_404(Article, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated articles to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user
        #Associate comment with articles based on passed id
        form.instance.articles=get_object_or_404(Article, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(ArticleCommentCreateView, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated articles.
        """
        return reverse('articles:articles-detail', kwargs={'pk': self.kwargs['pk'],})

class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Form for ceating a articles. Requires login. 
    """
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/articlesForm.html'

    def get_context_data(self, **kwargs):
        """
        Add associated articles to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(ArticleCreateView, self).get_context_data(**kwargs)

        return context
        
    def form_valid(self, form):
        """
        Add author and associated articles to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.author = self.request.user

        # Call super-class form validation behaviour
        return super(ArticleCreateView, self).form_valid(form)

# import generic UpdateView 
from django.views.generic.edit import DeleteView 
  
class ArticleDeleteView(DeleteView): 
    # specify the model you want to use 
    model = Article 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url = '/articles/articless/'

class ArticleCommentDeleteView(DeleteView): 
    # specify the model you want to use 
    model = ArticleComment 
    
    #buffer context
    plus_context = {}
      
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        articles = ArticleComment.objects.get(pk = self.kwargs['pk']).articles

        self.plus_context['articles'] = articles

        return context
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    def get_success_url(self): 
        """
        After deleting comment return to associated articles.
        """
        articles = self.plus_context.get('articles', None)
        return reverse('articles:articles-detail', kwargs={'pk': articles.pk,})
