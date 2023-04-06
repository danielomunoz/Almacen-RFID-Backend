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
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

	def delete(self, request, pk, format=None):
		persona = self.get_object(pk)
		if persona == None:
			return Response({"ok": False, "errors": "No se encontró una persona con ese ID en base de datos"})
		persona.delete()
		return Response({"ok": True, "payload": "Persona borrada satisfactoriamente, id: {}".format(pk)})



class Objeto_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		objeto = Objeto.objects.all()
		serializer = ObjetoSerializer(objeto, many=True)
		return Response({"ok": True, "payload": serializer.data})

	def post(self, request, format=None):
		serializer = ObjetoSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

class Objeto_APIView_Detail(APIView):
	def get_object(self, pk):
		try:
			return Objeto.objects.get(id=pk)
		except Objeto.DoesNotExist:
			return None

	def get(self, request, pk, format=None):
		objeto = self.get_object(pk)
		if objeto == None:
			return Response({"ok": False, "errors": "No se encontró un objeto con ese ID en base de datos"})
		serializer = ObjetoSerializer(objeto)
		return Response({"ok": True, "payload": serializer.data})

	def put(self, request, pk, format=None):
		objeto = self.get_object(pk)
		if objeto == None:
			return Response({"ok": False, "errors": "No se encontró un objeto con ese ID en base de datos"})
		serializer = ObjetoSerializer(objeto, data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

	def delete(self, request, pk, format=None):
		objeto = self.get_object(pk)
		if objeto == None:
			return Response({"ok": False, "errors": "No se encontró una objeto con ese ID en base de datos"})
		objeto.delete()
		return Response({"ok": True, "payload": "Objeto borrado satisfactoriamente, id: {}".format(pk)})


class Accion_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		accion = Accion.objects.all()
		serializer = AccionSerializer(accion, many=True)
		return Response({"ok": True, "payload": serializer.data})

	def post(self, request, format=None):
		serializer = AccionSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

class Accion_APIView_Detail(APIView):
	def get_object(self, pk):
		try:
			return Accion.objects.get(id=pk)
		except Accion.DoesNotExist:
			return None

	def get(self, request, pk, format=None):
		accion = self.get_object(pk)
		if accion == None:
			return Response({"ok": False, "errors": "No se encontró una accion con ese ID en base de datos"})
		serializer = AccionSerializer(accion)
		return Response({"ok": True, "payload": serializer.data})

	def put(self, request, pk, format=None):
		accion = self.get_object(pk)
		if accion == None:
			return Response({"ok": False, "errors": "No se encontró una accion con ese ID en base de datos"})
		serializer = AccionSerializer(accion, data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

	def delete(self, request, pk, format=None):
		accion = self.get_object(pk)
		if accion == None:
			return Response({"ok": False, "errors": "No se encontró una accion con ese ID en base de datos"})
		accion.delete()
		return Response({"ok": True, "payload": "Accion borrada satisfactoriamente, id: {}".format(pk)})


class Detector_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		detector = Detector.objects.all()
		serializer = DetectorSerializer(detector, many=True)
		return Response({"ok": True, "payload": serializer.data})

	def post(self, request, format=None):
		serializer = DetectorSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

class Detector_APIView_Detail(APIView):
	def get_object(self, pk):
		try:
			return Detector.objects.get(id=pk)
		except Detector.DoesNotExist:
			return None

	def get(self, request, pk, format=None):
		detector = self.get_object(pk)
		if detector == None:
			return Response({"ok": False, "errors": "No se encontró un detector con ese ID en base de datos"})
		serializer = DetectorSerializer(detector)
		return Response({"ok": True, "payload": serializer.data})

	def put(self, request, pk, format=None):
		detector = self.get_object(pk)
		if detector == None:
			return Response({"ok": False, "errors": "No se encontró un detector con ese ID en base de datos"})
		serializer = DetectorSerializer(detector, data=request.data)
		if not serializer.is_valid():
			return Response({"ok": False, "errors": serializer.errors})
		serializer.save()
		return Response({"ok": True, "payload": serializer.data})

	def delete(self, request, pk, format=None):
		detector = self.get_object(pk)
		if detector == None:
			return Response({"ok": False, "errors": "No se encontró un detector con ese ID en base de datos"})
		detector.delete()
		return Response({"ok": True, "payload": "Detector borrado satisfactoriamente, id: {}".format(pk)})



class PersonaPorFecha(APIView):
	def get(self, request, format=None):
		
		fecha_registro = self.request.query_params.get('fecha', None)
		queryset = Persona.objects.filter(fecha_registro__gt=fecha_registro)
		serializer = PersonaSerializer(queryset, many=True)

		return Response(serializer.data)
