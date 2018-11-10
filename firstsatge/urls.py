from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MyMeinView.as_view(), name='main_view'),
    path('detail/<str:alias><int:globalId>/', views.MyDetailView.as_view(), name='detail'),
    path('api/', views.MyApi.as_view(), name='api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)