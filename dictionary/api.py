from rest_framework.generics import ListAPIView

from dictionary.serializers import WordSerializer, DefinitionSerializer
from dictionary.models import Word, Definition

class WordApi(ListAPIView):
    # Get all words from DB
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class DefinitionApi(ListAPIView):
    # Get all words from DB
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer