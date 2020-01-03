from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
#from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')

        profile = ""
        if request_data.get('profile'):
            profile = request_data['profile']

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now,
            profile=profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    GENDER = (("0", "Female"), ("1", "Male"), ("2", "Secret"))
    
    user_id     = models.AutoField(verbose_name="user_id", primary_key=True)
    username    = models.CharField(_('username'), max_length=30)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True)
    email       = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    profile     = models.CharField(_('profile'), max_length=255, blank=True)
    gender      = models.CharField(choices = GENDER, max_length=1, default = "2", blank=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    image       = models.ImageField(_('image'), max_length=200, upload_to="users/images/",
                                          null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def email_user(self, subject, message, from_email=None):
        """Send an email to this User. """
        send_mail(subject, message, from_email, [self.email])

    def user_has_perm(user, perm, obj):
        """
        A backend can raise `PermissionDenied` to short-circuit permission checking.
        """
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @staticmethod
    def get_default_user():
        user, created = User.objects.get_or_create(
            username = 'unknown user',
            email= 'xxx@sample.com'
        )
        return buyer

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "顧客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Address(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="投稿時間")
    user = models.ForeignKey('User', verbose_name="顧客",related_name="addresses", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name="名前")
    last_name = models.CharField(max_length=255, verbose_name="名字")
    street_address1 = models.CharField(max_length=255, verbose_name="住所１") 
    street_address2 = models.CharField(max_length=255, verbose_name="住所２", blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name="市町村区")
    state = models.CharField(max_length=255, verbose_name="都道府県")
    zip = models.CharField(max_length=255, verbose_name="郵便番号")
    phone = models.CharField(max_length=255, verbose_name="電話番号", blank=True, null=True)

    class Meta:
        verbose_name = "住所"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

