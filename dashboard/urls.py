from django.urls import path
from . import views

app_name='dashboard' #define application namespace

#domain.com/dashboard/...
urlpatterns=[
    path('',views.PostListView.as_view(), name='post_list'),
    path('new',views.PostCreateView.as_view(), name='new_post'),
    path('<int:pk>/edit/',views.PostUpdateView.as_view(), name='update_post'),
    path("<int:pk>/delete/", views.BlogDeleteView.as_view(),name="post_delete"),   
]