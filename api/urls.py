from django.urls import path, include
# from rest_framework import routers

from .api import *


# router = routers.DefaultRouter()

# router.register('api/persona', PersonaViewSet, 'persona')
# router.register('api/objeto', ObjetoViewSet, 'objeto')
# router.register('api/accion', AccionViewSet, 'accion')

urlpatterns = [
	# path('', include(router.urls)),
	path('api/persona', Persona_APIView.as_view()),
	path('api/persona/<int:pk>/', Persona_APIView_Detail.as_view()),
	path('api/personaPorFecha', PersonaPorFecha.as_view()),
]
