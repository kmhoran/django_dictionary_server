from rest_framework.viewsets import ModelViewSet

from dictionary.serializers import WordSerializer, DefinitionSerializer
from dictionary.models import Word, Definition

class WordViewSet(ModelViewSet):
    # Get all words from DB
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class DefinitionViewSet(ModelViewSet):
    # Get all words from DB
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer