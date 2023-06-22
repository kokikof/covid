
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core import serializers
from .models import Test
from django.http import JsonResponse


class TestViewSet(APIView):

    def get(self, request):
        queryset = Test.objects.all().order_by('data_sdachi')
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')

    def post(self, request):
        queryset = Test.objects.all().order_by('data_sdachi')
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')


class TestGetSet (APIView):

    def get(self, request):
        queryset = Test.objects.all().order_by('data_sdachi')
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')

    def post(self, request):
        try:
            temp = Test()
            temp.data_sdachi = request.POST.get('data_sdachi')
            temp.resultat = request.POST.get('resultat')
            temp.FIO = request.POST.get('FIO')
            temp.IO = request.POST.get('IO')
            temp.save()
            return JsonResponse({"STATUS": "OK"})
        except Exception as e:
            print(e)
            return JsonResponse({"STATUS": "ERROR"})


class TestPutDel (APIView):

    def get(self, request, pk_index):
        queryset = Test.objects.all().order_by('data_sdachi')
        queryset_json = serializers.serialize('json', queryset)
        return HttpResponse(queryset_json, content_type='application/json')

    def delete(self, request, pk_index):
        try:
            Testt = Test.objects.get(pk=pk_index)
            Testt.delete()
            res = {"STATUS": "OK"}
            return JsonResponse(res)
        except Exception as e:
            print(e)
            return JsonResponse({"STATUS": "DELETE ERROR"})

    def put(self, request, pk_index):
        try:
            test_covid = Test.objects.get(pk=pk_index)
            print(request.POST)
            # request.PUT = put.dict()
            # print(request.PUT.get('FIO'))
            print(request.data)
            test_covid.FIO = request.data.get('FIO')
            test_covid.resultat = request.data.get('resultat')
            test_covid.data_sdachi = request.data.get('data_sdachi')
            test_covid.IO = request.data.get('IO')
            test_covid.save()
            res = {'status': 'UPDATE OK'}
            return JsonResponse(res)
        except Exception as e:
            print(e)
            res = {'status': 'UPDATE ERROR'}
            return JsonResponse(res)
def home(request):
    return render(request, 'home.html')

def send(request):
    error = False
    try:
        res = request.POST['res']
        fio = request.POST['FIO']
        date = request.POST['date']
        pasp = request.POST['pasport']
        print(res, fio, date, pasp)
        neww = Test()
        neww.FIO = fio
        neww.resultat = res
        neww.data_sdachi = date
        neww.IO = pasp
        neww.save()
        return redirect("/")    
    except:
        error = True
        return render(request, 'home.html', {"error":error})

def check(request):
    error = False
    try:
        idd = request.POST['us_id']
        us = Test.objects.get(pk=idd)
        return render(request, 'check.html', {'user': us})
    except:
        error = True
        return render(request, "home.html", {"error":error})

def new_page_view(request):
    return render(request, 'new_page.html')

def rosp (request):
    return render(request, 'rosp.html')

def cont(request):
    return render(request, 'сont.html')