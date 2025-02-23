from django.db import migrations

def add_default_data(apps, schema_editor):
    ReclamoTipo = apps.get_model('reclamos', 'ReclamoTipo')
    ReclamoEstado = apps.get_model('reclamos', 'ReclamoEstado')

    ReclamoTipo.objects.create(nombre='General', descripcion='Reclamos generales')
    ReclamoEstado.objects.create(nombre='Nuevo', descripcion='Reclamo recién creado')

class Migration(migrations.Migration):

    dependencies = [
        ('reclamos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_data),
    ]
