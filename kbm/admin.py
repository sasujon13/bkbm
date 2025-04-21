import nested_admin
from django import forms
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.forms.widgets import HiddenInput
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Teacher, Staff, ExTeacher, ExStaff, OtherPeople, TeacherHonours, NonMpoStaff, Notification, Education, Experience, Dept
from .models import Departments, RelatedImage, TeacherPart, Gallary, Post, PostDetails
# Inline for Education model


class RelatedImageInline(nested_admin.NestedTabularInline):
    model = RelatedImage
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(Caption__in=request.user.depts.all())
        return qs
     
class RelatedPostInline(nested_admin.NestedTabularInline):
    model = PostDetails
    inlines = [RelatedImageInline]
    extra = 1
    # fields = ('Title', 'SubTitle', 'Description', 'Date', 'Comment')  

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(Caption__in=request.user.depts.all())
        return qs

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)

        class CustomForm(formset.form):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                # Hide the field using both HiddenInput and style
                if 'Dept' in self.fields:
                    self.fields['Dept'].widget = HiddenInput(attrs={'style': 'display:none;'})
                    self.fields['Dept'].required = False  # Just in case
                    self.fields['Dept'].disabled = True   # Optional safety
                    if obj:
                        self.initial['Dept'] = obj.pk      # Pre-set the parent Post ID

        formset.form = CustomForm
        return formset

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['Exam', 'Year', 'Result', 'Board_Uni']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['Title', 'Year', 'Description', 'Comment']

class EducationInline(admin.TabularInline):  # or admin.StackedInline if you prefer
    model = Education
    extra = 1
    can_delete = True
    form = EducationForm

class ExperienceInline(admin.TabularInline):  # or admin.StackedInline if you prefer
    model = Experience
    extra = 1
    can_delete = True
    form = ExperienceForm

def completed_button(self, obj):
        if obj.pk:
            move_url = reverse('move_completed_orders', args=[obj.pk])
            return format_html(
                '<div id="move_button"><a class="button move_button" href="{}" target="_blank">Move</a></div><div style="margin-top: 10px; color: red; margin-left:5px; display:none" id="snackbar_container_{}">Error !</div>',
                move_url, obj.pk
            )
        else:
            return '-'

class DepartmentsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    list_display = ('Dept',)
    inlines = [RelatedImageInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
    
    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(Departments, DepartmentsAdmin)

@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'text',)
    search_fields = ('date', 'category', 'text',)
    list_filter = ('category', 'date',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(TeacherPart)
class TeacherPartAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(ExTeacher)
class ExTeacherAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(ExStaff)
class ExStaffAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(OtherPeople)
class OtherPeopleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(TeacherHonours)
class TeacherHonoursAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(NonMpoStaff)
class NonMpoStaffAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 3})},
    }
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

class GallaryAdmin(admin.ModelAdmin):
    list_display = ('Dept',)
    inlines = [RelatedImageInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
    
    def has_delete_permission(self, request, obj=None):
        return False
    
admin.site.register(Gallary, GallaryAdmin)

class PostAdmin(nested_admin.NestedModelAdmin):
    list_display = ('Dept',)
    inlines = [RelatedPostInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
    
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Post, PostAdmin)