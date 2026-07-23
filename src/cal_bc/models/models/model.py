from django.db import models
from django_prose_editor.fields import ProseEditorField


class Model(models.Model):
    class Meta:
        ordering = ["name"]

    name = models.CharField(null=False, blank=False, db_index=True)

    def __str__(self):
        return self.name

    def latest_version(self):
        versions = list(self.version_set.all())
        return versions[-1] if len(versions) > 0 else None


class Version(models.Model):
    class Meta:
        ordering = ["name"]

    model = models.ForeignKey(Model, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, db_index=True)
    url = models.CharField(null=False, blank=False)

    def __str__(self):
        return f"{self.model!s} v{self.name}"

    def has_form_link(self):
        return self.section_set.count() > 0


class Section(models.Model):
    class Meta:
        ordering = ["code"]

    version = models.ForeignKey(Version, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    code = models.CharField(null=False, blank=False, db_index=True)

    def __str__(self):
        return f"{self.version!s} § {self.code} {self.name}"

    @property
    def next_section(self):
        return self.version.section_set.filter(code__gt=self.code).first()

    @property
    def previous_section(self):
        return self.version.section_set.filter(code__lt=self.code).last()


class Subsection(models.Model):
    class Meta:
        ordering = ["code"]

    section = models.ForeignKey(Section, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    code = models.CharField(null=False, blank=False, db_index=True)
    description = models.CharField(null=True, blank=True)
    guide = ProseEditorField(
        null=True,
        blank=True,
        sanitize=True,
        extensions={
            "Bold": True,
            "Italic": True,
            "Heading": {"levels": [1, 2, 3]},
            "BulletList": True,
            "ListItem": True,
        },
    )

    def __str__(self):
        return f"{self.section.version!s} § {self.section.code}{self.code} {self.name}"

    @property
    def next_subsection(self):
        query = self.section.subsection_set.filter(code__gt=self.code)
        if not query.exists() and self.section.next_section:
            query = self.section.next_section.subsection_set
        return query.first()

    @property
    def previous_subsection(self):
        query = self.section.subsection_set.filter(code__lt=self.code)
        if not query.exists() and self.section.previous_section:
            query = self.section.previous_section.subsection_set
        return query.last()


class Group(models.Model):
    class Meta:
        ordering = ["position"]

    subsection = models.ForeignKey(Subsection, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    description = models.CharField(null=True, blank=True)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{self.subsection.section.version!s} § {self.subsection.section.code}{self.subsection.code} {self.name}"

    @property
    def table_row_set(self):
        return Row.objects.filter(
            id__in=self.row_set.filter(
                field__column__column_group__in=self.columngroup_set.all()
            ).all()
        )

    @property
    def non_table_row_set(self):
        return Row.objects.filter(
            id__in=self.row_set.exclude(
                field__column__column_group__in=self.columngroup_set.all()
            ).all()
        )

    @property
    def nonempty_column_group_set(self):
        return self.columngroup_set.exclude(name="").all()


class Row(models.Model):
    class Meta:
        ordering = ["position"]

    group = models.ForeignKey(Group, null=False, on_delete=models.CASCADE)
    name = models.CharField(blank=True)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)
    guide = ProseEditorField(
        null=True,
        blank=True,
        sanitize=True,
        extensions={
            "Bold": True,
            "Italic": True,
            "Heading": {"levels": [1, 2, 3]},
            "BulletList": True,
            "ListItem": True,
        },
    )

    def __str__(self):
        return f"{self.group.subsection.section.version!s} § {self.group.subsection.section.code}{self.group.subsection.code} Row {self.position}"


class ColumnGroup(models.Model):
    class Meta:
        ordering = ["position"]

    group = models.ForeignKey(Group, null=False, on_delete=models.CASCADE)
    name = models.CharField(blank=True)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{self.group!s} {self.name}"


class Column(models.Model):
    class Meta:
        ordering = ["position"]

    column_group = models.ForeignKey(ColumnGroup, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{self.column_group!s} {self.name}"


class FieldColumn(models.Model):
    field = models.OneToOneField("Field", on_delete=models.CASCADE)
    column = models.ForeignKey("Column", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.column)


class Field(models.Model):
    class Meta:
        ordering = ["position"]

    row = models.ForeignKey(Row, null=False, on_delete=models.CASCADE)
    column = models.ManyToManyField(Column, through="FieldColumn")
    name = models.CharField(null=False, blank=False)
    cell = models.CharField(null=False)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return f"{self.row.group.subsection.section.version!s} § {self.row.group.subsection.section.code}{self.row.group.subsection.code} {self.name}"


class Value(models.Model):
    class Meta:
        ordering = ["position"]

    field = models.ForeignKey(Field, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    value = models.CharField(null=False, blank=False)
    position = models.PositiveIntegerField(default=0, null=False, db_index=True)

    def __str__(self):
        return self.name
