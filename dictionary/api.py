from django.db.utils import Error
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from dictionary.serializers import WordSerializer, DefinitionSerializer
from dictionary.models import Word, Definition

class WordViewSet(ModelViewSet):
    # Get all words from DB
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def create(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            raise Error()


class DefinitionViewSet(ModelViewSet):
    # Get all words from DB
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer