# Generated by Django 4.1.13 on 2024-01-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=100)),
                ('post_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=100)),
                ('likes_count', models.IntegerField()),
                ('share_count', models.IntegerField()),
                ('updated_time', models.DateTimeField(blank=True, null=True)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('connection_code', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100)),
                ('tracked_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100, null=True)),
                ('banner', models.CharField(max_length=100, null=True)),
                ('bio', models.CharField(max_length=100, null=True)),
                ('profession', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
