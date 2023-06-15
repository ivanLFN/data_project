
from django.contrib import admin
from django.urls import path
from data_api.views import upload_file, get_file_list, get_column, get_data
from users.views import register, user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_file/', upload_file, name='upload_file'),
    path('files/', get_file_list, name='get-file-list'),
    path('files/<int:file_id>/columns/', get_column, name='get_column'),
    path('files/<int:file_id>/data/', get_data, name='get_data'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]
