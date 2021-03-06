# Generated by Django 3.2.8 on 2022-04-09 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audiofile', models.FileField(blank=True, null=True, upload_to='audisl/audioFiles/')),
                ('textfile', models.FileField(blank=True, null=True, upload_to='audisl/textFiles/')),
                ('imagefile', models.FileField(blank=True, null=True, upload_to='audisl/imageFiles/')),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
