# users/views.py
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .forms import AlumniSmansaUserCreateForm, AlumniSmansaUserVerifyForm, AlumniSmansaUserAdminForm, AlumniSmansaUserUpdateForm
from .models import AlumniSmansaUser
from articles.models import Article, ArticleComment

class AlumniSmansaUserCreateView(CreateView):
    form_class = AlumniSmansaUserCreateForm
    model = AlumniSmansaUser
    template_name = 'account/signup.html'

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(AlumniSmansaUserCreateView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        self.object.set_password(form.cleaned_data['password'])

        self.object.save()

        return super(AlumniSmansaUserCreateView,self).form_valid(form)    

class AlumniSmansaUserListView(generic.ListView):
    """
    Generic class-based view for a list of authors.
    """
    model = AlumniSmansaUser
    template_name = 'users/alumniSmansauserList.html'
    context_object_name = 'alumniSmansauserList'
    paginate_by = 5

    def get_queryset(self):

        if self.request.user.is_superuser:
            return AlumniSmansaUser.objects.filter(verified_by=0)
        else:
            displayUser = list()
            displayUser.append(self.request.user.id)

            activeUser = AlumniSmansaUser.objects.filter(verified_by__gt=0)

            for usr in activeUser:
                displayUser.append(usr.id)

            return AlumniSmansaUser.objects.filter(pk__in=displayUser)

class AlumniSmansaUserNewListView(generic.ListView):
    """
    Generic class-based view for a list of authors.
    """
    template_name = 'users/alumniSmansauserNewList.html'  # Specify your own template name/location
    model = AlumniSmansaUser
    context_object_name = 'alumniSmansauserList'
    paginate_by = 5

    def get_queryset(self):

        return AlumniSmansaUser.objects.filter(verified_by=0)

class AlumniSmansaUserActiveListView(generic.ListView):
    """
    Generic class-based view for a list of AlumniSmansaUser.
    """
    template_name = 'users/activeAlumniSmansaUserList.html'  # Specify your own template name/location
    model = AlumniSmansaUser
    context_object_name = 'alumniSmansauserList'
    paginate_by = 5

    def get_queryset(self):

        return AlumniSmansaUser.objects.filter(verified_by__gt=0)

class AlumniSmansaUserDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    template_name = 'users/alumniSmansauserDetail.html'
    model = AlumniSmansaUser

class AlumniSmansaUserVerifyView(LoginRequiredMixin, UpdateView):
    form_class = AlumniSmansaUserVerifyForm
    model = AlumniSmansaUser
    context_object_name = 'alumniSmansauserList'
    template_name = 'users/alumniSmansauserVerify.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(AlumniSmansaUserVerifyView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        if form.cleaned_data.get('user_mode', None) == '1':#general user
            #Add logged-in user as author of comment
            self.object.verified_by = self.request.user.id

            content_type = ContentType.objects.get_for_model(AlumniSmansaUser)
            permission = Permission.objects.get(
                codename='add_article',
                content_type=content_type,
            )
            self.object.user_permissions.add(permission)
            content_type = ContentType.objects.get_for_model(ArticleComment)
            permission = Permission.objects.get(
                codename='add_articlecomment',
                content_type=content_type,
            )
            self.object.user_permissions.add(permission)
        elif form.cleaned_data.get('user_mode', None) == '2':#Admin user
            self.object.is_staff = True
            self.object.is_admin = True
            self.object.is_superuser = True
        self.object.save()

        return super(AlumniSmansaUserVerifyView,self).form_valid(form)    

class AlumniSmansaUserAdminView(LoginRequiredMixin, FormView):
    template_name = 'users/alumniSmansauserAdmin.html'  # Specify your own template name/location
    form_class = AlumniSmansaUserAdminForm

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)

        context['caption'] = 'Article Alumni SMANSA Genteng'

        authors = AlumniSmansaUser.objects.all()
        newComers = authors.filter(verified_by=0).count()
        activeAuthors = authors.filter(verified_by__gt=0).count()
        context['authors'] = authors.count()
        context['newComers'] = newComers
        context['activeAuthors'] = activeAuthors

        articles = Article.objects.all().count()
        context['articles'] = articles

        return context

class AlumniSmansaUserDeleteView(generic.DeleteView): 
    # specify the model you want to use 
    template_name = 'users/alumniSmansauserConfirmDelete.html'
    model = AlumniSmansaUser 
      
    # can specify success url 
    # url to redirect after sucessfully 
    # deleting object 
    success_url = '/users/authors/'

class AlumniSmansaUserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AlumniSmansaUserUpdateForm
    model = AlumniSmansaUser
    template_name = 'users/alumniSmansauserUpdate.html'  # Specify your own template name/location

    # Sending user object to the form, to verify which fields to display/remove (depending on group)
    def getForm_kwargs(self):
        kwargs = super(AlumniSmansaUserUpdateView, self).getForm_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AlumniSmansaUserUpdateView, self).get_context_data(**kwargs)

        return context

    def form_valid(self, form,**kwargs):
        self.object = form.save(commit=False)

        #update password if non blank
        if len(form.cleaned_data['password']):
            self.object.set_password(form.cleaned_data['password'])

        if form.cleaned_data.get('user_mode', None) == '1':#general user
            #Add logged-in user as author of comment
            self.object.verified_by = self.request.user.id

            content_type = ContentType.objects.get_for_model(Article)
            permission = Permission.objects.get(
                codename='add_article',
                content_type=content_type,
            )
            self.object.user_permissions.add(permission)
            content_type = ContentType.objects.get_for_model(ArticleComment)
            permission = Permission.objects.get(
                codename='add_articlecomment',
                content_type=content_type,
            )
            self.object.user_permissions.add(permission)
        elif form.cleaned_data.get('user_mode', None) == '2':#Admin user
            self.object.is_staff = True
            self.object.is_admin = True
            self.object.is_superuser = True
        self.object.save()

        return super(AlumniSmansaUserUpdateView,self).form_valid(form)    
