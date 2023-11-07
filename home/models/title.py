from django.db import models

from django.utils.translation import gettext_lazy as _
from .abstract_models import BaseModelMixin



class YtVideoData(BaseModelMixin):

    """"""

    STATUS_CHOICE = [
        ("", "--Select Status--"),
        ("IN_ACTIVE", "In-Active"),
        ("DRAFT", "Draft"),
        ("PUBLISHED", "Published"),
        ("DEMO", "Demo"),
    ]

    video_link = models.CharField(_("Question"), max_length=90)
    video_discription = models.TextField(_("Description"), blank=True, null=False)
    video_name = models.CharField(_("Question"), max_length=90)

    status = models.CharField(
        _("Status"), default="PUBLISHED", choices=STATUS_CHOICE, max_length=300
    )

    def __str__(self):
        return self.video_name

