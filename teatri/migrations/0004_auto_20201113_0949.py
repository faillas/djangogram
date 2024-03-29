# Generated by Django 2.2.17 on 2020-11-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teatri', '0003_auto_20201113_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valmedi',
            name='nome_medi',
        ),
        migrations.AddField(
            model_name='profili',
            name='caratteri_medi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='casual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='designed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='grafica',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='gruppo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='hashtag_medi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='parole_medie',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='post_medi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='professional',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='scena',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='singolo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profili',
            name='tag_medi',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Img',
        ),
        migrations.DeleteModel(
            name='ValMedi',
        ),
    ]
