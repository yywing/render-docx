import os
import uuid

from django.db import models
from django.conf import settings


class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    remark = models.TextField()
    template = models.ForeignKey(
        "app.template.Template", on_delete=models.CASCADE
    )

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

    @property
    def path(self):
        return os.path.join(settings.DOCUMENT_PATH, self.id.hex)
