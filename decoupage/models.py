import uuid

from django.db import models
from django.urls import reverse


class Region(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=16)
    code_iso = models.CharField(max_length=5)
    code_ansd = models.CharField(max_length=2)
    area = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['code_ansd']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Region_detail", kwargs={"pk": self.pk})


class Department(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    code_ansd = models.CharField(max_length=3)
    area = models.PositiveSmallIntegerField()
    region = models.ForeignKey(
        Region,
        related_name='departments',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['code_ansd']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("department_detail", kwargs={"pk": self.pk})


class Town(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32)
    department = models.ForeignKey(
        Department,
        related_name='towns',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Town_detail", kwargs={"pk": self.pk})
