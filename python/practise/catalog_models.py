from django.contrib.auth.models import User
from django.db import models
from PIL import Image

SOURCE_TYPE = (
    ('connect', 'Connect'),
    ('course', 'Course')
)

FORMAT_TYPE = (
    ('feature', 'Feature'),
    ('normal', 'Normal')
)

SORT_AS_TYPE = (
    ('asc', 'Ascending'),
    ('desc', 'Descending'),
)


class Content_Source(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    type = models.CharField(max_length=255, choices=SOURCE_TYPE)
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_source_creator")
    modified_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_source_modifier")

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Sources"
        unique_together = ("name", "title")

    def __str__(self):
        return self.name


class Content_Category(models.Model):

    source = models.ForeignKey(to=Content_Source, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    order = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_category_creator")
    modified_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_category_modifier")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Content Categories"


class Content_List(models.Model):

    category = models.ForeignKey(to=Content_Category, on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_list_creator")
    modified_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_list_modifier")

    name = models.CharField(max_length=255)
    format_type = models.CharField(max_length=255, choices=FORMAT_TYPE)
    mode = models.CharField(max_length=255)
    auto_function = models.CharField(max_length=255)
    sort_as = models.CharField(max_length=255, choices=SORT_AS_TYPE)
    sort_by = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    region = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Content(models.Model):

    source = models.ForeignKey(to=Content_Source, on_delete=models.PROTECT)
    lists = models.ManyToManyField(to=Content_List, through="Mapper")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_creator")
    modified_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="content_modifier")

    name = models.CharField(max_length=255)
    icon = models.ImageField()
    source_identity = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Mapper(models.Model):
    list = models.ForeignKey(to=Content_List, on_delete=models.PROTECT)
    content = models.ForeignKey(to=Content, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="mapper_creator")
    modified_by = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name="mapper_modifier")

    def __str__(self):
        return self.content + " mapped to " + self.list


class BookMark(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    content = models.ForeignKey(to=Content, on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    is_active = models.BooleanField(verbose_name="is the entry active?")

    def __str__(self):
        # pylint: disable=E1101
        return self.user.username + " bookmarked " + self.content.name
