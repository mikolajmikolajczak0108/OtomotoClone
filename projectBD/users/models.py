


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import psycopg2
from django.conf import settings
from django.utils import timezone


def get_next_user_id():
    conn = psycopg2.connect(
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD']
    )
    cur = conn.cursor()
    cur.execute('SELECT get_next_user_id()')
    next_id = cur.fetchone()[0]
    cur.close()
    conn.close()

    return next_id


class MyUserManager(BaseUserManager):


    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)





class MyUser(AbstractBaseUser):
    id = models.IntegerField(primary_key=True, default=get_next_user_id())
    email = models.EmailField(unique=True)
    nick = models.CharField(max_length=100, blank=True)
    # password = models.CharField(max_length=100, blank=True) # this field should not be here
    f_name = models.CharField(max_length=30, blank=True)
    l_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    offers_count = models.IntegerField(default=0)
    account_creation_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField()
    role_id = models.IntegerField(default=2)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        db_table = 'User'
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser
