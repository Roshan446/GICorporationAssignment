from django.urls import path
from .views import *
urlpatterns = [
path('csv_file_upload/', CsvExtractorView.as_view(), name="csv_file_upload")

]