from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.ArticleHomeView.as_view(), name='homeArticles'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('<uuid:pk>', views.ArticleDetailView.as_view(), name='articleDetail'),
    path('create/', views.ArticleCreateView.as_view(), name='articleCreate'),
    path('article/<uuid:pk>', views.ArticleDetailView.as_view(), name='articleDetail'),
    path('author/<int:pk>', views.ArticleListByAuthorView.as_view(), name='articlesByAuthor'),
    path('article/<uuid:pk>/comment/', views.ArticleCommentCreateView.as_view(), name='articleComment'),
]

if settings.DEBUG:   
    urlpatterns += [ 
        # <pk> is identification for id field, 
        # slug can also be used 
        path('delete/<uuid:pk>', views.ArticleDeleteView.as_view(), name='articleDelete'), 
        path('comment/<int:pk>/delete/', views.ArticleCommentDeleteView.as_view(), name='articleCommentDelete'), 
    ]
