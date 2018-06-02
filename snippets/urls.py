from django.urls import path
from snippets import views


app_name = 'snippets'
urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]
