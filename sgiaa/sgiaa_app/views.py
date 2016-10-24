#unicode utf-8
from django.shortcuts import render
from .models import Bairro
from django.shortcuts import render, get_object_or_404
import googlemaps
from datetime import datetime
import csv

def base(request):
    return render(request,"sgiaa_app/base.html",{})
def index(request):
    return render(request,"sgiaa_app/index.html",{})

def ver_bairros(request):
    if request.method == 'GET':
        all_bairros = Bairro.objects.all()
        cor = '142, 68, 173,1.0'
        margem = "margin:0px;"
        titulo = "Bairros de Natal"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'margem':margem,'titulo':titulo})



def ver_mapa(request):
    geocode = []
    nome = []
    coordenadas = []
    bairros = []
    marcacao = ""
    gmaps = googlemaps.Client(key='AIzaSyC2j9HL1dcHxSZGc6MhQBqPolkvpo_AdMo')
    all_bairros = Bairro.objects.all()

    #for bairro in all_bairros:
    #    geocode = gmaps.geocode(bairro.nome +' Natal,Rio Grande do Norte, BR')
    #    lng = geocode[0]['geometry']['location']['lng']
    #    lat = geocode[0]['geometry']['location']['lat']
    #    nome.append( geocode[0]['address_components'][0]['short_name'])
    #    coordenadas.append("{"+"lat:"+str(lat)+","+"lng :"+str(lng)+"}")
    #for i in range(0,len(nome)):
    #    marcacao += nome[i]+":{ center :"+coordenadas[i]+",population : "+ str(200)+"},"

    return render(request,"sgiaa_app/ver_mapa.html",{'all_bairros':all_bairros,'geocode':geocode})





def ver_bairros_1(request):
    all_bairros = Bairro.objects.filter(bairro_risco = 1)
    cor = '189, 195, 199,1.0'
    titulo = "Risco nível 1"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})

def ver_bairros_2(request):
    all_bairros = Bairro.objects.filter(bairro_risco = 2)
    cor = '46, 204, 113,1.0'
    titulo = "Risco nível 2"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})

def ver_bairros_3(request):
    all_bairros = Bairro.objects.filter(bairro_risco = 3)
    cor ='52, 152, 219,1.0'
    titulo = "Risco nível 3"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})

def ver_bairros_4(request):
    all_bairros = Bairro.objects.filter(bairro_risco = 4)
    cor = '230, 126, 34,1.0'
    titulo = "Risco nível 4"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})

def ver_bairros_5(request):
    all_bairros = Bairro.objects.filter(bairro_risco = 5)
    cor = '231, 76, 60,1.0'
    titulo = "Risco nível 5"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})

def ver_regiao_1(request):
    all_bairros = Bairro.objects.filter(id_regiao = 1)
    cor = '142, 68, 173,1.0'
    titulo = "Zona norte"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})
def ver_regiao_2(request):
    all_bairros = Bairro.objects.filter(id_regiao = 2)
    cor = '142, 68, 173,1.0'
    titulo = "Zona sul"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})
def ver_regiao_3(request):
    all_bairros = Bairro.objects.filter(id_regiao = 3)
    cor = '142, 68, 173,1.0'
    titulo = "Zona leste"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})
def ver_regiao_4(request):
    all_bairros = Bairro.objects.filter(id_regiao = 4)
    cor = '142, 68, 173,1.0'
    titulo = "Zona oeste"
    return render(request,"sgiaa_app/ver_bairros.html",{'all_bairros':all_bairros,'cor':cor,'titulo':titulo})
