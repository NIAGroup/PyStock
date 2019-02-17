from django.urls import path
from django.conf.urls import include,url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('', views.printer, name='testFxn'),
    # ex: /polls/3
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/3/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r'^polls/scripts/NIA_stocks_automation.py', views.IndexView, name='chart')
]
