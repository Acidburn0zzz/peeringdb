# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-07 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

def forwards_func(apps, schema_editor):
    """
    move relation shit from sponsorship->org to org->sponsorship
    to allow a many orgs to many sponsorship relation
    """
    Sponsorship =  apps.get_model("peeringdb_server", "Sponsorship")
    SponsorshipOrganization = apps.get_model("peeringdb_server", "SponsorshipOrganization")

    for sponsorship in Sponsorship.objects.all():
        SponsorshipOrganization.objects.create(
            org=sponsorship.org,
            sponsorship=sponsorship,
            url=sponsorship.url,
            logo=sponsorship.logo)


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0020_vqueue_item_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorshipOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, help_text='If specified clicking the sponsorship will take the user to this location', null=True, verbose_name='URL')),
                ('logo', models.FileField(blank=True, help_text='Allows you to upload and set a logo image file for this sponsorship', null=True, upload_to=b'logos/')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorshiporg_set', to='peeringdb_server.Organization')),
                ('sponsorship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorshiporg_set', to='peeringdb_server.Sponsorship')),
            ],
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='orgs',
            field=models.ManyToManyField(related_name='sponsorship_set', through='peeringdb_server.SponsorshipOrganization', to='peeringdb_server.Organization'),
        ),
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]