# Generated by Django 4.2 on 2023-12-16 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_book_return_date_remove_book_taken_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookTransaction',
            new_name='Transaction',
        ),
        migrations.RemoveField(
            model_name='book',
            name='department',
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.department')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(default=576, on_delete=django.db.models.deletion.CASCADE, to='library.subject'),
            preserve_default=False,
        ),
    ]
