from django.db import models


class Model(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(null=False, blank=False, db_index=True)

    def __str__(self):
        return self.name

    def latest_version(self):
        return list(self.version_set.all())[-1]


class Version(models.Model):
    class Meta:
        ordering = ['name']

    model = models.ForeignKey(Model, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, db_index=True)
    url = models.CharField(null=False, blank=False)

    def __str__(self):
        return f"{str(self.model)} v{self.name}"


class Section(models.Model):
    class Meta:
        ordering = ['code']

    version = models.ForeignKey(Version, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    code = models.CharField(null=False, blank=False, db_index=True)

    def __str__(self):
        return f"{str(self.version)} § {self.code} {self.name}"


class Subsection(models.Model):
    class Meta:
        ordering = ['code']

    section = models.ForeignKey(Section, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    code = models.CharField(null=False, blank=False, db_index=True)
    description = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{str(self.section.version)} § {self.section.code}{self.code} {self.name}"


class Group(models.Model):
    class Meta:
        ordering = ['position']

    subsection = models.ForeignKey(Subsection, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{str(self.subsection.section.version)} § {self.subsection.section.code}{self.subsection.code} {self.name}"


class Row(models.Model):
    class Meta:
        ordering = ['position']

    group = models.ForeignKey(Group, null=False, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{str(self.group.subsection.section.version)} § {self.group.subsection.section.code}{self.group.subsection.code} Row {self.position}"


class Field(models.Model):
    class Meta:
        ordering = ['position']

    row = models.ForeignKey(Row, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    cell = models.CharField(null=False)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{str(self.row.group.subsection.section.version)} § {self.row.group.subsection.section.code}{self.row.group.subsection.code} {self.name}"


class Value(models.Model):
    class Meta:
        ordering = ['position']

    field = models.ForeignKey(Field, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    value = models.CharField(null=False, blank=False)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return self.name
