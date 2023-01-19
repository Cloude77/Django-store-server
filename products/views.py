from django.shortcuts import render, HttpResponse

# Create your views here.
# controllers (functions)


def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')