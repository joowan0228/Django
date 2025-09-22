from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from pathlib import Path
from io import BytesIO
from django.core.files.base import ContentFile

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    thumbnail = models.ImageField(
        upload_to='todo/thumbnails',
        default='todo/no_image/NO-IMAGE.gif',
        null=True,
        blank=True
    )
    completed_image = models.ImageField(
        upload_to='todo/completed_images',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.completed_image:
            image = Image.open(self.completed_image)
            image.thumbnail((100, 100))
            image_path = Path(self.completed_image.name)
            thumbnail_name = f"{image_path.stem}_thumbnail{image_path.suffix}"
            ext = image_path.suffix.lower()
            if ext in ['.jpg', '.jpeg']:
                file_type = 'JPEG'
            elif ext == '.png':
                file_type = 'PNG'
            elif ext == '.gif':
                file_type = 'GIF'
            else:
                super().save(*args, **kwargs)
                return
            temp_thumb = BytesIO()
            image.save(temp_thumb, format=file_type)
            temp_thumb.seek(0)
            self.thumbnail.save(thumbnail_name, ContentFile(temp_thumb.read()), save=False)
            temp_thumb.close()
        super().save(*args, **kwargs)
