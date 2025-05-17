from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd 
from csvapi.serializers import CsvUploadSerializer
import re 
from .models import *




class CsvExtractorView(APIView):
    def post(self, request, *args, **kwargs):
        
        email_validator = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        created_row = 0
        missed_row = 0
        csv_serailizer = CsvUploadSerializer(data=request.data)
        if csv_serailizer.is_valid():
            csv_file = csv_serailizer.validated_data['csv_file']

            data = pd.read_csv(csv_file)
            errors_records = []


            for index, row in data.iterrows():
                errors = []

                name = row["name"]
                email = row["email"]
                try:
                    age = int(row["age"])
                except:
                    errors.append("Invalid age format, must be an integer from 0 to 120")
                    age = row["age"]

                    
                
                if (not name.strip()  or not 
                    re.match(email_validator,email) or not 
                    isinstance(age, int) or not 0<=int(age)<=120) or Users.objects.filter(email=email).exists():
                    missed_row +=1
                    if not name.strip():
                        errors.append("Name cannot be empty and only white spaces are not allowed")

                    if not  re.match(email_validator,email): 
                        errors.append("Invalid email format")

                    if  Users.objects.filter(email=email).exists():
                        errors.append("The email exists in our database")
            
                    if not 0<=int(age)<=120:    
                        errors.append("Invalid age")
                    
                    
                    errors_records.append(
                        {
                            "name":name,
                            "email":email,
                            "age":age ,
                            "error":errors if errors else "N/A"
                        }
                    )
                else:
                    Users.objects.create(
                        name = name,
                        age = age,
                        email = email
                    )
                    created_row+=1
                    
            records = {"message":"Successfully parsed csv file to data", "created":created_row, "missed":missed_row, "errors":errors_records}
            return Response(data=records, status=status.HTTP_201_CREATED)
        else:
            return Response(data={"message":"There is an error with the upload, please try again"}, status=status.HTTP_400_BAD_REQUEST)


                
        
                        
                        
                    
                    
                    
                    
                
        
        
        