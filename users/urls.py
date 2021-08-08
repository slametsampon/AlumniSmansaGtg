# accounts/urls.py
from django.urls import path
from . import views 

app_name = 'users'
urlpatterns = [
    path('signup/', views.AlumniSmansaUserCreateView.as_view(), name='signup'),
    path('admin/', views.AdminSmansaView.as_view(), name='admin'),
    path('authors/', views.AlumniSmansaUserListView.as_view(), name='authors'),
    path('new_comers/', views.AlumniSmansaUserNewListView.as_view(), name='authorsNew'),
    path('active/', views.AlumniSmansaUserActiveListView.as_view(), name='authorsActive'),
    path('verify/<int:pk>/', views.AlumniSmansaUserVerifyView.as_view(), name='authorVerify'),
    path('author/<int:pk>', views.AlumniSmansaUserDetailView.as_view(), name='authorDetail'),
]

urlpatterns += [ 
    # <pk> is identification for id field, 
    # slug can also be used 
    path('author/<int:pk>/delete/', views.AlumniSmansaUserDeleteView.as_view(), name='authorDelete'), 
    path('author/<int:pk>/update/', views.AlumniSmansaUserUpdateView.as_view(), name='authorUpdate'), 
]