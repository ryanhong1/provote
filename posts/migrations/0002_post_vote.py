# Generated by Django 3.1.6 on 2021-02-13 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.question'),
        ),
    ]
