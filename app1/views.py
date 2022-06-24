from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'name':'yash'}
    return render(request,'hai.html',context=d)

def hello(request):
    d={'a':20, 'b':25}
    return render(request,'hai.html',context=d)

def yash(request):
    d={'a':30, 'b':25, 'c':35}
    return render(request,'hai.html',context=d)

def harry(request):
    d={'a':35, 'b':54, 'c':45}
    return render(request,'hai.html',context=d)

def yaswanth(request):
    d={'name':'haritha'}
    return render(request,'looping.html',context=d)
