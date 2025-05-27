from rest_framework import serializers
from .models import (
    Usuario, Curso, Interesa, Matricula, Material,
    Tarea, EntregaTarea, Foro, MensajeForo
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class InteresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesa
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class EntregaTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntregaTarea
        fields = '__all__'

class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = '__all__'

class MensajeForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeForo
        fields = '__all__'
