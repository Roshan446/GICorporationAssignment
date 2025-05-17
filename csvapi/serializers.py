from rest_framework.serializers import Serializer
from rest_framework import serializers

    
    
class CsvUploadSerializer(Serializer):
    csv_file = serializers.FileField()    
    
    def validate(self, attrs):
        csv_file = attrs.get("csv_file")
        if csv_file: 
            if  csv_file.content_type !=  'text/csv':
                raise serializers.ValidationError("Only CSV file formats are allowed")
        return super().validate(attrs)
    
    
