# Generated by Django 3.2 on 2021-04-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('name', models.CharField(max_length=200, verbose_name='名前')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('undergraduate', models.IntegerField(choices=[(1, '経済学部'), (2, '法学部'), (3, '文学部'), (4, '外国語学部'), (5, '教育学部')], default=1, verbose_name='学部')),
                ('cource', models.IntegerField(choices=[(1, '経済学科'), (2, '国際経済学科'), (3, '経営学科'), (4, '観光経営学科'), (5, '法律学科'), (6, '政治学科'), (7, '日本文化学科'), (8, '史学科'), (9, '社会学科'), (10, '心理学科'), (11, '外国語学科'), (12, '教育文化学科'), (13, '初等教育学科')], verbose_name='学科')),
                ('obtainedu_unit', models.IntegerField(verbose_name='取得単位')),
            ],
        ),
    ]