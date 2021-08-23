from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .models import Article, ArticleComment

class ArticleTest(TestCase):
    def test_create_article(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'will', 
            email = 'will@email.com', 
            address = 'maron', 
            mobile_number = '0811-3323-706', 
            bio = 'short bio', 
            password = 'test123')
        
        article = Article.objects.create(
            title = 'kancil nyolong timun',
            author = user
        )
        
        self.assertEqual(article.title,'kancil nyolong timun')
        self.assertEqual(article.author,user)
    
    
class ArticleCommentTest(TestCase):
    def test_create_article_comment(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'will', 
            email = 'will@email.com', 
            address = 'maron', 
            mobile_number = '0811-3323-706', 
            bio = 'short bio', 
            password = 'test123')
        
        article = Article.objects.create(
            title = 'kancil nyolong timun',
            author = user
        )
        
        articleComment = ArticleComment.objects.create(
            description = "It's nice ",
            author = user,
            article = article
        )
        
        self.assertEqual(articleComment.description,"It's nice ")
        self.assertEqual(articleComment.article,article)
        self.assertEqual(articleComment.author,user)
    
class ArticleCreateTest(TestCase):
    def setUp(self):
        url = reverse('articles:articleCreate')
        self.response = self.client.get(url)
        
    def test_articlecreate_template(self):
        pass
        