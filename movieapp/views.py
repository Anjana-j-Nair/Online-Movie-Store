from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import movies
from .forms import form_movie

# Create your views here.
def ms(request):
    movie=movies.objects.all()
    context={'movie_list':movie}
    return render(request,"index.html",context)
def detail(request,movie_id):
    m=movies.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':m})
def addmovie(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('desc')
        y=request.POST.get('year')#fetching
        i=request.FILES['img']
        m=movies(name=n,desc=d,year=y,img=i) # add to database first one is the db feild name & second is the variable name
        m.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    mov=movies.objects.get(id=id)
    form=form_movie(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render (request,'edit.html',{'f':form,'m':mov})
def delete(request,id):
    if request.method=='POST':
        mov=movies.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')