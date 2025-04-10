from django.contrib import admin
from django import forms
from .models import Teacher, Staff, ExTeacher, ExStaff, OtherPeople, TeacherHonours, NonMpoStaff, Notification, Education, Experience
# Inline for Education model


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

    # completed_button.short_description = "Actions" def move_completed_orders(request, pk):

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'text',)
    search_fields = ('date', 'category', 'text',)
    list_filter = ('category', 'date',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(ExTeacher)
class ExTeacherAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(ExStaff)
class ExStaffAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(OtherPeople)
class OtherPeopleAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(TeacherHonours)
class TeacherHonoursAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)

@admin.register(NonMpoStaff)
class NonMpoStaffAdmin(admin.ModelAdmin):
    inlines = [EducationInline, ExperienceInline]
    list_display = ('Name', 'Designation', 'Dept',)
    search_fields = ('Name', 'Designation', 'Dept',)
    list_filter = ('Designation', 'Dept',)
    ordering = ('Order',)
