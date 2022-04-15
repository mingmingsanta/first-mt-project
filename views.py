from django.shortcuts import render,redirect,get_object_or_404
from django.http.response import HttpResponse
from urllib import request
from django.http import HttpRequest
from .models import worker, workplace
from .forms import workerModelForm,workplaceModelForm




# def workertable(request):
#     return render(request,"MonitoringApp/workertable.html")




# def 근로자_목록(request,작업장1_id):      #근로자 목록
#     작업장1 = get_object_or_404(workplace,pk=작업장1_id)
#     #근로자 = worker.objects.all()
#     context = {
#         "근로자키" : 작업장1
#     }

#     return render(request,"근로자_목록.html",context)



def 근로자_목록(request):      #근로자 목록
    근로자 = worker.objects.all()   #    근로자 = worker.objects.all()
    context = {
        "근로자키" : 근로자
    }

    return render(request,"근로자_목록.html",context)




def 근로자_등록(request):     #근로자 등록
    폼 = workerModelForm()
    if request.method == "POST":
        폼 = workerModelForm(request.POST)

        if 폼.is_valid():
            폼.save()
            return redirect("/근로장_목록/근로자_목록")

    context = {
        "폼키" : 폼
    }

    return render(request,"근로자_등록.html",context)





def 근로자_상세(request,pk):
    근로자 = worker.objects.get(id=pk)    #근로자 = worker.objects.all()
    context = {
        "근로자키" : 근로자
    }

    return render(request,"근로자_상세.html",context)




def 근로자_업데이트(request,pk):
    근로자 = worker.objects.get(id=pk)

    폼 = workerModelForm(instance=근로자)
    if request.method == "POST":
        폼 = workerModelForm(request.POST,instance=근로자)

        if 폼.is_valid():
            폼.save()
            return redirect("/근로장_목록/근로자_목록")
    context = {
        "폼키" : 폼,
        "근로자키": 근로자
    }

    return render(request,"근로자_업데이트.html",context)




def 근로장_목록(request):
    근로장 = workplace.objects.all()
    근로자 = worker.objects.all()

    context = {
        "근로장키": 근로장,
        "근로자키": 근로자
    }
    return render(request, "근로장_목록.html", context)




def 근로장_등록(request):     #근로자 등록
    폼 = workplaceModelForm()
    if request.method == "POST":
        폼 = workplaceModelForm(request.POST)

        if 폼.is_valid():
            폼.save()
            return redirect("/")     #근로자 목록으로 이동

    context = {
        "폼키" : 폼
    }

    return render(request,"근로장_등록.html",context)



def 근로자_삭제(request,pk):
    근로자 = worker.objects.get(id=pk)
    근로자.delete()
    return redirect("/근로장_목록/근로자_목록")




def 근로장_삭제(request,pk):
    근로장  = workplace.objects.get(id=pk)
    근로장.delete()
    return redirect("/근로장_목록")




def 근로장_업데이트(request,pk):
    근로장 = workplace.objects.get(id=pk)

    폼 = workplaceModelForm(instance=근로장)
    if request.method == "POST":
        폼 = workplaceModelForm(request.POST,instance=근로장)

        if 폼.is_valid():
            폼.save()
            return redirect("/근로장_목록")
    context = {
        "폼키" : 폼,
        "근로장키": 근로장
    }

    return render(request,"근로장_업데이트.html",context)





def 근로장_상세(request,pk):

    근로장 = workplace.objects.get(id=pk)
    근로자 = worker.objects.get(id=pk)
    폼 = workerModelForm(request.POST,instance=근로자)
    근로자 = worker.objects.all()   #    근로자 = worker.objects.all()



    context = {
        "근로장키" : 근로장,
        "근로자키" : 근로자,
        '폼키' : 폼
    }

    return render(request,"근로장_상세.html",context)



















