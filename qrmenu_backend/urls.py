from django.contrib import admin
from django.urls import path , include

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',include('rest_framework.urls')),

    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),

    path('',include('core.urls')),

]
