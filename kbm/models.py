from django.utils.translation import gettext as _
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
 
    
class Dept(models.Model):
    Name = models.CharField(max_length=255, null=True, blank=True)

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
    

class RelatedImage(models.Model):
    image = models.ImageField(upload_to='images/depts')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.content_object}"


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True)
    Img = GenericRelation(RelatedImage)
    Title = models.CharField(max_length=63, blank=True, null=True)
    Description = models.CharField(max_length=2048, blank=True, null=True)
    Photo = models.ImageField(upload_to='images/depts', blank=True, null=True)
    TitlePhoto = models.CharField(max_length=63, blank=True, null=True)
    DescriptionPhoto = models.CharField(max_length=2048, blank=True, null=True)
    TitleRoutine = models.CharField(max_length=63, blank=True, null=True)
    ImgRoutine = GenericRelation(RelatedImage)


class Post(models.Model): 
    Departments = models.ForeignKey(Departments, related_name='departments', on_delete=models.CASCADE, null=True, blank=True)
    Title = models.CharField(max_length=255, blank=True, null=True)
    SubTitle = models.CharField(max_length=255, blank=True, null=True)
    Img = GenericRelation(RelatedImage)
    Description = models.CharField(max_length=1024, blank=True, null=True)
    Date = models.DateField(null=True, blank=True)
    Comment = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.Title} - {self.SubTitle} - {self.Description} - {self.Date}"