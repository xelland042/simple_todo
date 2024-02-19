from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TodoModelViewSet

router = DefaultRouter()
router.register(r'', TodoModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
