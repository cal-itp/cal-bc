from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline

from cal_bc.models.models.model import (
    Column,
    ColumnGroup,
    Field,
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
    ordering_field = "position"
    hide_ordering_field = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Field) and obj.value_set.count():
            return 0
        else:
            return 1


class FieldColumnInline(TabularInline):
    model = Field.column.through

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "column" and request.resolver_match.kwargs:
            kwargs["queryset"] = Column.objects.filter(
                column_group__group=Group.objects.filter(
                    row__field__id=request.resolver_match.kwargs["object_id"]
                ).first()
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FieldRangeInline(TabularInline):
    model = FieldRange


@admin.register(Field)
class FieldAdmin(ModelAdmin):
    model = Field
    inlines = [ValueInline, FieldRangeInline, FieldColumnInline]
    warn_unsaved_form = True
    list_display = ["name", "cell", "row_name", "group_name", "subsection", "section", "version_name", "model_name"]
    list_select_related = ["row", "row__group", "row__group__subsection", "row__group__subsection__section", "row__group__subsection__section__version", "row__group__subsection__section__version__model"]
    search_fields = ["name", "cell", "row__name", "row__group__name", "row__group__subsection__name", "row__group__subsection__section__name", "row__group__subsection__section__version__name", "row__group__subsection__section__version__model__name"]
    readonly_fields = ["model_name", "version_name", "section", "subsection", "group_name"]
    fieldsets = (
        (
            None,
            { "fields": ["model_name", "version_name", "section", "subsection", "group_name", "row"] },
        ),
        (
            "Field",
            { "fields": ["name", "cell", "unit", "display_type"] },
        ),
    )

    @admin.display(description="Model", ordering="row__group__subsection__section__version__model__name")
    def model_name(self, obj):
        return obj.row.group.subsection.section.version.model.name

    @admin.display(description="Version", ordering="row__group__subsection__section__version__name")
    def version_name(self, obj):
        return obj.row.group.subsection.section.version.name

    @admin.display(description="Section", ordering="row__group__subsection__section")
    def section(self, obj):
        return obj.row.group.subsection.section
    
    @admin.display(description="Subsection", ordering="row__group__subsection")
    def subsection(self, obj):
        return obj.row.group.subsection

    @admin.display(description="Group", ordering="row__group__name")
    def group_name(self, obj):
        return obj.row.group.name

    @admin.display(description="Row", ordering="row__name")
    def row_name(self, obj):
        return obj.row.name


class FieldInline(StackedInline):
    model = Field
    ordering_field = "position"
    hide_ordering_field = True
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Row) and obj.field_set.count():
            return 0
        else:
            return 1


class RowInline(StackedInline):
    model = Row
    inlines = [FieldInline]
    ordering_field = "position"
    hide_ordering_field = True
    show_change_link = True
    tab = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Group) and obj.row_set.count():
            return 0
        else:
            return 1


class ColumnInline(TabularInline):
    model = Column
    ordering_field = "position"
    hide_ordering_field = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, ColumnGroup) and obj.column_set.count():
            return 0
        else:
            return 1


class ColumnGroupInline(TabularInline):
    model = ColumnGroup
    inlines = [ColumnInline]
    ordering_field = "position"
    hide_ordering_field = True
    tab = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Group) and obj.columngroup_set.count():
            return 0
        else:
            return 1


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    model = Group
    inlines = [RowInline, ColumnGroupInline]
    warn_unsaved_form = True
    ordering = ["name"]
    list_display = ["name", "is_summary", "subsection", "section", "version_name", "model_name"]
    list_select_related = ["subsection", "subsection__section", "subsection__section__version", "subsection__section__version__model"]
    list_filter = ["is_summary"]
    list_filter_options = { "is_summary": { "label": "Summary Groups", "horizontal": True } }
    search_fields = ["name", "subsection__code", "subsection__name", "subsection__code", "subsection__section__name", "subsection__section__version__name", "subsection__section__version__model__name"]
    readonly_fields = ["model_name", "version_name", "section"]
    fieldsets = (
        (
            None,
            { "fields": ["model_name", "version_name", "section", "subsection"] },
        ),
        (
            "Group",
            { "fields": ["name", "description", "is_summary"] },
        ),
    )

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
    show_change_link = True
    ordering_field = "position"
    hide_ordering_field = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Subsection) and obj.group_set.count():
            return 0
        else:
            return 1


@admin.register(Subsection)
class SubsectionAdmin(ModelAdmin):
    model = Subsection
    inlines = [GroupInline]
    warn_unsaved_form = True
    ordering = ["name"]
    list_display = ["name", "code", "section", "version_name", "model_name"]
    list_select_related = ["section", "section__version", "section__version__model"]
    search_fields = ["name", "code", "description", "model__name", "version_name"]
    readonly_fields = ["model_name", "version_name"]
    fieldsets = (
        (
            None,
            { "fields": ["model_name", "version_name", "section"] },
        ),
        (
            "Subsection",
            { "fields": ["code", "name", "description", "guide"] },
        ),
    )

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
    fields = ["code", "name", "description", "guide"]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Section) and obj.subsection_set.count():
            return 0
        else:
            return 1


class SectionInline(StackedInline):
    model = Section
    inlines = [SubsectionInline]
    fields = ["code", "name"]
    
    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and isinstance(obj, Version) and obj.section_set.count():
            return 0
        else:
            return 1


@admin.register(Version)
class VersionAdmin(ModelAdmin):
    model = Version
    inlines = [SectionInline]
    warn_unsaved_form = True
    list_display = ["name", "model", "url"]
    search_fields = ["name", "url", "model"]
    fields = ["name", "url", "model"]


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
    model = Model
    inlines = [VersionInline]
    warn_unsaved_form = True
    list_display = ("name", "tag_list", "description")
    search_fields = ["name", "description"]

    @admin.display(description="Tags")
    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
