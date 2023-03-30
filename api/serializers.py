from rest_framework import serializers

from .models import Persona
from .models import Objeto
from .models import Accion

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Persona
		fields = '__all__'

class ObjetoSerializer(serializers.ModelSerializer):
	responsable = PersonaSerializer()
	propietario = PersonaSerializer()
	class Meta:
		model = Objeto
		fields = '__all__'

class AccionSerializer(serializers.ModelSerializer):
	persona = PersonaSerializer()
	objeto = ObjetoSerializer()
	class Meta:
		model = Accion
		fields = '__all__'
