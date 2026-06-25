from django.contrib import admin
import nested_admin

from cal_bc.models.models.model import Model, Version, Section, Subsection, Group, Row, Field, Value

class ValueInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Value

    def get_extra(self, request, obj=None, **kwargs):
        return 0


class FieldInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = Field
    inlines = [ValueInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.id is not None and obj.field_set.count():
            return 0
        else:
            return 1


class RowInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = Row
    inlines = [FieldInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.id is not None and obj.row_set.count():
            return 0
        else:
            return 1


@admin.register(Group)
class GroupAdmin(nested_admin.NestedModelAdmin):
    model = Group
    inlines = [RowInline]
    exclude = ["position"]


class GroupInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = Group
    show_change_link = True

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.id is not None and obj.group_set.count():
            return 0
        else:
            return 1


class SubsectionInline(nested_admin.NestedStackedInline):
    model = Subsection
    inlines = [GroupInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.id is not None and obj.subsection_set.count():
            return 0
        else:
            return 1


class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    inlines = [SubsectionInline]

    def get_extra(self, request, obj=None, **kwargs):
        if obj is not None and obj.id is not None and obj.section_set.count():
            return 0
        else:
            return 1


@admin.register(Version)
class VersionAdmin(nested_admin.NestedModelAdmin):
    model = Version
    inlines = [SectionInline]


class VersionInline(nested_admin.NestedTabularInline):
    model = Version
    show_change_link = True


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    inlines = [VersionInline]
