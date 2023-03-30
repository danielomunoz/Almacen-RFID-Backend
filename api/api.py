from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Persona
from .models import Objeto
from .models import Accion

from .serializers import PersonaSerializer
from .serializers import ObjetoSerializer
from .serializers import AccionSerializer


class PersonaViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = PersonaSerializer

class ObjetoViewSet(viewsets.ModelViewSet):
	queryset = Objeto.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = ObjetoSerializer

class AccionViewSet(viewsets.ModelViewSet):
	queryset = Accion.objects.all()
	permission_classes = [permissions.AllowAny]
	serializer_class = AccionSerializer
