from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import MusicalWork
from api.reconcile import reconcile_file


class FileUploadView(APIView):
    # parser_classes = (FileUploadParser, )

    def put(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        reconcile_file(file)
        return Response(dict(success='success'), status=200)