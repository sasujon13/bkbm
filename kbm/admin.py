from django.contrib import admin
from .models import Teacher, Staff, ExTeacher, ExStaff, OtherPeople, TeacherHonours, NonMpoStaff

admin.site.register(Teacher)
admin.site.register(Staff)
admin.site.register(ExTeacher)
admin.site.register(ExStaff)
admin.site.register(OtherPeople)
admin.site.register(TeacherHonours)
admin.site.register(NonMpoStaff)


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
