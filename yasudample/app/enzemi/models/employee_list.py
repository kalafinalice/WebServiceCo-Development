from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class EmployeeListManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class EmployeeList(AbstractBaseUser):
    employee_id = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    pc_address = models.EmailField(unique=True, db_index=True, max_length=100)
    mobile_address = models.EmailField(max_length=100)
    name = models.CharField(max_length=50, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    control_level = models.IntegerField(blank=True, null=True)
    work_start_time = models.TimeField(blank=True, null=True)
    work_finish_time = models.TimeField(blank=True, null=True)
    detination = models.IntegerField(blank=True, null=True)
    work_day = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=True)
    updater = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    is_admin = models.BooleanField(default=False)

    objects = EmployeeListManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
