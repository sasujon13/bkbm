from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .location import Bangladesh
import logging
from .models import Teacher, ExTeacher, Staff, ExStaff, OtherPeople, TeacherHonours, NonMpoStaff, Notification, TeacherPart, Dept, Departments
from .serializers import TeacherSerializer, ExTeacherSerializer, StaffSerializer, ExStaffSerializer, OtherPeopleSerializer, TeacherHonoursSerializer, NonMpoStaffSerializer, NotificationSerializer, TeacherPartSerializer, DeptSerializer, DepartmentsSerializer


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class DivisionsView(APIView):
    def get(self, request):
        divisions = list(Bangladesh.keys())
        return Response(divisions)


class DistrictsView(APIView):
    def get(self, request):
        division = request.query_params.get('division')
        if division in Bangladesh:
            districts = list(Bangladesh[division].keys())
            return Response(districts)
        return Response([])


class ThanasView(APIView):
    def get(self, request):
        division = request.query_params.get('division')
        district = request.query_params.get('district')
        if division in Bangladesh and district in Bangladesh[division]:
            thanas = Bangladesh[division][district]
            return Response(thanas)
        return Response([])
 

class TeacherListAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True, context={'request': request})
        return Response(serializer.data) 

class DeptListAPIView(APIView):
    def get(self, request):
        depts = Dept.objects.all()
        serializer = DeptSerializer(depts, many=True, context={'request': request})
        return Response(serializer.data)  

class TeacherPartListAPIView(APIView):
    def get(self, request):
        teachersPart = TeacherPart.objects.all()
        serializer = TeacherPartSerializer(teachersPart, many=True, context={'request': request})
        return Response(serializer.data)    

class ExTeacherListAPIView(APIView):
    def get(self, request):
        exTeachers = ExTeacher.objects.all()
        serializer = ExTeacherSerializer(exTeachers, many=True, context={'request': request})
        return Response(serializer.data)    

class StaffListAPIView(APIView):
    def get(self, request):
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True, context={'request': request})
        return Response(serializer.data)    

class ExStaffListAPIView(APIView):
    def get(self, request):
        exStaffs = ExStaff.objects.all()
        serializer = ExStaffSerializer(exStaffs, many=True, context={'request': request})
        return Response(serializer.data)    

class OtherPeopleListAPIView(APIView):
    def get(self, request):
        otherPeoples = OtherPeople.objects.all()
        serializer = OtherPeopleSerializer(otherPeoples, many=True, context={'request': request})
        return Response(serializer.data)
    
class TeacherHonoursListAPIView(APIView):
    def get(self, request):
        teacherHonours = TeacherHonours.objects.all()
        serializer = TeacherHonoursSerializer(teacherHonours, many=True, context={'request': request})
        return Response(serializer.data)
    
class NonMpoStaffListAPIView(APIView):
    def get(self, request):
        nonMpoStaffs = NonMpoStaff.objects.all()
        serializer = NonMpoStaffSerializer(nonMpoStaffs, many=True, context={'request': request})
        return Response(serializer.data)
    
class NotificationExistsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        notification = Notification.objects.all()
        serializer = NotificationSerializer(notification, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DepartmentDetailView(RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    
    def get_object(self):
        dept_name = self.kwargs.get('Name')  # this is from the URL
        try:
            return Departments.objects.get(Name__Name=dept_name)
        except Departments.DoesNotExist:
            raise NotFound("Department not found.")
