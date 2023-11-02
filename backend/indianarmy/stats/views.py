from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from rest_framework.parsers import MultiPartParser
import openpyxl
from .serializers import *
import traceback
from rest_framework.response import Response
from django.db.models import Count
import json


class ExcelUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        try:
            print(request.FILES)
            excel_file = request.FILES.get('excel_file')

            
            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active

            # header_row = sheet[1]
            # column_name_to_index = {cell.value: cell.column for cell in header_row}

            for row in sheet.iter_rows(min_row=2, values_only=True):  
                gender = row[2]
                salary = row[3]
                city = row[4]
                task_force = row[5]

                employee_data = {
                    "gender": gender,
                    "salary": salary,
                    "city": city,
                    "task_force": task_force,
                }
            
                employeeserializer = EmployeeSerializer(data=employee_data)
                if employeeserializer.is_valid():
                    employeeserializer.save()
                    print("ok")

                else:
                    print(employeeserializer.errors)


            return Response({'message': 'Data has been ingested into the database'})
        except Exception as e:
            
            traceback.print_exc()  
            return Response({'error': str(e)}, status=400)


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.filter(gender='Male')
    serializer_class = EmployeeSerializer


class SortByGenderListView(APIView):
    def get(self, request):
        male_count = EmployeeModel.objects.filter(gender='Male').count()
        female_count = EmployeeModel.objects.filter(gender='Female').count()
        return Response({"male": male_count, "female": female_count})
    
    
class SortByCityListView(APIView):
    def get(self, request):
        employee_count_by_city = EmployeeModel.objects.values('city').annotate(employee_count=Count('id'))

        result = {'data':[{'city': city_data['city'], 'count': city_data['employee_count']} for city_data in employee_count_by_city]}

        return Response(result)
    

class SortByTaskForceListView(APIView):
    def get(self, request):
        employee_count_by_task_force = EmployeeModel.objects.values('task_force').annotate(employee_count=Count('id'))

        result = {'data':[{'task force': data['task_force'], 'count': data['employee_count']} for data in employee_count_by_task_force]}

        return Response(result)
    