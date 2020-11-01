from django.urls import path
from .views import index,Product,Cart,Checkout,ProducDetailView,Confirmation,login,Trakking,Blog,Element,register,Contact
urlpatterns = [
    path('', index,name='home'),
    path('product', Product,name='product'),
    path('cart', Cart,name='cart'),
    path('checkout', Checkout,name='checkout'),
    path('confirmation', Confirmation,name='confirmation'),
    path('single_product', ProducDetailView,name='single_product'),
    path('login', login,name='login'),
    path('trakking', Trakking,name='trakking'),
    path('blog', Blog,name='blog'),
    path('element', Element,name='element'),
    path('register', register,name='register'),
    path('contact', Contact,name='contact'),
]
