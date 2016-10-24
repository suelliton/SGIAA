from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^ver_bairros/$',views.ver_bairros),
    url(r'^ver_bairros_1/$',views.ver_bairros_1),
    url(r'^ver_bairros_2/$',views.ver_bairros_2),
    url(r'^ver_bairros_3/$',views.ver_bairros_3),
    url(r'^ver_bairros_4/$',views.ver_bairros_4),
    url(r'^ver_bairros_5/$',views.ver_bairros_5),
    url(r'^ver_regiao_1/$',views.ver_regiao_1),
    url(r'^ver_regiao_2/$',views.ver_regiao_2),
    url(r'^ver_regiao_3/$',views.ver_regiao_3),
    url(r'^ver_regiao_4/$',views.ver_regiao_4),
    url(r'^ver_mapa/$',views.ver_mapa),
]
