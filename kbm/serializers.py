from rest_framework import serializers
from .models import Item, Customer, Order, Ordered, OrderDetail, Transaction, Teacher, Staff, ExTeacher, ExStaff, OtherPeople, TeacherHonours, NonMpoStaff, Notification

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fullName', 'gender', 'division', 'district', 'thana', 'union', 'village']

    def update(self, instance, validated_data):
        # Exclude 'username' and 'password' fields from the update
        validated_data.pop('username', None)
        validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderDetails = OrderDetailSerializer(many=True, read_only=True)
    transaction = TransactionSerializer(many=True, read_only=True)
    class Meta:
        model = Order
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
    

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'