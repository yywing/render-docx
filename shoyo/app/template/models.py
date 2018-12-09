import os
import uuid
from urllib.parse import urljoin

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage

icon_location = FileSystemStorage(
    location=os.path.join(settings.MEDIA_ROOT, 'template_icon'),
    base_url=urljoin(settings.MEDIA_URL, 'template-icon')
)


class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    icon = models.FileField(storage=icon_location)
    remark = models.TextField()

    json_schema = JSONField(default={})
    ui_schema = JSONField(default={})

    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        permissions = (
            ('user', 'can use it'),
            ('editor', 'can edit it, and use'),
            ('owner', 'with full power'),
        )
