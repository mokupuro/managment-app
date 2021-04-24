from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


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


class CustomUserManager(UserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""

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

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
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
        default=1
    )

    obtainedu_unit = models.IntegerField(
        verbose_name='取得単位',
        null=True
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        """username属性のゲッター

        他アプリケーションが、username属性にアクセスした場合に備えて定義
        メールアドレスを返す
        """
        return self.email