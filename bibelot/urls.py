from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bibelot import views

urlpatterns = [
    path('bibelots/', views.BibelotList.as_view(), name='bibelot-list'),
    path('bibelots/<int:pk>/', views.BibelotDetail.as_view(), name='bibelot-detail'),

    path('bibelots/<int:pk>/highlight/',
         views.BibelotHighlight.as_view(), name='bibelot-highlight'), # new

    path('users/', views.UserList.as_view(), name='user-list'), # new
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'), # new
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

