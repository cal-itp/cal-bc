from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline

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


class ValueInline(TabularInline):
    model = Value

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class FieldColumnInline(TabularInline):
    model = Field.column.through

    def get_extra(self, request, obj=None, **kwargs):
        if (
            obj is not None
            and obj.pk is not None
            and isinstance(obj, Field)
            and FieldColumn.objects.filter(field_id=obj.pk).count()
        ):
            return 0
        else:
            return 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "column" and request.resolver_match.kwargs:
            kwargs["queryset"] = Column.objects.filter(
                column_group__group=request.resolver_match.kwargs["object_id"]
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FieldRangeInline(TabularInline):
    model = FieldRange

    def get_extra(self, request, obj=None, **kwargs):
        return 0

@admin.register(Field)
class FieldAdmin(ModelAdmin):
    model = Field
    inlines = [FieldRangeInline, FieldColumnInline, ValueInline]
    ordering_field = "position"


class FieldInline(StackedInline):
    model = Field
    inlines = [FieldColumnInline, FieldRangeInline, ValueInline]
    ordering_field = "position"
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Row) and obj.field_set.count():
            return 0
        else:
            return 1


@admin.register(Row)
class RowAdmin(ModelAdmin):
    model = Row
    inlines = [FieldInline]
    ordering_field = "position"
    show_change_link = True


class RowInline(StackedInline):
    model = Row
    inlines = [FieldInline]
    ordering_field = "position"
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Group) and obj.row_set.count():
            return 0
        else:
            return 1


class ColumnInline(TabularInline):
    model = Column
    ordering_field = "position"

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, ColumnGroup) and obj.column_set.count():
            return 0
        else:
            return 1


class ColumnGroupInline(TabularInline):
    model = ColumnGroup
    inlines = [ColumnInline]
    ordering_field = "position"

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Group) and obj.columngroup_set.count():
            return 0
        else:
            return 1


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    model = Group
    inlines = [RowInline, ColumnGroupInline]
    exclude = ["position"]
    list_display = ["name", "model_name", "version_name", "section", "subsection"]
    list_select_related = ["subsection", "subsection__section", "subsection__section__version", "subsection__section__version__model"]
    ordering = ["name"]
    search_fields = ["name", "subsection__code", "subsection__name", "subsection__code", "subsection__section__name", "subsection__section__version__name", "subsection__section__version__model__name"]
    search_help_text = "Search by Name, Model, Version, Section, and Subsection"
    fields = ["model_name", "version_name", "section", "subsection", "name", "description", "is_summary"]
    readonly_fields = ["model_name", "version_name", "section"]
    warn_unsaved_form = True

    @admin.display(description="Model", ordering="subsection__section__version__model__name")
    def model_name(self, obj):
        return obj.subsection.section.version.model.name

    @admin.display(description="Version", ordering="subsection__section__version__name")
    def version_name(self, obj):
        return obj.subsection.section.version.name

    @admin.display(description="Section", ordering="subsection__section__name")
    def section(self, obj):
        return obj.subsection.section


class GroupInline(TabularInline):
    model = Group
    ordering_field = "position"
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Subsection) and obj.group_set.count():
            return 0
        else:
            return 1

@admin.register(Subsection)
class SubsectionAdmin(ModelAdmin):
    model = Subsection
    inlines = [GroupInline]
    fields = ["model_name", "version_name", "section", "name", "code", "description", "guide"]
    readonly_fields = ["model_name", "version_name", "section"]
    list_display = ["name", "code", "section", "model_name", "version_name"]
    search_fields = ["name", "code", "description", "model__name", "version_name"]
    search_help_text = "Search by Name, Code, Description, Model, and Model Version"
    warn_unsaved_form = True

    @admin.display(description="Model", ordering="subsection__section__version__model__name")
    def model_name(self, obj):
        return obj.section.version.model.name

    @admin.display(description="Version", ordering="subsection__section__version__name")
    def version_name(self, obj):
        return obj.section.version.name

    @admin.display(description="Section", ordering="subsection__section__name")
    def section(self, obj):
        return obj.section


class SubsectionInline(StackedInline):
    model = Subsection
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Section) and obj.subsection_set.count():
            return 0
        else:
            return 1


class SectionInline(StackedInline):
    model = Section
    inlines = [SubsectionInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Version) and obj.section_set.count():
            return 0
        else:
            return 1


@admin.register(Version)
class VersionAdmin(ModelAdmin):
    model = Version
    inlines = [SectionInline]
    list_display = ["name", "model", "url"]
    search_fields = ["name", "url", "model__name"]
    search_help_text = "Search by Name, URL, and Model"
    warn_unsaved_form = True


class VersionInline(TabularInline):
    model = Version
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Model) and obj.version_set.count():
            return 0
        else:
            return 1

@admin.register(Model)
class ModelAdmin(ModelAdmin):
    inlines = [VersionInline]
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    search_help_text = "Search by Name and Description"
    warn_unsaved_form = True

