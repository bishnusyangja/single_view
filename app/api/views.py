from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


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
                headers = [item.upper().strip() for item in values]
                try:
                    idx = headers.index('ISWC')
                except ValueError:
                    idx = -1
                except Exception as exc:
                    print('IndexExcep', exc)
                    idx = -1
                print(idx, headers)
            else:
                print(values)
                if idx == -1:
                    break
                key_item = values[idx]
                if key_item in headers:
                    rows[key_item] = {header: values[j] for j, header in enumerate(headers)}
        print(rows)
        return Response(dict(success='success'), status=200)