# Generated by Django 4.1.7 on 2023-03-02 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('new', 'новый'), ('in progress', 'в процессе'), ('done', 'выполнено')], max_length=100, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('type', 'задача'), ('bug', 'ошибка'), ('enhancement', 'улучшение')], max_length=100, verbose_name='Тип задачи')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(blank=True, max_length=100, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('edit_time', models.DateTimeField(null=True, verbose_name='Время редактирования')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.status', verbose_name='Статус')),
                ('type', models.ManyToManyField(related_name='type_tasks', to='webapp.type', verbose_name='Тип задачи')),
            ],
        ),
    ]
