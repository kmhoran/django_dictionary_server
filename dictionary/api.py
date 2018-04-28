from rest_framework.generics import ListAPIView

from dictionary.serializers import WordSerializer
from dictionary.models import Word

class WordApi(ListAPIView):
    # Get all words from DB
    queryset = Word.objects.all()
    serializer_class = WordSerializer