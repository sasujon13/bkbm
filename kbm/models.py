import os
from django.utils.translation import gettext as _
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.files.storage import default_storage
 
    
class Dept(models.Model):
    Name = models.CharField(max_length=255, null=False, blank=False, unique=True, default='Administration')
    users = models.ManyToManyField(User, related_name='depts')
    def __str__(self):
        return self.Name
    
    
class Teacher(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Tmis = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)  

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class TeacherPart(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Tmis = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class TeacherHonours(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Tmis = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)  

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"   
    

class Staff(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)  

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}" 
    

class NonMpoStaff(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)  

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class ExTeacher(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Tmis = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)  

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class ExStaff(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)  

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
        
class OtherPeople(models.Model):
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.DOB and not self.Retirement:
            self.Retirement = self.DOB + relativedelta(years=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"

class Notification(models.Model):
    CATEGORY = [
        ('HSC', 'HSC'),
        ('Degree', 'Degree'),
        ('Honours', 'Honours'),
        ('BBA', 'BBA'),
        ('BM', 'BM'),
        ('Open Uni.', 'Open Uni'),
        ('Agriculture', 'Agriculture'),
        ('All', 'All')
    ]
    category = models.CharField(max_length=28, choices=CATEGORY, blank=True, null=True)
    text = models.TextField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=512, null=True, blank=True)
    img = models.ImageField(upload_to='images/notification')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.text} {self.link}"


class Education(models.Model): 
    Teacher = models.ForeignKey(Teacher, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    TeacherPart = models.ForeignKey(TeacherPart, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    TeacherHonours = models.ForeignKey(TeacherHonours, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    ExTeacher = models.ForeignKey(ExTeacher, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    Staff = models.ForeignKey(Staff, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    ExStaff = models.ForeignKey(ExStaff, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    NonMpoStaff = models.ForeignKey(NonMpoStaff, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    OtherPeople = models.ForeignKey(OtherPeople, related_name='educations', on_delete=models.CASCADE, null=True, blank=True)
    Exam = models.CharField(max_length=63, blank=True, null=True)
    Year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    Result = models.CharField(max_length=63, blank=True, null=True)
    Board_Uni = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Exam} - {self.Year} {self.Result} - {self.Board_Uni}"


class Experience(models.Model): 
    Teacher = models.ForeignKey(Teacher, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    TeacherPart = models.ForeignKey(TeacherPart, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    TeacherHonours = models.ForeignKey(TeacherHonours, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    ExTeacher = models.ForeignKey(ExTeacher, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    Staff = models.ForeignKey(Staff, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    ExStaff = models.ForeignKey(ExStaff, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    NonMpoStaff = models.ForeignKey(NonMpoStaff, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    OtherPeople = models.ForeignKey(OtherPeople, related_name='experiences', on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=63, blank=True, null=True)
    Year = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    Description = models.CharField(max_length=1024, blank=True, null=True)
    Comment = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Title} - {self.Year} - {self.Description} - {self.Comment}"


# def upload_to_dept_folder(instance, filename):
#     dept_name = 'Admin'

#     if hasattr(instance.content_object, 'Dept') and instance.content_object.Dept:
#         dept_name = instance.content_object.Dept.Name

#     # dept_name = dept_name.replace(' ', '_')
#     return os.path.join('images', dept_name, filename)
def upload_to_dept_folder(instance, filename):
    dept_name = 'Admin'  # default fallback

    try:
        if instance.post_detail and instance.post_detail.post and instance.post_detail.post.dept:
            dept_name = instance.post_detail.post.dept.Name
    except AttributeError:
        pass

    return os.path.join('images', dept_name, filename)


class RelatedImage(models.Model):
    Dept = models.ForeignKey('Dept', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    Departments = models.ForeignKey('Departments', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    PostDetails = models.ForeignKey('PostDetails', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    Gallary = models.ForeignKey('Gallary', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    Img = models.ImageField(upload_to=upload_to_dept_folder, null=True, blank=True)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    Caption = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            old = RelatedImage.objects.get(pk=self.pk)
            if old.Img and not self.Img:
                if default_storage.exists(old.Img.name):
                    default_storage.delete(old.Img.name)
                    print(f"Cleared and deleted file: {old.Img.name}")
                self.delete()
                return
            elif old.Img and old.Img != self.Img:
                if default_storage.exists(old.Img.name):
                    default_storage.delete(old.Img.name)
                    print(f"Replaced and deleted old file: {old.Img.name}")
        except RelatedImage.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.Img and default_storage.exists(self.Img.name):
            default_storage.delete(self.Img.name)
            print(f"Deleted file from media: {self.Img.name}")
        super().delete(*args, **kwargs)

    def __str__(self):
        return ""


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    Dept = models.ForeignKey('Dept', on_delete=models.CASCADE, null=False, blank=False, default=99, editable=False)
    Img = GenericRelation(RelatedImage)
    Title = models.CharField(max_length=63, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Photo = models.ImageField(upload_to='images/depts', blank=True, null=True)
    TitlePhoto = models.CharField(max_length=63, blank=True, null=True)
    DescriptionPhoto = models.CharField(max_length=2048, blank=True, null=True)
    TitleRoutine = models.CharField(max_length=63, blank=True, null=True)
    ImgRoutine = GenericRelation(RelatedImage)

    def __str__(self):
        return f"{self.Dept}"


class PostDetails(models.Model):
    id = models.AutoField(primary_key=True)
    Dept = models.ForeignKey('Dept', on_delete=models.CASCADE, null=False, blank=False, default=99, editable=False)
    Post = models.ForeignKey('Post', on_delete=models.CASCADE, null=False, blank=False, default=99, editable=False)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    Title = models.CharField(max_length=255, blank=True, null=True)
    SubTitle = models.CharField(max_length=255, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Date = models.DateField(null=True, blank=True)
    Comment = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        try:
            old = RelatedImage.objects.get(pk=self.pk)
            if old.Img and not self.Img:
                if default_storage.exists(old.Img.name):
                    default_storage.delete(old.Img.name)
                    print(f"Cleared and deleted file: {old.Img.name}")
                self.delete()
                return
            elif old.Img and old.Img != self.Img:
                if default_storage.exists(old.Img.name):
                    default_storage.delete(old.Img.name)
                    print(f"Replaced and deleted old file: {old.Img.name}")
        except RelatedImage.DoesNotExist:
            pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.Img and default_storage.exists(self.Img.name):
            default_storage.delete(self.Img.name)
            print(f"Deleted file from media: {self.Img.name}")
        super().delete(*args, **kwargs)

    def __str__(self):
        return ""


class Post(models.Model):
    Dept = models.ForeignKey('Dept', on_delete=models.CASCADE, null=False, blank=False, default=99, editable=False)
    PostDetails = GenericRelation(PostDetails)
    Img = GenericRelation(RelatedImage)

    def __str__(self):
        return f"{self.Dept}"


class Gallary(models.Model):
    Dept = models.ForeignKey('Dept', on_delete=models.CASCADE, null=False, blank=False, default=99, editable=False)
    Img = GenericRelation(RelatedImage)

    def __str__(self):
        return f"{self.Dept}"