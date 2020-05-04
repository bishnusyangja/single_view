from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class FileUploadView(APIView):
    # parser_classes = (FileUploadParser, )

    def dispatch(self, request, *args, **kwargs):
        print("at dispatch")
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("at put method")
        # import pdb; pdb.set_trace()
        # print("file printing", self.request.data)
        file_obj = request.FILES.get('file')
        lines = file_obj.readlines()
        rows = {}
        idx = -1
        for i, item in enumerate(lines):
            values = item.decode('utf-8').strip('\n').split(',')
            if i == 1:
                headers = [item.upper().strip() for item in values]
                try:
                    idx = headers.index('ISWC')
                except ValueError:
                    idx = -1
                except Exception as exc:
                    print('IndexExcep', exc)
                    idx = -1
            else:
                if idx == -1:
                    break
                'ISWC'
                rows[headers[0]]
            print(item.decode('utf-8').strip('\n').split(','))
        return Response(dict(success='success'), status=200)