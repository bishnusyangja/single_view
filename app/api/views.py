from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import MusicalWork


class FileUploadView(APIView):
    # parser_classes = (FileUploadParser, )

    def put(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        lines = file_obj.readlines()
        rows = {}
        idx = -1
        headers = []
        for i, item in enumerate(lines):
            values = item.decode('utf-8').strip('\n').split(',')
            if i == 0:
                headers = [item.lower().strip() for item in values]
                print(headers)
                try:
                    idx = headers.index('iswc')
                except ValueError:
                    idx = -1
                except Exception as exc:
                    print('IndexExcep', exc)
                    idx = -1
            else:
                if idx == -1:
                    break
                key_item = values[idx]
                if key_item in headers:
                    obj = MusicalWork(**{f'item_{header}' if header == 'id' else header: values[j]
                                                    for j, header in enumerate(headers)})
                    rows[key_item] = obj

        return Response(dict(success='success'), status=200)