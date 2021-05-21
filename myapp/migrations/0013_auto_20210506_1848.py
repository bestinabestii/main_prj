# Generated by Django 3.2 on 2021-05-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_user_login_u_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer_details',
            old_name='addr1',
            new_name='addr',
        ),
        migrations.RemoveField(
            model_name='volunteer_details',
            name='addr2',
        ),
        migrations.RemoveField(
            model_name='volunteer_details',
            name='addr3',
        ),
        migrations.RemoveField(
            model_name='volunteer_details',
            name='district_id',
        ),
        migrations.RemoveField(
            model_name='volunteer_details',
            name='id_name',
        ),
        migrations.RemoveField(
            model_name='volunteer_details',
            name='id_no',
        ),
        migrations.AddField(
            model_name='volunteer_details',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=25),
        ),
    ]