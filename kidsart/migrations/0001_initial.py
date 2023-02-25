# Generated by Django 4.1.7 on 2023-02-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imageData', models.BinaryField()),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
