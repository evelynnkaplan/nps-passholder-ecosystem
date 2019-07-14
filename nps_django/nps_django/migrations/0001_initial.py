# Generated by Django 2.2.3 on 2019-07-12 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Passholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nps_django.Park')),
                ('passholder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nps_django.Passholder')),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Standard', 'Annual Pass'), ('Senior Lifetime', 'Senior Lifetime Pass'), ('Senior Annual', 'Senior Annual Pass'), ('Access', 'Access Pass'), ('Military', 'US Military'), ('4th Grade', 'Annual 4th Grade Pass'), ('Volunteer', 'Volunteer Pass')], default='Standard', max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone_num', models.CharField(max_length=20)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('passholders', models.ManyToManyField(to='nps_django.Passholder')),
            ],
        ),
    ]
