from django.urls import path, include
from rest_framework import routers

from .api import PersonaViewSet
from .api import ObjetoViewSet
from .api import AccionViewSet


router = routers.DefaultRouter()

router.register('api/persona', PersonaViewSet, 'persona')
router.register('api/objeto', ObjetoViewSet, 'objeto')
router.register('api/accion', AccionViewSet, 'accion')

urlpatterns = [
	path('', include(router.urls)),
]
