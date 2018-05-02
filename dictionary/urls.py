from dictionary.api import WordViewSet, DefinitionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'word', WordViewSet)
router.register(r'definition', DefinitionViewSet)

urlpatterns = router.urls