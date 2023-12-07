from django.urls import path
from tree.views import IndexPageView

app_name = 'tree'

urlpatterns = [
    path('tree_menu/', IndexPageView.as_view(), name='index')
]