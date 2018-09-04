from django.db import models


class ProjectGroup(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    description = models.TextField(null=True, blank=True)
    project_group = models.ForeignKey(
        ProjectGroup,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
