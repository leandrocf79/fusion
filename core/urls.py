
from django.urls import path
from .views import IndexView, Teste404, Teste500

urlpatterns =[
    path ('', IndexView.as_view(), name='index'),
    #path ('teste/', TesteViews.as_view(), name='teste'), # Se alguem digitar teste/ no navegador abre página teste. http://127.0.0.1:8000/teste/
    path ('404/', Teste404.as_view(), name='404'),
    path ('500/', Teste500.as_view(), name='500'),
]