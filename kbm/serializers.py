from rest_framework import serializers
from .models import Teacher, Staff, ExTeacher, Departments, Gallary
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
        fields = ['Dept', 'Img', 'Caption']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return ''
    


class GallarySerializer(serializers.ModelSerializer):
    Img = RelatedImageSerializer(many=True, read_only=True)
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    Dept = serializers.PrimaryKeyRelatedField(
        queryset=Dept.objects.all(), write_only=True
    )

    class Meta:
        model = Gallary
        fields = ['Caption', 'Img', 'images', 'Dept']

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        dept = validated_data.pop('Dept', None)
        gallary = Gallary.objects.create(**validated_data)

        for img in images:
            RelatedImage.objects.create(
                Dept=dept,
                image=img,
                content_object=gallary
            )
        return gallary
    

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
    

class DepartmentsSerializer(serializers.ModelSerializer):
    img = RelatedImageSerializer(source='Img', many=True, read_only=True)

    class Meta:
        model = Departments
        fields = '__all__'
