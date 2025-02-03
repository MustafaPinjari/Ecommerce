from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser to handle user creation with email as a unique identifier.
    """
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    A custom user model extending AbstractUser, allowing for additional fields.
    """
    email = models.EmailField(unique=True)  # Email as unique and required
    phone = models.CharField(max_length=15, blank=True, null=True, help_text="Optional phone number.")
    address = models.TextField(blank=True, null=True, help_text="Optional address for the user.")
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        help_text="Upload a profile picture."
    )

    objects = CustomUserManager()  # Assign the custom manager

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.username

    def clean(self):
        """
        Normalize email field during data validation.
        """
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
