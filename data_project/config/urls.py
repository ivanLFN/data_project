
from django.contrib import admin
from django.urls import path
from data_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('files/', views.get_file_list, name='get-file-list'),
    path('files/<int:file_id>/columns/', views.get_column, name='get_column'),
    path('files/<int:file_id>/data/', views.get_data, name='get_data'),
]
