from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('Courses',views.Courses, name='Courses'),
    path('Learn',views.Learn, name='Learn'),
    path('Tests',views.Tests, name='Tests'),
    path('connect',views.Connect, name='connect'),
    path('base',views.base, name='base'),
    path('checkout',views.checkout, name='checkout'),
    path('footer',views.footer, name='footer'),
    path('navbar',views.Connect, name='navbar'),

]