from rest_framework.routers import DefaultRouter
from .views import *

"""
All routes for Parent User:

Route : 'parent/'
 - Get(list) 
 - Post(create) 

Route : 'parent/<pk>/'
 - Get(retrieve)
 - Put(update)
 - Patch(partial_update)
 - Delete(destroy)

 All routes for Child User:

Route : 'child/'
 - Get(list) 
 - Post(create) 
 
Route : 'child/<pk>/'
 - Get(retrieve)
 - Put(update)
 - Patch(partial_update)
 - Delete(destroy)
"""

router = DefaultRouter()


router.register('parent', ParentViewSet)

router.register('child', ChildViewSet)

urlpatterns = router.urls
