from django.shortcuts import render

# Create your views here.
def jinja_operations(request):
    d={'a':300,'b':400,'c':4000}
    return render(request,'jinja_operations.html',context=d)