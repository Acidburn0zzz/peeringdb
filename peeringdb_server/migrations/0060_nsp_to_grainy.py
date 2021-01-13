# Generated by Django 2.2.17 on 2020-11-17 13:10

from django.db import migrations


def nsp_to_grainy(apps, schema_editor):
    NSP_UserPermission = apps.get_model("django_namespace_perms", "UserPermission")
    NSP_GroupPermission = apps.get_model("django_namespace_perms", "GroupPermission")
    G_UserPermission = apps.get_model("django_grainy", "UserPermission")
    G_GroupPermission = apps.get_model("django_grainy", "GroupPermission")

    for uperm in NSP_UserPermission.objects.all():
        print(
            f"migrating {uperm.namespace} for user {uperm.user_id}: {uperm.permissions}"
        )
        G_UserPermission.objects.get_or_create(
            namespace=uperm.namespace, permission=uperm.permissions, user=uperm.user
        )

    for gperm in NSP_GroupPermission.objects.all():
        print(
            f"migrating {gperm.namespace} for group {gperm.group_id}: {gperm.permissions}"
        )
        G_GroupPermission.objects.get_or_create(
            namespace=gperm.namespace, permission=gperm.permissions, group=gperm.group
        )


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0059_ixf_typos"),
    ]

    operations = [
        migrations.RunPython(nsp_to_grainy),
    ]
