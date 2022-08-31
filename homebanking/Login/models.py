from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractUser)
from Clientes.models import Cliente
from Empleados.models import Empleado

class   MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Hola, debes ingresar DNI')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email, password=None):
        user = self.create_user(
            username,
            password=password,
            email=email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractUser):
    id_empleado=models.OneToOneField(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    id_cliente=models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    username=models.CharField(max_length=50,blank=True,null=True, unique=True,verbose_name = "DNI")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    # def __str__(self):
    #     return self.id


