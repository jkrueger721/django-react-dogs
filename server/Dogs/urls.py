from .views import DogViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', DogViewSet)
urlpatterns = router.urls