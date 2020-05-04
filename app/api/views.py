from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import MusicalWork
from api.reconcile import reconcile_file
from api.serializer import MusicalWorkSerializer


class FileUploadView(APIView):
    # parser_classes = (FileUploadParser, )

    def put(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        reconcile_file(file)
        return Response(dict(success='success'), status=200)


class WorkSingleAPIView(viewsets.ModelViewSet):
    serializer_class = MusicalWorkSerializer
    queryset = MusicalWork.objects.all()

    def download_file(self):
        return Response(dict(success='success'), status=200)

    def list(self, request, *args, **kwargs):
        download = request.query_params.get('download', '')
        if download == 'download':
            return self.download_file()
        return super().list(request, *args, **kwargs)
