# Generated by Django 2.2.17 on 2021-01-30 11:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_no', models.CharField(max_length=12)),
                ('is_mentor', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay_text', models.TextField(blank=True, max_length=500)),
                ('user_comment', models.TextField(blank=True, max_length=500)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('replayed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentor', to='mentor_user.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, max_length=500)),
                ('attach', models.FileField(upload_to='uploads/% Y/% m/% d/')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('replays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mentor_user.Replay')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='mentor_user.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='MenterRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_request_exits', models.BooleanField(default=True)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('requested_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_request', to='mentor_user.UserProfile')),
                ('requested_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentor_request', to='mentor_user.UserProfile')),
            ],
        ),
    ]