from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from data_api.models import DataFile
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from django.contrib.auth.models import User




@csrf_exempt
@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        data_file = DataFile.objects.create(main_file=file)
        return JsonResponse({'message': 'Файл успешно загружен.'})
    return JsonResponse({'message': 'Ошибочный запрос.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_file_list(request):
    data_files = DataFile.objects.all()
    files = [{'id': data_file.id, 'filename': data_file.main_file.name} for data_file in data_files]
    return JsonResponse({'files': files})



# curl -X GET -H "Authorization: Token ваш_токен" http://127.0.0.1:8000/files/2/columns/
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_column(request, file_id):
    try:
        data_file = DataFile.objects.get(id=file_id)
        df = pd.read_csv(data_file.main_file.path)
        columns = list(df.columns)
        return Response({'columns': columns})
    except DataFile.DoesNotExist:
        return Response({'message': 'Файл не найден'})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_data(request, file_id):
    try:
        data_file = DataFile.objects.get(id=file_id)
        df = pd.read_csv(data_file.main_file.path)

        filters = request.GET.getlist('filter')

        if filters:
            for f in filters:
                column, value = f.split('=')
                df = df[df[column] == value]
        
        sort_by = request.GET.get('sort_by')
        if sort_by:
            df = df.sort_values(by=sort_by)


        data = df.to_dict(orient='records')
        return Response(data)
    except DataFile.DoesNotExist:
        return Response({'message': 'Файл не найден.'})
