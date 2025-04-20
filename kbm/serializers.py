from rest_framework import serializers
from .models import Teacher, Staff, ExTeacher, Departments, Gallary, Post
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
    class Meta:
        model = RelatedImage
        fields = ['Img', 'Caption']

    def get_Img(self, obj):
        dept_name = self.context.get('filter_dept_Name')
        images = obj.Img.all()

        # Just check if the gallery's Dept matches, skip filtering RelatedImage by Dept
        if dept_name and obj.Dept.Name != dept_name:
            return []

        return RelatedImageSerializer(images, many=True, context=self.context).data
    

class GallarySerializer(serializers.ModelSerializer):
    Img = serializers.SerializerMethodField()
    Dept = serializers.CharField(source='Dept.Name', read_only=True)

    class Meta:
        model = Gallary
        fields = ['Dept', 'Img']

    def get_Img(self, obj):
        images = obj.Img.all()  # This only includes images attached to this object
        return RelatedImageSerializer(images, many=True, context=self.context).data


        # if dept_name:
        #     images = images.filter(Dept__Name=dept_name)

        # return RelatedImageSerializer(images, many=True, context=self.context).data
    

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
    

class DepartmentsSerializer(serializers.ModelSerializer):
    img = RelatedImageSerializer(source='Img', many=True, read_only=True)

    class Meta:
        model = Departments
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    img = RelatedImageSerializer(source='Img', many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
