# Generated by Django 3.0.5 on 2020-06-16 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20200616_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='Friends',
        ),
        migrations.CreateModel(
            name='Friends_setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Friends', models.ManyToManyField(blank=True, null=True, related_name='_friends_setup_Friends_+', to='App.Friends_setup')),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.Account')),
            ],
        ),
    ]
