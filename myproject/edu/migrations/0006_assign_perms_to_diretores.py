from django.db import migrations


def assign_perms(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    try:
        ct = ContentType.objects.get(app_label='edu', model='curso')
    except ContentType.DoesNotExist:
        return

    codenames = ['add_curso', 'change_curso', 'delete_curso', 'view_curso']
    perms = list(Permission.objects.filter(content_type=ct, codename__in=codenames))

    try:
        group = Group.objects.get(name='diretores')
    except Group.DoesNotExist:
        return

    if perms:
        group.permissions.add(*perms)


def remove_perms(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    try:
        ct = ContentType.objects.get(app_label='edu', model='curso')
    except ContentType.DoesNotExist:
        return

    codenames = ['add_curso', 'change_curso', 'delete_curso', 'view_curso']
    perms = list(Permission.objects.filter(content_type=ct, codename__in=codenames))

    Group = apps.get_model('auth', 'Group')
    try:
        group = Group.objects.get(name='diretores')
        if perms:
            group.permissions.remove(*perms)
    except Group.DoesNotExist:
        return


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0005_alter_disciplina_curso_alter_disciplina_nome'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(assign_perms, remove_perms),
    ]
