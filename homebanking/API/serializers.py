from rest_framework import serializers
from Prestamos.models import Prestamo
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Login.models import MyUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
        model = MyUser
        fields = ['id_cliente','username','email', 'date_joined']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','DNI','email','fecha_de_nac','tipo_cliente','usuario']


class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    id_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo', 'tipo', 'total', 'id_cliente']



class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    id_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
    class Meta:
        model = Cuenta
        fields = ['id_cliente','balance','iban', 'tipo_cuenta']