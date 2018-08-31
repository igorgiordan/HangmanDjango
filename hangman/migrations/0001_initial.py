# Generated by Django 2.1 on 2018-08-30 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='user2')),
                ('status', models.IntegerField(choices=[(1, 'Finalizado'), (2, 'Não finalizado')])),
                ('errors', models.IntegerField(default=0, verbose_name='erros')),
            ],
            options={
                'verbose_name': 'partida',
                'verbose_name_plural': 'partidas',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, verbose_name='user1')),
                ('score', models.IntegerField(default=0, verbose_name='pontuação')),
            ],
            options={
                'verbose_name': 'pontuação',
                'verbose_name_plural': 'pontuações',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=15, verbose_name='palavra')),
                ('clue', models.CharField(max_length=150, verbose_name='dica')),
            ],
            options={
                'verbose_name': 'palavra',
                'verbose_name_plural': 'palavras',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Word', to='hangman.Word'),
        ),
    ]
