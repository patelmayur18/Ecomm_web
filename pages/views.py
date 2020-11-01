from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def Product(request):
    return render(request,'pages/category.html')


def Cart(request):
    return render(request,'pages/cart.html')


def Checkout(request):
    return render(request,'pages/checkout.html')

def Confirmation(request):
    return render(request,'pages/confirmation.html')

def ProducDetailView(request):
    return render(request,'pages/single-product.html')

def login(request):
    return render(request,'pages/login.html')

def Trakking(request):
    return render(request,'pages/tracking.html')

def Blog(request):
    return render(request,'pages/blog.html')

def Element(request):
    return render(request,'pages/elements.html')

def register(request):
    return render(request,'pages/register.html')   

def Contact(request):
    return render(request,'pages/contact.html')                   