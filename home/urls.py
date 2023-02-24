from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('detail/<int:user_id>/<slug:post_slug>', views.PostDetailView.as_view(), name='post_detail'),
]
