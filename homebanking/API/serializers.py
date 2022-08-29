from rest_framework import serializers
from Prestamos.models import Prestamo
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Login.models import MyUser
from Tarjetas.models import Tarjeta
from Empleados.models import Empleado
from Prestamos.models import Prestamo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
        model = MyUser
        fields = ['id_cliente','username','email', 'date_joined']

class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','fecha_contratacion','DNI']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','DNI','email','fecha_de_nac','tipo_cliente']


class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    ID_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo', 'tipo', 'total', 'ID_cliente']


class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    ID_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
    class Meta:
        model = Cuenta
        fields = ['ID_cliente','balance','iban', 'tipo_cuenta']

class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    ID_cliente = serializers.HyperlinkedRelatedField(view_name='cliente-detail',read_only=True)
    class Meta:
        model = Tarjeta
        fields = ['numero','cvv','fecha_otorgamiento', 'fecha_vencimiento','tipo','marca','ID_cliente']

