from django.db import models

# Create your models here.
class User(models.Model):

    UNDERGRADUATE_CHOICES = (
        (1, '経済学部'),
        (2, '法学部'),
        (3, '文学部'),
        (4, '外国語学部'),
        (5, '教育学部'),
    )

    COURCE_CHOICES = (
        (1, '経済学科'),
        (2, '国際経済学科'),
        (3, '経営学科'),
        (4, '観光経営学科'),
        (5, '法律学科'),
        (6, '政治学科'),
        (7, '日本文化学科'),
        (8, '史学科'),
        (9, '社会学科'),
        (10, '心理学科'),
        (11, '外国語学科'),
        (12, '教育文化学科'),
        (13, '初等教育学科'),
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )

    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    undergraduate = models.IntegerField(
        verbose_name='学部',
        choices=UNDERGRADUATE_CHOICES,
        default=1,
    )

    cource = models.IntegerField(
        verbose_name='学科',
        choices=COURCE_CHOICES,
    )

    obtainedu_unit = models.IntegerField(
      verbose_name='取得単位',
    )


class Syllabus(models.Model):

    COURCE_CHOICES = (
        (1, '経済学科'),
        (2, '国際経済学科'),
        (3, '経営学科'),
        (4, '観光経営学科'),
        (5, '法律学科'),
        (6, '政治学科'),
        (7, '日本文化学科'),
        (8, '史学科'),
        (9, '社会学科'),
        (10, '心理学科'),
        (11, '外国語学科'),
        (12, '教育文化学科'),
        (13, '初等教育学科'),
    )

    OTHERS_CHOICES = (
        (1, '1年'),
        (2, '2年'),
        (3, '3年'),
        (4, '4年'),
    )

    SEMESTER_CHOICES = (
        (1, '前期'),
        (2, '後期'),
    )

    LECTURE_TYPE_CHOICES = (
        (1, '必修'),
        (2, '選択必修'),
        (3, '選択必修A'),
        (4, '選択必修B'),
        (5, '選択'),
        (6, 'その他'),
    )

    cource = models.IntegerField(
        verbose_name='学科',
        choices=COURCE_CHOICES,
    ) 

    others = models.IntegerField(
        verbose_name='学年',
        choices=OTHERS_CHOICES
    )

    semester = models.IntegerField(
        verbose_name='履修期',
        choices=SEMESTER_CHOICES
    )

    lecture_type = models.IntegerField(
        verbose_name='講義種類',
        choices=LECTURE_TYPE_CHOICES
    )