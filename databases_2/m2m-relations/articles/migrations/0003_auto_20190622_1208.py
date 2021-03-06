# Generated by Django 2.2.2 on 2019-06-22 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('articles', '0002_auto_20190622_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_mane', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='Scope',
        ),
        migrations.DeleteModel(
            name='ArticleTag',
        ),
        migrations.AddField(
            model_name='articlebadge',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
        migrations.AddField(
            model_name='articlebadge',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Scope'),
        ),
        migrations.AddField(
            model_name='article',
            name='badges',
            field=models.ManyToManyField(through='articles.ArticleBadge', to='articles.Scope'),
        ),
    ]
