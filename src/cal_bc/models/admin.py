import nested_admin
from django.contrib import admin

from cal_bc.models.models.model import (
    Column,
    ColumnGroup,
    Field,
    FieldColumn,
    FieldRange,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Value,
    Version,
)


class ValueInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Value

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class FieldColumnInline(nested_admin.NestedTabularInline):
    model = Field.column.through

    def get_extra(self, request, obj=None, **kwargs):
        if (
            obj is not None
            and obj.pk is not None
            and FieldColumn.objects.filter(field_id=obj.pk).count()
        ):
            return 0
        else:
            return 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "column":
            kwargs["queryset"] = Column.objects.filter(
                column_group__group=request.resolver_match.kwargs["object_id"]
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FieldRangeInline(nested_admin.NestedTabularInline):
    model = FieldRange

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class FieldInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = Field
    inlines = [FieldColumnInline, FieldRangeInline, ValueInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.field_set.count():
            return 0
        else:
            return 1


class RowInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = Row
    inlines = [FieldInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.row_set.count():
            return 0
        else:
            return 1


class ColumnInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Column

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.column_set.count():
            return 0
        else:
            return 1


class ColumnGroupInline(
    nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline
):
    model = ColumnGroup
    inlines = [ColumnInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.columngroup_set.count():
            return 0
        else:
            return 1


@admin.register(Group)
class GroupAdmin(nested_admin.NestedModelAdmin):
    model = Group
    inlines = [RowInline, ColumnGroupInline]
    exclude = ["position"]
    list_display = ["name", "model_name", "version_name", "section", "subsection"]
    list_select_related = ["subsection", "subsection__section", "subsection__section__version", "subsection__section__version__model"]
    ordering = ["name"]
    search_fields = ["name", "subsection__code", "subsection__name", "subsection__code", "subsection__section__name", "subsection__section__version__name", "subsection__section__version__model__name"]
    search_help_text = "Search by Name, Model, Version, Section, and Subsection"

    @admin.display(description="Model", ordering="subsection__section__version__model__name")
    def model_name(self, obj):
        return obj.subsection.section.version.model.name

    @admin.display(description="Version", ordering="subsection__section__version__name")
    def version_name(self, obj):
        return obj.subsection.section.version.name

    @admin.display(description="Section", ordering="subsection__section__name")
    def section(self, obj):
        return obj.subsection.section


class GroupInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Group
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.group_set.count():
            return 0
        else:
            return 1


class SubsectionInline(nested_admin.NestedStackedInline):
    model = Subsection
    inlines = [GroupInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.subsection_set.count():
            return 0
        else:
            return 1


class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    inlines = [SubsectionInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.section_set.count():
            return 0
        else:
            return 1


@admin.register(Version)
class VersionAdmin(nested_admin.NestedModelAdmin):
    model = Version
    inlines = [SectionInline]
    list_display = ["name", "model", "url"]
    search_fields = ["name", "url", "model__name"]
    search_help_text = "Search by Name, URL, and Model"


class VersionInline(nested_admin.NestedTabularInline):
    model = Version
    show_change_link = True


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    inlines = [VersionInline]
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    search_help_text = "Search by Name and Description"
