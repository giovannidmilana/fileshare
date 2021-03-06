# Generated by Django 3.1.1 on 2020-09-29 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directory', models.FileField(default='media/images/users.jpg', upload_to='temp/')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(default='media/images/users.jpg', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='media/images/users.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='MultiFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploads', models.FileField(default='media/images/users.jpg', upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('doc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='g_cloud.dirupload')),
            ],
        ),
    ]
