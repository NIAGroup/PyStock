from django.urls import path
from django.conf.urls import include,url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls
    path('', views.IndexView.as_view(), name='index'),
<<<<<<< HEAD
    path('', views.test, name='testFxn'),
=======
    path('', views.printer, name='testFxn'),
>>>>>>> 4ed7ccfc86b3d0ce2a81a7c8b7ed7b8457e5b16a
    # ex: /polls/3
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/3/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r'^polls/scripts/NIA_stocks_automation.py', views.IndexView, name='chart')
]
