# Generated by Django 2.0.2 on 2018-05-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0002_auto_20180511_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automationtestresult',
            name='host',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='测试地址'),
        ),
    ]