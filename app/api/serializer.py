from rest_framework import serializers

from api.models import MusicalWork


class MusicalWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = MusicalWork
        fields = ('pk', 'title', 'contributers', 'iswc', 'item_id')