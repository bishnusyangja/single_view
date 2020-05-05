import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import MusicalWork
from api.reconcile import reconcile_file
from api.serializer import MusicalWorkSerializer
from app.log import get_logger

logger = get_logger()


class FileUploadView(APIView):
    # parser_classes = (FileUploadParser, )

    def put(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        logger.info("this is message")
        reconcile_file(file)
        return Response(dict(success='success'), status=200)


class WorkSingleAPIView(viewsets.ModelViewSet):
    serializer_class = MusicalWorkSerializer
    queryset = MusicalWork.objects.all()

    def download_file(self):
        rows = self.get_queryset()
        filename = 'musical-work-report.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        for row in rows:
            # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
            writer.writerow(row)
        return response

    def list(self, request, *args, **kwargs):
        download = request.query_params.get('download', '')
        if download == 'download':
            return self.download_file()
        return super().list(request, *args, **kwargs)
