from django import forms
from .models import Matricula, Usuario, Curso

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['id_nodo_estudiante', 'id_curso', 'comprobante_pago']

    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        self.fields['id_nodo_estudiante'].queryset = Usuario.objects.filter(rol='Estudiante')

class AsignarProfesorForm(forms.Form):
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.filter(id_nodo_profesor__isnull=True),
        label="Curso sin profesor asignado"
    )
    profesor = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(rol='Profesor'),
        label="Profesor"
    )