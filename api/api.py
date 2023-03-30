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

class PersonaPorFecha(APIView):
	def get(self, request, format=None):
		
		fecha_registro = self.request.query_params.get('fecha', None)
		queryset = Persona.objects.filter(fecha_registro__gt=fecha_registro)
		serializer = PersonaSerializer(queryset, many=True)

		return Response(serializer.data)
