import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModelMixin(models.Model):

    """"""

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    updated_on = models.DateTimeField(_("Modification Date"), auto_now=True)
    created_on = models.DateTimeField(_("Creation Date"), auto_now_add=True)
    is_delete = models.BooleanField(default = False)

    class Meta:
        abstract = True



