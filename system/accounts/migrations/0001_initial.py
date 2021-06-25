# Generated by Django 3.0 on 2021-06-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_option', models.CharField(choices=[('Basic', 'Basic'), ('Professional', 'Professional'), ('Enterprise', 'Enterprise')], max_length=200, null=True)),
            ],
        ),
    ]
