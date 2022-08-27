from django import forms
from .models import MyUser
from Clientes.models import Cliente

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('id_cliente',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_cliente'].queryset = Cliente.objects.all()
