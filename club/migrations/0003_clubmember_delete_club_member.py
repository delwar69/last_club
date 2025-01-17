# Generated by Django 5.0.6 on 2025-01-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_club_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=100)),
                ('joining_date', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('spouse_name', models.CharField(blank=True, max_length=200)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Other', 'Other')], max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5)),
                ('permanent_address', models.TextField()),
                ('present_address', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('phone_office', models.CharField(blank=True, max_length=15)),
                ('phone_residence', models.CharField(blank=True, max_length=15)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('signature_image', models.ImageField(blank=True, null=True, upload_to='signatures/')),
            ],
        ),
        migrations.DeleteModel(
            name='club_Member',
        ),
    ]
