# blog/forms.py
from django import forms
from django.forms import widgets, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Article, ArticleComment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field


class ArticleCreateForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':12}))

    def clean_title(self):
        data = self.cleaned_data['title']
        
        # Remember to always return the cleaned data.
        return data

    def clean_content(self):
        data = self.cleaned_data['content']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Article',
            Field('title', css_class='form-group col-md-4 mb-0'),
            Field('content', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Article
        fields = ('title', 'content',)

class ArticleCommentCreateForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    def clean_description(self):
        data = self.cleaned_data['description']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Comment',
            Field('description', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Submit')
        )

    class Meta:
        model = ArticleComment
        fields = ('description',)
