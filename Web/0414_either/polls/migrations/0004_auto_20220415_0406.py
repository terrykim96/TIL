# Generated by Django 3.2.12 on 2022-04-14 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20220415_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='vote',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='polls.vote'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='choice_a',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vote',
            name='choice_b',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vote',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]