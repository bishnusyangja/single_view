import csv

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from api.models import MusicalWork
from api.reconcile import reconcile_file
from api.serializer import MusicalWorkSerializer
from app.log import get_logger

logger = get_logger()


class FileUploadView(APIView):
    authentication_classes = []

    def put(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        status = reconcile_file(file)
        if status:
            return Response(dict(success='success'), status=200)
        else:
            return Response(dict(success='either file type or file content is not supported'), status=400)


class WorkSingleAPIView(GenericViewSet, mixins.ListModelMixin):
    authentication_classes = []
    serializer_class = MusicalWorkSerializer
    queryset = MusicalWork.objects.all()

    def download_file(self):
        rows = self.get_queryset()
        filename = 'musical-work-report.csv'
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        writer = csv.writer(response)
        writer.writerow(['Title', 'Contributors', 'ISWC', 'ID'])
        for row in rows:
            writer.writerow([row.title, row.contributors, row.iswc, row.item_id])
        return response

    def paginate_queryset(self, queryset):
        page_size = self.request.query_params.get('page_size')
        if page_size:
            self.paginator.page_size = page_size
        return super().paginate_queryset(queryset)

    def list(self, request, *args, **kwargs):
        download = request.query_params.get('download', '')
        if download == 'download':
            return self.download_file()
        return super().list(request, *args, **kwargs)
