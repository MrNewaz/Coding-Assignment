from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# Parent Route
# Get & Post /parent
# Put & Delete /parent/<pk>
router.register('parent', ParentViewSet)


# Parent Route
# Get & Post /child
# Put & Delete /child/<pk>
router.register('child', ChildViewSet)

urlpatterns = router.urls
