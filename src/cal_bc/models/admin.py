import nested_admin
from django.contrib import admin

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

admin.AdminSite.site_header = "Cal B/C Admin"

class ValueInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Value
    extra = 0


class FieldColumnInline(nested_admin.NestedTabularInline):
    model = Field.column.through
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "column" and request.resolver_match.kwargs:
            kwargs["queryset"] = Column.objects.filter(
                column_group__group=request.resolver_match.kwargs["object_id"]
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FieldRangeInline(nested_admin.NestedTabularInline):
    model = FieldRange
    extra = 0


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


class ColumnGroupInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
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
    ordering = ["name"]
    list_display = ["name", "display_type", "subsection", "section", "version_name", "model_name"]
    list_select_related = ["subsection", "subsection__section", "subsection__section__version", "subsection__section__version__model"]
    search_fields = ["name", "subsection__code", "subsection__name", "subsection__code", "subsection__section__name", "subsection__section__version__name", "subsection__section__version__model__name"]
    search_help_text = "Search by Name, Model, Version, Section, and Subsection"
    readonly_fields = ["model_name", "version_name", "section"]
    fieldsets = (
        (
            None,
            { "fields": ["model_name", "version_name", "section", "subsection"] },
        ),
        (
            "GROUP",
            { "fields": ["name", "description", "guide", "display_type"] },
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


class GroupInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Group
    exclude = ["guide"]
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.group_set.count():
            return 0
        else:
            return 1


class SubsectionInline(nested_admin.NestedStackedInline):
    model = Subsection
    inlines = [GroupInline]
    fields = ["code", "name", "description", "guide"]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.subsection_set.count():
            return 0
        else:
            return 1


class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    inlines = [SubsectionInline]
    fields = ["code", "name"]
    
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
    search_fields = ["name", "model__name", "url"]
    search_help_text = "Search by Name, Model, and URL"
    fields = ["name", "url", "model"]


@admin.register(Subsection)
class SubsectionAdmin(nested_admin.NestedModelAdmin):
    model = Subsection
    list_select_related = ["section", "section__version", "section__version__model"]
    readonly_fields = ["model_name", "version_name"]
    fieldsets = (
        (
            None,
            { "fields": ["model_name", "version_name", "section"] },
        ),
        (
            "SUBSECTION",
            { "fields": ["code", "name", "description", "guide"] },
        ),
    )

    def has_module_permission(self, request):
        # Hide the module on the admin index page
        return False

    @admin.display(description="Model")
    def model_name(self, obj):
        return obj.section.version.model.name

    @admin.display(description="Version")
    def version_name(self, obj):
        return obj.section.version.name


@admin.register(Section)
class SectionAdmin(nested_admin.NestedModelAdmin):
    model = Section
    list_select_related = ["version_name", "version__model"]
    readonly_fields = ["model_name", "version_name"]
    fieldsets = (
        (
            None,
            { "fields": ["model_name", "version_name"] },
        ),
        (
            "SECTION",
            { "fields": ["code", "name"] },
        ),
    )

    def has_module_permission(self, request):
        # Hide the module on the admin index page
        return False

    @admin.display(description="Model")
    def model_name(self, obj):
        return obj.version.model.name

    @admin.display(description="Version")
    def version_name(self, obj):
        return obj.version.name


class VersionInline(nested_admin.NestedTabularInline):
    model = Version
    show_change_link = True


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    model = Model
    inlines = [VersionInline]
    list_display = ("name", "tag_list", "description")
    search_fields = ["name", "description"]
    search_help_text = "Search by Name and Description"

    @admin.display(description="Tags")
    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
