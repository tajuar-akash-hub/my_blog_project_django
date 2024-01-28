
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='homepage'),
    path('category/<slug:catagory_slug>/', views.home,name='category_wise_post'),
    path('author/', include("author.urls")),
    path('catagory/', include("catagories.urls")),
    path('posts/', include("posts.urls")),
]
