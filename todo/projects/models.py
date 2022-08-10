from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=32, help_text='Project name')
    url = models.URLField(help_text='Project url', null=True, blank=True)
    user = models.ManyToManyField(get_user_model())

class Todo(models.Model):
    text = models.TextField()
    project = models.ForeignKey('Projects', on_delete=models.CASCADE)
    created = models.DateField(editable=False)
    modified = models.DateField(editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now().date()
        self.modified = timezone.now().date()
        return super(Todo, self).save(*args, **kwargs)
