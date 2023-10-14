from django.db import models

from uploader.models import Image

STATUS_EQUIPMENT = [
        ('new', 'Novo'),
        ('semi-new', 'Semi-novo'),
    ]

TYPE_EQUIPMENT = [
    ('athletic', "Athletic"),
    ('supergold', "SuperGold")
]

class Equipment(models.Model):
    name = models.CharField(max_length=200) # remove it
    model = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, choices=TYPE_EQUIPMENT, default='athletic', null=True, blank=True) #
    status = models.CharField(max_length=20, choices=STATUS_EQUIPMENT, null=True, blank=True, default=None)
    description = models.CharField(max_length=200, blank=True, null=True) 
    image = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipments"