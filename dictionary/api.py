from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from dictionary.serializers import WordSerializer, DefinitionSerializer
from dictionary.models import Word, Definition

class WordViewSet(ModelViewSet):
    # Get all words from DB
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def create(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
           

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DefinitionViewSet(ModelViewSet):
    # Get all words from DB
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer