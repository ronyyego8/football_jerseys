from django.urls import path
from .views import JerseyListView, JerseyDetailView, JerseyCreateView, JerseyUpdateView, JerseyDeleteView
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('list/', JerseyListView.as_view(), name='jersey_list'),
    path('<int:pk>/', JerseyDetailView.as_view(), name='jersey_detail'),
    path('new/', JerseyCreateView.as_view(), name='jersey_create'),
    path('<int:pk>/update/', JerseyUpdateView.as_view(), name='jersey_update'),
    path('<int:pk>/delete/', JerseyDeleteView.as_view(), name='jersey_delete'),
]
