# Generated by Django 2.2.2 on 2019-06-22 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20190622_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlebadge',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_data', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articlebadge',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_data', to='articles.Scope'),
        ),
    ]
