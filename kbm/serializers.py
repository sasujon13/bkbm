from rest_framework import serializers
from .models import Teacher, Staff, ExTeacher, Departments
from .models import ExStaff, OtherPeople, TeacherHonours, NonMpoStaff, Notification, TeacherPart, Dept, RelatedImage


class DeptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dept
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return '' 

class TeacherPartSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = TeacherPart
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return '' 

class StaffSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return '' 

class ExTeacherSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ExTeacher
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return '' 

class ExStaffSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = ExStaff
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return '' 

class OtherPeopleSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = OtherPeople
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return ''
    

class TeacherHonoursSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = TeacherHonours
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return ''
    

class NonMpoStaffSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = NonMpoStaff
        fields = '__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.Img and hasattr(obj.Img, 'url'):
            return request.build_absolute_uri(obj.Img.url)
        return ''
    

class RelatedImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = RelatedImage
        fields = ['caption', 'image']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return ''
    

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
    

class DepartmentsSerializer(serializers.ModelSerializer):
    img = RelatedImageSerializer(source='Img', many=True, read_only=True)

    class Meta:
        model = Departments
        fields = '__all__'
