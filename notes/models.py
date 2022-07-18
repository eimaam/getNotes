from unicodedata import category
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
import os
from django.core.files.storage import FileSystemStorage

# Create your models here.
def instance(instance, filename):
    return f"{instance.user.username}{os.sep}{filename}"

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, *args, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

USER = get_user_model()
class Upload(models.Model):
    
    category = models.CharField(max_length=200)
    courseCode = models.CharField(max_length=200)
    courseTitle = models.CharField(max_length=200)
    upload_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    file = models.FileField(upload_to=instance, storage=OverwriteStorage())

    