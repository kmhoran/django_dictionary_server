from rest_framework import serializers
from dictionary.models import Word, Definition

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields=('id',
                'word')

class DefinitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Definition
        fields=('word',
                'definition',
                'part_of_speech')