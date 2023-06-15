from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from data_api.models import DataFile
import pandas as pd


@csrf_exempt
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        data_file = DataFile.objects.create(main_file=file)
        return JsonResponse({'message': 'Файл успешно загружен.'})
    return JsonResponse({'message': 'Ошибочный запрос.'})

def get_file_list(request):
    data_files = DataFile.objects.all()
    files = [{'id': data_file.id, 'filename': data_file.main_file.name} for data_file in data_files]
    return JsonResponse({'files': files})



