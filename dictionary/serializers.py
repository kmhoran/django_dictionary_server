from rest_framework import serializers
from dictionary.models import Word, Definition


class DefinitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Definition
        fields=('word',
                'definition',
                'part_of_speech')

class WordSerializer(serializers.ModelSerializer):
    definition_set = DefinitionSerializer(required=False, read_only=True, many=True)
    class Meta:
        model = Word
        fields=('id',
                'name',
                'definition_set')

        


