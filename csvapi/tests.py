from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.
from django.core.files.uploadedfile import SimpleUploadedFile


class TestCaseSetup(APITestCase):
    
    def setup(self):
        return super().setUp()



class RunViewTest(TestCaseSetup):
    
    def test_csv_file_upload(self):
        url = reverse('csv_file_upload')
        csv_content = b"name,email,age\nJim Jimbo,jimmy@firenet.com,30\nrandy cooper,randy@lis.com,25\nrandy cooper,randylis.com,121\n  ,randylis@gmail.com,121\nrandy cooper,randylis@com,121"
        csv_file = SimpleUploadedFile('test.csv', csv_content ,content_type="text/csv")
        res = self.client.post(url,  data={"csv_file":csv_file}, format='multipart')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data["missed"],3)
        self.assertEqual(res.data["created"],2)
