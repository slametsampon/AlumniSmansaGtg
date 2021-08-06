from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

import uuid
from datetime import date

from users.models import AlumniSmansaUser

class Article(models.Model):
    """
    Model representing a article post.
    """
    id = models.UUIDField( # new
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(AlumniSmansaUser, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because Article can only have one author/AlumniSmansaUser, but AlumniSmansaUser can have multiple articles.
    content = models.TextField(max_length=2000, help_text="Enter you article text here.")
    post_date = models.DateField(default=date.today)
    
    class Meta:
        ordering = ["-post_date"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular article instance.
        """
        return reverse('articles:articleDetail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        

class ArticleComment(models.Model):
    """
    Model representing a comment against a article post.
    """
    description = models.TextField(max_length=1000, help_text="Enter comment about article here.")
    author = models.ForeignKey(AlumniSmansaUser, on_delete=models.SET_NULL, null=True)
      # Foreign Key used because ArticleComment can only have one author/AlumniSmansaUser, but users can have multiple comments
    post_date = models.DateTimeField(auto_now_add=True)
    article= models.ForeignKey(Article, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=75
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring
