from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	username = None

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []




class Template(models.Model):
	template_name = models.CharField(max_length=255)
	subject = models.CharField(max_length=255)
	body =models.TextField(blank=True,null=True)

	class Meta:
		ordering = ['-id']
	def __str__(self):
		return (f"{self.template_name}") if self.template_name else 'this Template has no body'
	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk': self.pk})