from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.utils import timezone
from markdown import markdown
from scrapy.selector import HtmlXPathSelector


class CustomUserManager(BaseUserManager):

    def create_user(self, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_staff=False, is_active=True, is_superuser=False, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('e-mail address', max_length=200, unique=True, db_index=True)
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'table_user'
        verbose_name = 'User'


class Post(models.Model):

    url = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    time_published = models.DateTimeField(blank=True, null=True)
    time_modified = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.title)

    def save(self, **kwargs):
        if not self.id:
            self.time_published = timezone.now()
        self.time_modified = timezone.now()
        super(Post, self).save()

    def xpath_extract(self, selector, path, extract_all=False):
        result = selector.select(path).extract()
        if not extract_all:
            if len(result) > 0:
                return result[0]
            else:
                return None
        else:
            return result

    def html_content(self):
        return markdown(self.content)

    def summary(self):
        selector = HtmlXPathSelector(text=self.html_content())
        first_paragraph = self.xpath_extract(selector, "//p/text()")
        return '<p>%s&#8230;</p>' % (first_paragraph)

    class Meta:
        db_table = 'table_post'
