# Generated by Django 3.2 on 2021-04-24 04:58

from django.db import migrations, models
import django.utils.timezone
import managementapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cource', models.IntegerField(choices=[(1, '経済学科'), (2, '国際経済学科'), (3, '経営学科'), (4, '観光経営学科'), (5, '法律学科'), (6, '政治学科'), (7, '日本文化学科'), (8, '史学科'), (9, '社会学科'), (10, '心理学科'), (11, '外国語学科'), (12, '教育文化学科'), (13, '初等教育学科')], verbose_name='学科')),
                ('others', models.IntegerField(choices=[(1, '1年'), (2, '2年'), (3, '3年'), (4, '4年')], verbose_name='学年')),
                ('semester', models.IntegerField(choices=[(1, '前期'), (2, '後期')], verbose_name='履修期')),
                ('lecture_type', models.IntegerField(choices=[(1, '必修'), (2, '選択必修'), (3, '選択必修A'), (4, '選択必修B'), (5, '選択'), (6, 'その他')], verbose_name='講義種類')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('undergraduate', models.IntegerField(choices=[(1, '経済学部'), (2, '法学部'), (3, '文学部'), (4, '外国語学部'), (5, '教育学部')], default=1, verbose_name='学部')),
                ('cource', models.IntegerField(choices=[(1, '経済学科'), (2, '国際経済学科'), (3, '経営学科'), (4, '観光経営学科'), (5, '法律学科'), (6, '政治学科'), (7, '日本文化学科'), (8, '史学科'), (9, '社会学科'), (10, '心理学科'), (11, '外国語学科'), (12, '教育文化学科'), (13, '初等教育学科')], default=1, verbose_name='学科')),
                ('obtainedu_unit', models.IntegerField(verbose_name='取得単位')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', managementapp.models.CustomUserManager()),
            ],
        ),
    ]
