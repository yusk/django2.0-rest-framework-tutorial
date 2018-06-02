from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

schema_view = get_schema_view(title='Pastebin API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('snippets.urls')),
    path('quickstart/', include(router.urls)),
    path('schema/', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
