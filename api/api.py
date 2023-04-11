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
		nombre = self.request.query_params.get('nombre', None)
		descripcion = self.request.query_params.get('descripcion', None)
		familia = self.request.query_params.get('familia', None)
		categoria = self.request.query_params.get('categoria', None)
		subcategoria = self.request.query_params.get('subcategoria', None)
		numero_serie = self.request.query_params.get('numero_serie', None)
		estado_en_almacen = self.request.query_params.get('estado_en_almacen', None)
		fecha_alta = self.request.query_params.get('fecha_alta', None)
		responsable = self.request.query_params.get('responsable', None)
		propietario = self.request.query_params.get('propietario', None)
		localizacion = self.request.query_params.get('localizacion', None)
		fecha_ultima_accion = self.request.query_params.get('fecha_ultima_accion', None)
		codigo_rfid = self.request.query_params.get('codigo_rfid', None)
		imagen = self.request.query_params.get('imagen', None)
		estado_objeto = self.request.query_params.get('estado_objeto', None)
		fecha_baja = self.request.query_params.get('fecha_baja', None)

		queryset = Objeto.objects.all()

		if nombre is not None:
			queryset = queryset & Objeto.objects.filter(nombre__icontains=nombre)
		if descripcion is not None:
			queryset = queryset & Objeto.objects.filter(descripcion__icontains=descripcion)
		if familia is not None:
			queryset = queryset & Objeto.objects.filter(familia__icontains=familia)
		if categoria is not None:
			queryset = queryset & Objeto.objects.filter(categoria__icontains=categoria)
		if subcategoria is not None:
			queryset = queryset & Objeto.objects.filter(subcategoria__icontains=subcategoria)
		if numero_serie is not None:
			queryset = queryset & Objeto.objects.filter(numero_serie__icontains=numero_serie)
		if estado_en_almacen is not None:
			queryset = queryset & Objeto.objects.filter(estado_en_almacen=estado_en_almacen)
		if fecha_alta is not None:
			queryset = queryset & Objeto.objects.filter(fecha_alta=fecha_alta)
		if responsable is not None:
			queryset = queryset & Objeto.objects.filter(responsable=responsable)
		if propietario is not None:
			queryset = queryset & Objeto.objects.filter(propietario=propietario)
		if localizacion is not None:
			queryset = queryset & Objeto.objects.filter(localizacion__icontains=localizacion)
		if fecha_ultima_accion is not None:
			queryset = queryset & Objeto.objects.filter(fecha_ultima_accion=fecha_ultima_accion)
		if codigo_rfid is not None:
			queryset = queryset & Objeto.objects.filter(codigo_rfid__icontains=codigo_rfid)
		if imagen is not None:
			queryset = queryset & Objeto.objects.filter(imagen=imagen)
		if estado_objeto is not None:
			queryset = queryset & Objeto.objects.filter(estado_objeto=estado_objeto)
		if fecha_baja is not None:
			queryset = queryset & Objeto.objects.filter(fecha_baja=fecha_baja)

		serializer = ObjetoSerializer(queryset, many=True)
		return Response({"ok": True, "payload": serializer.data})

	def post(self, request, format=None):
		serializer = PostObjetoSerializer(data=request.data)
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
		serializer = PostObjetoSerializer(objeto, data=request.data)
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
		serializer = PostAccionSerializer(data=request.data)
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
		serializer = PostAccionSerializer(accion, data=request.data)
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
		print(fecha_registro)
		tupapi = self.request.query_params.get('tupapi', None)
		print(tupapi)
		queryset = Persona.objects.filter(fecha_registro__gt=fecha_registro)
		serializer = PersonaSerializer(queryset, many=True)

		return Response(serializer.data)


class MisObjetos(APIView):
	def get(self, request, fk, format=None):
		soy_propietario = self.request.query_params.get('soy_propietario', None)
		soy_responsable = self.request.query_params.get('soy_responsable', None)
		nombre = self.request.query_params.get('nombre', None)
		descripcion = self.request.query_params.get('descripcion', None)
		familia = self.request.query_params.get('familia', None)
		categoria = self.request.query_params.get('categoria', None)
		subcategoria = self.request.query_params.get('subcategoria', None)
		numero_serie = self.request.query_params.get('numero_serie', None)
		estado_en_almacen = self.request.query_params.get('estado_en_almacen', None)
		fecha_alta = self.request.query_params.get('fecha_alta', None)
		responsable = self.request.query_params.get('responsable', None)
		propietario = self.request.query_params.get('propietario', None)
		localizacion = self.request.query_params.get('localizacion', None)
		fecha_ultima_accion = self.request.query_params.get('fecha_ultima_accion', None)
		codigo_rfid = self.request.query_params.get('codigo_rfid', None)
		imagen = self.request.query_params.get('imagen', None)
		estado_objeto = self.request.query_params.get('estado_objeto', None)
		fecha_baja = self.request.query_params.get('fecha_baja', None)

		try:
			if soy_propietario is not None and soy_responsable is None:
				queryset = Objeto.objects.filter(propietario=fk)
			elif soy_propietario is None and soy_responsable is not None:
				queryset = Objeto.objects.filter(responsable=fk)
			else:
				queryset = Objeto.objects.filter(propietario=fk) | Objeto.objects.filter(responsable=fk)

			if nombre is not None:
				queryset = queryset & Objeto.objects.filter(nombre__icontains=nombre)
			if descripcion is not None:
				queryset = queryset & Objeto.objects.filter(descripcion__icontains=descripcion)
			if familia is not None:
				queryset = queryset & Objeto.objects.filter(familia__icontains=familia)
			if categoria is not None:
				queryset = queryset & Objeto.objects.filter(categoria__icontains=categoria)
			if subcategoria is not None:
				queryset = queryset & Objeto.objects.filter(subcategoria__icontains=subcategoria)
			if numero_serie is not None:
				queryset = queryset & Objeto.objects.filter(numero_serie__icontains=numero_serie)
			if estado_en_almacen is not None:
				queryset = queryset & Objeto.objects.filter(estado_en_almacen=estado_en_almacen)
			if fecha_alta is not None:
				queryset = queryset & Objeto.objects.filter(fecha_alta=fecha_alta)
			if responsable is not None:
				queryset = queryset & Objeto.objects.filter(responsable=responsable)
			if propietario is not None:
				queryset = queryset & Objeto.objects.filter(propietario=propietario)
			if localizacion is not None:
				queryset = queryset & Objeto.objects.filter(localizacion__icontains=localizacion)
			if fecha_ultima_accion is not None:
				queryset = queryset & Objeto.objects.filter(fecha_ultima_accion=fecha_ultima_accion)
			if codigo_rfid is not None:
				queryset = queryset & Objeto.objects.filter(codigo_rfid__icontains=codigo_rfid)
			if imagen is not None:
				queryset = queryset & Objeto.objects.filter(imagen=imagen)
			if estado_objeto is not None:
				queryset = queryset & Objeto.objects.filter(estado_objeto=estado_objeto)
			if fecha_baja is not None:
				queryset = queryset & Objeto.objects.filter(fecha_baja=fecha_baja)

			serializer = ObjetoSerializer(queryset, many=True)

			return Response({"ok": True, "payload": serializer.data})
		except:
			return Response({"ok": False, "errors": "No introdujo un ID válido para nuestra base de datos"})
