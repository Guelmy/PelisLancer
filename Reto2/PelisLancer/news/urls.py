

from django.conf.urls import url, include, url
from .views import index, IndexListView
#from PelisLancer import news
#from news import views
#from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^index/(?P<username>\w+)' , TemplateView.as_view(template_name='fake.html'), name='fake'),
    url(r'^$', IndexListView.as_view()),
]
