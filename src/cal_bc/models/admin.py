from functools import partial

import django_admin_tables
import nested_admin
from django.contrib import admin
from django.db import transaction
from django.urls import reverse
from django.utils.html import format_html

from cal_bc.models.forms.model import ChoiceForm, FieldForm
from cal_bc.models.models.model import (
    Choice,
    ChoiceGroup,
    Column,
    ColumnGroup,
    Field,
    FieldRange,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
    VersionFile,
    VersionFileNamedCell,
    VersionFileSheet,
)
from cal_bc.models.tasks import refresh_version_file_details, update_version_file

admin.AdminSite.site_header = "Cal-B/C Admin"


class ChoiceInline(django_admin_tables.AdminTablesMixin, nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Choice
    form = ChoiceForm
    extra = 0
    radio_select_exclusive_fields = ["is_selected"]


class ChoiceGroupInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = ChoiceGroup
    inlines = [ChoiceInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.pk is not None and obj.choicegroup_set.count():
            return 0
        else:
            return 1


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
    form = FieldForm
    inlines = [FieldColumnInline, FieldRangeInline, ChoiceGroupInline]

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
    list_display = ["name", "is_summary", "subsection", "section", "version_name", "model_name"]
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
            { "fields": ["name", "description", "guide", "is_summary"] },
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
    show_change_link = True

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

class VersionFileSheetInline(nested_admin.NestedTabularInline):
    model = VersionFileSheet
    readonly_fields = ["name"]
    classes = ["collapse", "hide-original-rows"]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    class Media:
        css = {
            "all": ["admin/css/custom.css"]
        }
    

class VersionFileNamedCellInline(nested_admin.NestedTabularInline):
    model = VersionFileNamedCell
    fields = ["display_cell"]
    readonly_fields = ["display_cell"]
    classes = ['collapse']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description="Cells")
    def display_cell(self, obj):
        return "!".join([item.strip() for item in obj.cell.replace("$","").strip("[]()'").split("', '")])


@admin.register(VersionFile)
class VersionFileAdmin(nested_admin.NestedModelAdmin):
    model = VersionFile
    inlines = [VersionFileSheetInline, VersionFileNamedCellInline]
    list_display = ["__str__", "file", "version_name", "model_name"]

    def has_module_permission(self, request):
        # Hide the module on the admin index page
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    @admin.display(description="Model", ordering="version__model__name")
    def model_name(self, obj):
        return obj.version.model.name

    @admin.display(description="Version", ordering="version__model__name")
    def version_name(self, obj):
        return obj.version.name


class VersionFileInline(nested_admin.NestedTabularInline):
    model = VersionFile
    readonly_fields = ["count_link"]
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    @admin.display(description="Details")
    def count_link(self, obj):
        if obj.pk:
            named_cells_count = obj.versionfilenamedcell_set.count()
            sheets_count = obj.versionfilesheet_set.count()
            url = reverse("admin:models_versionfile_change", args=[obj.pk])
            return format_html('<a href="{}">{}</a>', url, f"{sheets_count} Sheets and {named_cells_count} Named Cells")
        else:
            return "-"

    @admin.display(description="Named Cells Count")
    def named_cell_count_link(self, obj):
        if obj.pk:
            count = obj.versionfilenamedcell_set.count()
            url = reverse("admin:models_versionfile_change", args=[obj.pk])
            return format_html('<a href="{}">{}</a>', url, count)
        else:
            return "-"

    @admin.display(description="Sheets Count")
    def sheet_count_link(self, obj):
        if obj.pk:
            count = obj.versionfilesheet_set.count()
            url = reverse("admin:models_versionfile_change", args=[obj.pk])
            return format_html('<a href="{}">{}</a>', url, count)
        else:
            return "-"


@admin.register(Version)
class VersionAdmin(nested_admin.NestedModelAdmin):
    model = Version
    inlines = [VersionFileInline, SectionInline]
    list_display = ["name", "model", "url"]
    search_fields = ["name", "model__name", "url"]
    search_help_text = "Search by Name, Model, and URL"
    fields = ["name", "url", "model"]
    
    def save_related(self, request, form, formsets, change):
        # Trigger refresh_version_file_details when a new file is manually uploaded
        inline_changed = any(formset.has_changed() for formset in formsets if formset.model == VersionFile)
        
        with transaction.atomic():
            super().save_related(request, form, formsets, change)

            for formset in formsets:
                if formset.model == VersionFile:
                    if inline_changed:
                        transaction.on_commit(partial(refresh_version_file_details.enqueue, version_file_pk=formset.new_objects[0].pk))
                    elif len(formset.deleted_objects) == 0 and not hasattr(formset.instance, "versionfile"):
                        transaction.on_commit(partial(update_version_file.enqueue, version_pk=formset.instance.pk))
                    elif (len(formset.deleted_objects) == 0 and hasattr(formset.instance, "versionfile") and
                          (not formset.instance.versionfile.versionfilesheet_set.exists() or
                           not formset.instance.versionfile.versionfilenamedcell_set.exists())):
                        transaction.on_commit(partial(refresh_version_file_details.enqueue, version_file_pk=formset.instance.versionfile.id))

    def save_model(self, request, obj, form, change):
        # Trigger update_version_file when a new Version is created or the url is updated
        with transaction.atomic():
            super().save_model(request, obj, form, change)
            if obj is not None and change and 'url' in form.changed_data and form.initial.get('url') != obj.url:
                transaction.on_commit(partial(update_version_file.enqueue, version_pk=obj.pk))


@admin.register(Subsection)
class SubsectionAdmin(nested_admin.NestedModelAdmin):
    model = Subsection
    inlines = [GroupInline]
    list_display = ["__str__", "section", "version_name", "model_name"]
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

    @admin.display(description="Model", ordering="section__version__model__name")
    def model_name(self, obj):
        return obj.section.version.model.name

    @admin.display(description="Version", ordering="section__version__model__name")
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

    def has_change_permission(self, request, obj=None):
        return False


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

    def save_related(self, request, form, formsets, change):
        # Trigger update_version_file when a new version is created
        inline_changed = any(formset.has_changed() for formset in formsets if formset.model == Version)
        
        with transaction.atomic():
            super().save_related(request, form, formsets, change)
            if inline_changed:
                for formset in formsets:
                    if formset.model == Version:
                        transaction.on_commit(partial(update_version_file.enqueue, version_pk=formset.new_objects[0].pk))
