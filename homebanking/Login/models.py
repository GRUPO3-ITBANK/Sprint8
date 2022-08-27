from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractUser)
from Clientes.models import Cliente

class   MyUserManager(BaseUserManager):
    def create_user(self, username, id_cliente, password=None):
        if not username:
            raise ValueError('Hola, debes ingresar DNI')
        user = self.model(
            username=username,
            id_cliente=id_cliente,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,id_cliente, password=None):
        user = self.create_user(
            username,
            password=password,
            id_cliente=id_cliente,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractUser):
    id_cliente=models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    username=models.CharField(max_length=50,blank=True,null=True, unique=True,verbose_name = "DNI")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id_cliente']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        if self.is_admin == True :  
            return "(Superuser) " + self.username
        return "(Cliente comun) " + self.username


