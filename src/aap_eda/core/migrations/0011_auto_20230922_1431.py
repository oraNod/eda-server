# Generated by Django 3.2.20 on 2023-09-22 14:31

from django.db import migrations, models

import aap_eda.core.enums


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_activation_status_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="activation",
            name="status_message",
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="activationinstance",
            name="status_message",
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="activation",
            name="status",
            field=models.TextField(
                choices=[
                    ("starting", "starting"),
                    ("running", "running"),
                    ("pending", "pending"),
                    ("failed", "failed"),
                    ("stopping", "stopping"),
                    ("stopped", "stopped"),
                    ("deleting", "deleting"),
                    ("completed", "completed"),
                    ("unresponsive", "unresponsive"),
                    ("error", "error"),
                ],
                default=aap_eda.core.enums.ActivationStatus["PENDING"],
            ),
        ),
        migrations.AlterField(
            model_name="activationinstance",
            name="status",
            field=models.TextField(
                choices=[
                    ("starting", "starting"),
                    ("running", "running"),
                    ("pending", "pending"),
                    ("failed", "failed"),
                    ("stopping", "stopping"),
                    ("stopped", "stopped"),
                    ("deleting", "deleting"),
                    ("completed", "completed"),
                    ("unresponsive", "unresponsive"),
                    ("error", "error"),
                ],
                default=aap_eda.core.enums.ActivationStatus["PENDING"],
            ),
        ),
    ]