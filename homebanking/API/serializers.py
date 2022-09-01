from rest_framework import serializers
from Prestamos.models import Prestamo
from Clientes.models import Cliente
from Cuentas.models import Cuenta
from Login.models import MyUser
from Tarjetas.models import Tarjeta
from Empleados.models import Empleado
from Prestamos.models import Prestamo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id_cliente','username','email', 'date_joined']

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['nombre','apellido','fecha_contratacion','DNI']


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','DNI','email','fecha_de_nac','tipo_cliente','direccion','sucursal']

class ClienteSerializerDireccion(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['direccion']

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo', 'tipo', 'total', 'ID_cliente','sucursal']


class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['ID_cliente_id','balance','iban', 'tipo_cuenta']


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ['numero','cvv','fecha_otorgamiento', 'fecha_vencimiento','tipo','marca','ID_cliente']

