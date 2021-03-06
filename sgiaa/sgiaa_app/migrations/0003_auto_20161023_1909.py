# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgiaa_app', '0002_auto_20161020_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='authgrouppermissions',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthGroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authgrouppermissions',
            name='permission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthPermission'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.DjangoContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authusergroups',
            name='group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthGroup'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authusergroups',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authuseruserpermissions',
            name='permission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthPermission'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authuseruserpermissions',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthUser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bairro',
            name='coordenadas',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='bairro',
            name='id_regiao',
            field=models.ForeignKey(blank=True, db_column='id_regiao', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.Regiao'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sgiaa_app.AuthUser'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='authgrouppermissions',
            unique_together=set([('group', 'permission')]),
        ),
        migrations.AlterUniqueTogether(
            name='authpermission',
            unique_together=set([('content_type', 'codename')]),
        ),
        migrations.AlterUniqueTogether(
            name='authusergroups',
            unique_together=set([('user', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='authuseruserpermissions',
            unique_together=set([('user', 'permission')]),
        ),
        migrations.AlterUniqueTogether(
            name='djangocontenttype',
            unique_together=set([('app_label', 'model')]),
        ),
    ]
