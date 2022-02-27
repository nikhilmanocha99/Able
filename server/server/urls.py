from django.contrib import admin
from django.urls import path
from authentication.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView),
    path('register/', registerView),
]
