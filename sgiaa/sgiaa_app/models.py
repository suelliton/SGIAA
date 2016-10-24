from django.db import models
from django.utils import timezone


from django.db import models


class Bairro(models.Model):
    id = models.IntegerField(primary_key=True)
    bairro_risco = models.IntegerField()
    nome = models.CharField(max_length=25)
    taxa_eclusao = models.FloatField()
    total_larvas = models.IntegerField()
    total_ovos = models.IntegerField()
    coordenadas = models.CharField(default='',max_length=80)
    id_regiao = models.ForeignKey('Regiao', models.DO_NOTHING, db_column='id_regiao', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Bairro'


class Palheta(models.Model):
    id = models.IntegerField(primary_key=True)
    coordenada_x = models.IntegerField()
    coordenada_y = models.IntegerField()
    eclosao_palheta = models.IntegerField()
    ido = models.FloatField()
    ipo = models.FloatField()
    ovos_palheta = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Palheta'


class Regiao(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=10)
    regiao_risco = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Regiao'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    cpf = models.CharField(max_length=14)
    login = models.CharField(max_length=30)
    nome = models.CharField(max_length=30)
    senha = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission',models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'
