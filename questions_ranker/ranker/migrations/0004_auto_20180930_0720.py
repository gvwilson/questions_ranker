# Generated by Django 2.1 on 2018-09-30 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranker', '0003_auto_20180929_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankingentry',
            name='rank',
            field=models.CharField(choices=[('essential', 'Essential'), ('worthwhile', 'Worthwhile'), ('unimportant', 'Unimportant'), ('unwise', 'Unwise'), ('dont_understand', "I don't understand")], max_length=255, null=True, verbose_name='Selected rank'),
        ),
    ]
