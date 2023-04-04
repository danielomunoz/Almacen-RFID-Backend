from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *

from .serializers import *

class Persona_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		persona = Persona.objects.all()
		serializer = PersonaSerializer(persona, many=True)
		return Response({"ok": True, "payload": serializer.data})

	def post(self, request, format=None):
		serializer = PersonaSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

class Persona_APIView_Detail(APIView):
	def get_object(self, pk):
		try:
			return Persona.objects.get(id=pk)
		except Persona.DoesNotExist:
			return None

	def get(self, request, pk, format=None):
		persona = self.get_object(pk)
		if persona == None:
			return Response({"ok": False, "errors": "No se encontró una persona con ese ID en base de datos"})
		serializer = PersonaSerializer(persona)
		return Response({"ok": True, "payload": serializer.data})

	def put(self, request, pk, format=None):
		persona = self.get_object(pk)
		if persona == None:
			return Response({"ok": False, "errors": "No se encontró una persona con ese ID en base de datos"})
		serializer = PersonaSerializer(persona, data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "error": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

	def delete(self, request, pk, format=None):
		persona = self.get_object(pk)
		if persona == None:
			return Response({"ok": False, "errors": "No se encontró una persona con ese ID en base de datos"})
		persona.delete()
		return Response({"ok": True, "payload": "Persona borrada satisfactoriamente, id: {}".format(pk)})


# class PersonaViewSet(viewsets.ModelViewSet):
# 	queryset = Persona.objects.all()
#	permission_classes = [permissions.AllowAny]
#	serializer_class = PersonaSerializer

# class ObjetoViewSet(viewsets.ModelViewSet):
#	queryset = Objeto.objects.all()
#	permission_classes = [permissions.AllowAny]
#	serializer_class = ObjetoSerializer

# class AccionViewSet(viewsets.ModelViewSet):
#	queryset = Accion.objects.all()
#	permission_classes = [permissions.AllowAny]
#	serializer_class = AccionSerializer

class PersonaPorFecha(APIView):
	def get(self, request, format=None):
		
		fecha_registro = self.request.query_params.get('fecha', None)
		queryset = Persona.objects.filter(fecha_registro__gt=fecha_registro)
		serializer = PersonaSerializer(queryset, many=True)

		return Response(serializer.data)
