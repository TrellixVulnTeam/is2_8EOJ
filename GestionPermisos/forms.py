from django import forms

class crearRolForm(forms.Form):
    Rol = forms.CharField()
    OPTIONS = (
        ("add", "Agregar"),
        ("delete", "Borrar"),
        ("change","Modificar"),
        ("view","Ver"),
    )
    Historia = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    Proyecto = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    Sprint = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=OPTIONS)


#class asignarRolForm(forms.Form):
 #   nombreUsuario = forms.CharField(30)
    #roles = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = )