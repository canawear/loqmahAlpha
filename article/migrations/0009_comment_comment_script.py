# Generated by Django 2.2.4 on 2019-08-14 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190814_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_script',
            field=models.CharField(default='Buraya Dokunmayın', max_length=100),
        ),
    ]
