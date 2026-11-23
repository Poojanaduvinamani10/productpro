from django.shortcuts import render , redirect
from myapp.models import Product
from myapp.forms import ProductForm

def view1(request):
    d=Product.objects.all()
    search= request.GET.get('search')
    if search:
        d=Product.objects.filter(name__icontains=search)
    
    return render(request,'product.html',{'prod':d})

def createpro(request):
    f=ProductForm()
    if request.method=="POST":
        f=ProductForm(request.POST,request.FILES)
        if f.is_valid():
            f.save(commit=True)
        return redirect('display')
    a={'form':f}
    return render(request,'insert.html',a)

def updateproduct(request,id):
    p= Product.objects.get(id=id)
    f= ProductForm(instance=p)
    if request.method=="POST":
            f=ProductForm(request.POST,request.FILES,instance=p)
            if f.is_valid():
                f.save()
            return redirect('display')
    a={'form':f}
    return render(request,'insert.html',a)

def deleteproduct(request,id):
     p= Product.objects.get(id=id)
     p.delete()
     return redirect ('display')
