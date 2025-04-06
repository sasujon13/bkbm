from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import User

class Item(models.Model):
    SIZE = [
        ('XS', 'Extra_small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra_large'),
        ('XXL', 'Ultra_large'),
    ]
    code = models.CharField(max_length=4, unique=True, blank=False, null=True)
    name = models.CharField(max_length=63, blank=False, null=True)
    bangla_name = models.CharField(max_length=63, blank=False, null=True)
    size = models.CharField(max_length=14, choices=SIZE, blank=False, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    love = models.BooleanField(default=False, blank=False, null=True)
    add_to_cart = models.BooleanField(default=False, blank=False, null=True)
    discount = models.DecimalField(max_digits=2, decimal_places=0, default=0, blank=False, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)
    probable_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=False, null=True)
    PAYMENT_CHOICES = [
        ('Cash on Deilivery', 'cod'),
        ('bKash', 'bkash'),
        ('Nagad', 'nagad'),
        ('DBBL', 'dbbl'),
        ('Other', 'other'),
    ]
    CATEGORY = [
        ('Sea kbm', 'Sea kbm'),
        ('River kbm', 'River kbm'),
        ('Pond kbm', 'Pond kbm'),
        ('Bill kbm', 'Bill kbm'),
        ('other', 'Other'),
    ]
    TYPES = [
        ('Dry', 'Dry'),
        ('Soft', 'Soft'),
    ]
    VARIENTS = [
        ('Whole kbm', 'Whole kbm'),
        ('Half', 'Half'),
        ('One Third', 'One Third'),
        ('Quarter', 'Quarter'),
        ('NA', 'NA'),
    ]
    category = models.CharField(max_length=28, choices=CATEGORY, blank=False, null=True)
    supplier = models.CharField(max_length=54, blank=False, null=True)
    variants = models.CharField(max_length=15, choices=VARIENTS, blank=False, null=True, default="NA")
    types = models.CharField(max_length=15, choices=TYPES, blank=False, null=True, default="Soft")
    reviews = models.TextField(blank=False, null=True, default="Rated By @Author")
    ratings = models.DecimalField(max_digits=3, decimal_places=2, default="5", blank=False, null=True)
    shipping = models.TextField(max_length=14, blank=False, null=True, default="NA")
    in_stock = models.IntegerField(blank=False, null=True)
    payment_method = models.CharField(max_length=28, choices=PAYMENT_CHOICES, default="bKash", blank=False, null=True)
    details = models.TextField(max_length=512, blank=False, null=True, default="NA")
    videos = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    username = models.CharField(max_length=11, null=True, blank=True, default='')
    trxid = models.CharField(max_length=31, unique=True, default='')
    paidFrom = models.CharField(max_length=31, default='')
    Paid = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)

    def __str__(self):
        return self.trxid
    

class OrderDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    SN = models.IntegerField()
    Name = models.CharField(max_length=127)
    Image = models.URLField()
    Weight = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)
    Quantity = models.IntegerField(blank=False, null=True)
    Discount = models.DecimalField(max_digits=9, decimal_places=0, blank=False, null=True)
    Total = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)
    GrandTotal = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)
    Paid = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)
    Due = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=True)
    ShipingCost = models.DecimalField(max_digits=8, decimal_places=0, blank=False, null=True)

    def __str__(self):
        return self.Name

class Order(models.Model):
    division = models.CharField(max_length=31, null=True, blank=True)
    district = models.CharField(max_length=31, null=True, blank=True)
    thana = models.CharField(max_length=31, null=True, blank=True)
    paymentMethod = models.CharField(max_length=31, null=True, blank=True)
    username = models.CharField(max_length=11)
    fullName = models.CharField(max_length=31, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    union = models.CharField(max_length=31, null=True, blank=True)
    village = models.TextField(max_length=255, null=True, blank=True)
    altMobileNo = models.CharField(max_length=11, null=True, blank=True)
    orderDetails = models.ManyToManyField(OrderDetail, blank=True)
    transaction = models.ManyToManyField(Transaction, blank=True)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Ordered(models.Model):
    division = models.CharField(max_length=31, null=True, blank=True)
    district = models.CharField(max_length=31, null=True, blank=True)
    thana = models.CharField(max_length=31, null=True, blank=True)
    paymentMethod = models.CharField(max_length=31, null=True, blank=True)
    username = models.CharField(max_length=11)
    fullName = models.CharField(max_length=31, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    union = models.CharField(max_length=31, null=True, blank=True)
    village = models.TextField(max_length=255, null=True, blank=True)
    altMobileNo = models.CharField(max_length=11, null=True, blank=True)
    orderDetails = models.ManyToManyField(OrderDetail, blank=True)
    transaction = models.ManyToManyField(Transaction, blank=True)
    shipped = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    

class Canceled(models.Model):
    division = models.CharField(max_length=31, null=True, blank=True)
    district = models.CharField(max_length=31, null=True, blank=True)
    thana = models.CharField(max_length=31, null=True, blank=True)
    paymentMethod = models.CharField(max_length=31, null=True, blank=True)
    username = models.CharField(max_length=11)
    fullName = models.CharField(max_length=31, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    union = models.CharField(max_length=31, null=True, blank=True)
    village = models.TextField(max_length=255, null=True, blank=True)
    altMobileNo = models.CharField(max_length=11, null=True, blank=True)
    orderDetails = models.ManyToManyField(OrderDetail, blank=True)
    transaction = models.ManyToManyField(Transaction, blank=True)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class CustomerManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Mobile Number must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Common', 'Common'),
    ]
    username = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=128) 
    fullName = models.CharField(max_length=31)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    division = models.CharField(max_length=31)
    district = models.CharField(max_length=31)
    thana = models.CharField(max_length=31)
    union = models.CharField(max_length=31, blank=True)
    village = models.CharField(max_length=255)

    objects = CustomerManager()

    USERNAME_FIELD = "username"

    groups = models.ManyToManyField(Group, related_name="customer_set", blank=True)
    
    user_permissions = models.ManyToManyField(
        Permission, related_name="customer_set", blank=True
    )

    def __str__(self):
        return self.fullName

    def get_full_name(self):
        return self.fullName

    def get_short_name(self):
        return self.fullName

    

class CustomerToken(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    key = models.CharField("Key", max_length=40, primary_key=True)
    created = models.DateTimeField("Created", default=timezone.now)

    def __str__(self):
        return f"Token for {self.customer.username}"
    

class JsonData(models.Model):
    data = models.JSONField()

    def __str__(self):
        return f"JSON Data #{self.id}"


class Employee(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Common', 'Common'),
    ]
    user = models.CharField(max_length=8, unique=True, blank=False, null=False)
    name = models.CharField(max_length=63, blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True, choices=GENDER_CHOICES)
    fathersName = models.CharField(max_length=63, blank=True, null=True)
    mothersName = models.CharField(max_length=63, blank=True, null=True)
    husband = models.CharField(max_length=63, blank=True, null=True)
    designation = models.CharField(max_length=63, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    index = models.CharField(max_length=14, blank=True, null=True)
    joiningDate = models.DateTimeField(blank=True, null=True)
    bankAccount = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    teacherOrStaff = models.BooleanField(default=False, blank=True, null=True)
    mpoOrHonours = models.BooleanField(default=False, blank=True, null=True)
    password = models.CharField(blank=True, null=True, max_length=14)
    bloodGroup = models.CharField(max_length=14, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    comments = models.TextField(max_length=2047, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.user} {self.password}"
    
    
class Institute(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    pInstitute = models.CharField(max_length=127, blank=True, null=True)
    pijd = models.DateTimeField(blank=True, null=True)
    pird = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
    
    
class Address(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    division = models.CharField(max_length=31, blank=True, null=True)
    district = models.CharField(max_length=31, blank=True, null=True)
    thana = models.CharField(max_length=31, blank=True, null=True)
    union = models.CharField(max_length=31, blank=True, null=True)
    postCode = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


class Education(models.Model):   
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    exam = models.CharField(max_length=63, blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    passingYear = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    grade = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    maxGrade = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    pClass = models.CharField(max_length=63, blank=True, null=True)
    boardUniversity = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


class Profile(models.Model):   
    user = models.CharField(max_length=8, unique=True, blank=False, null=False)
    title = models.CharField(max_length=63, blank=True, null=True)
    description = models.TextField(max_length=4095, blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.title}"
    

class Teacher(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models. TextField(null=True, blank=True)
    PerAddress = models. TextField(null=True, blank=True)
    SSC = models. TextField(null=True, blank=True)
    HSC = models. TextField(null=True, blank=True)
    Degree = models. TextField(null=True, blank=True)
    Honours = models. TextField(null=True, blank=True)
    PreMasters = models. TextField(null=True, blank=True)
    Masters = models. TextField(null=True, blank=True)
    SSC_Year = models. TextField(null=True, blank=True)
    HSC_Year = models. TextField(null=True, blank=True)
    Degree_Year = models. TextField(null=True, blank=True)
    Honours_Year = models. TextField(null=True, blank=True)
    PreMasters_Year = models. TextField(null=True, blank=True)
    Masters_Year = models. TextField(null=True, blank=True)
    SSC_Result = models. TextField(null=True, blank=True)
    HSC_Result = models. TextField(null=True, blank=True)
    Degree_Result = models. TextField(null=True, blank=True)
    Honours_Result = models. TextField(null=True, blank=True)
    PreMasters_Result = models. TextField(null=True, blank=True)
    Masters_Result = models. TextField(null=True, blank=True)
    SSC_Board = models. TextField(null=True, blank=True)
    HSC_Board = models. TextField(null=True, blank=True)
    Degree_U = models. TextField(null=True, blank=True)
    Honours_U = models. TextField(null=True, blank=True)
    PreMasters_U = models. TextField(null=True, blank=True)
    Masters_U = models. TextField(null=True, blank=True)
    Experience = models. TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class TeacherHonours(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models. TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    SSC = models.TextField(null=True, blank=True)
    HSC = models.TextField(null=True, blank=True)
    Degree = models.TextField(null=True, blank=True)
    Honours = models.TextField(null=True, blank=True)
    PreMasters = models.TextField(null=True, blank=True)
    Masters = models.TextField(null=True, blank=True)
    SSC_Year = models.TextField(null=True, blank=True)
    HSC_Year = models.TextField(null=True, blank=True)
    Degree_Year = models.TextField(null=True, blank=True)
    Honours_Year = models.TextField(null=True, blank=True)
    PreMasters_Year = models.TextField(null=True, blank=True)
    Masters_Year = models.TextField(null=True, blank=True)
    SSC_Result = models.TextField(null=True, blank=True)
    HSC_Result = models.TextField(null=True, blank=True)
    Degree_Result = models.TextField(null=True, blank=True)
    Honours_Result = models.TextField(null=True, blank=True)
    PreMasters_Result = models.TextField(null=True, blank=True)
    Masters_Result = models.TextField(null=True, blank=True)
    SSC_Board = models.TextField(null=True, blank=True)
    HSC_Board = models.TextField(null=True, blank=True)
    Degree_U = models.TextField(null=True, blank=True)
    Honours_U = models.TextField(null=True, blank=True)
    PreMasters_U = models.TextField(null=True, blank=True)
    Masters_U = models.TextField(null=True, blank=True)
    Experience = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"   
    

class Staff(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    SSC = models.TextField(null=True, blank=True)
    HSC = models.TextField(null=True, blank=True)
    Degree = models.TextField(null=True, blank=True)
    Honours = models.TextField(null=True, blank=True)
    PreMasters = models.TextField(null=True, blank=True)
    Masters = models.TextField(null=True, blank=True)
    SSC_Year = models.TextField(null=True, blank=True)
    HSC_Year = models.TextField(null=True, blank=True)
    Degree_Year = models.TextField(null=True, blank=True)
    Honours_Year = models.TextField(null=True, blank=True)
    PreMasters_Year = models.TextField(null=True, blank=True)
    Masters_Year = models.TextField(null=True, blank=True)
    SSC_Result = models.TextField(null=True, blank=True)
    HSC_Result = models.TextField(null=True, blank=True)
    Degree_Result = models.TextField(null=True, blank=True)
    Honours_Result = models.TextField(null=True, blank=True)
    PreMasters_Result = models.TextField(null=True, blank=True)
    Masters_Result = models.TextField(null=True, blank=True)
    SSC_Board = models.TextField(null=True, blank=True)
    HSC_Board = models.TextField(null=True, blank=True)
    Degree_U = models.TextField(null=True, blank=True)
    Honours_U = models.TextField(null=True, blank=True)
    PreMasters_U = models.TextField(null=True, blank=True)
    Masters_U = models.TextField(null=True, blank=True)
    Experience = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True)  # Stored in MEDIA folder

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}" 
    

class NonMpoStaff(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    SSC = models.TextField(null=True, blank=True)
    HSC = models.TextField(null=True, blank=True)
    Degree = models.TextField(null=True, blank=True)
    Honours = models.TextField(null=True, blank=True)
    PreMasters = models.TextField(null=True, blank=True)
    Masters = models.TextField(null=True, blank=True)
    SSC_Year = models.TextField(null=True, blank=True)
    HSC_Year = models.TextField(null=True, blank=True)
    Degree_Year = models.TextField(null=True, blank=True)
    Honours_Year = models.TextField(null=True, blank=True)
    PreMasters_Year = models.TextField(null=True, blank=True)
    Masters_Year = models.TextField(null=True, blank=True)
    SSC_Result = models.TextField(null=True, blank=True)
    HSC_Result = models.TextField(null=True, blank=True)
    Degree_Result = models.TextField(null=True, blank=True)
    Honours_Result = models.TextField(null=True, blank=True)
    PreMasters_Result = models.TextField(null=True, blank=True)
    Masters_Result = models.TextField(null=True, blank=True)
    SSC_Board = models.TextField(null=True, blank=True)
    HSC_Board = models.TextField(null=True, blank=True)
    Degree_U = models.TextField(null=True, blank=True)
    Honours_U = models.TextField(null=True, blank=True)
    PreMasters_U = models.TextField(null=True, blank=True)
    Masters_U = models.TextField(null=True, blank=True)
    Experience = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True)  # Stored in MEDIA folder

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class ExTeacher(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    SSC = models.TextField(null=True, blank=True)
    HSC = models.TextField(null=True, blank=True)
    Degree = models.TextField(null=True, blank=True)
    Honours = models.TextField(null=True, blank=True)
    PreMasters = models.TextField(null=True, blank=True)
    Masters = models.TextField(null=True, blank=True)
    SSC_Year = models.TextField(null=True, blank=True)
    HSC_Year = models.TextField(null=True, blank=True)
    Degree_Year = models.TextField(null=True, blank=True)
    Honours_Year = models.TextField(null=True, blank=True)
    PreMasters_Year = models.TextField(null=True, blank=True)
    Masters_Year = models.TextField(null=True, blank=True)
    SSC_Result = models.TextField(null=True, blank=True)
    HSC_Result = models.TextField(null=True, blank=True)
    Degree_Result = models.TextField(null=True, blank=True)
    Honours_Result = models.TextField(null=True, blank=True)
    PreMasters_Result = models.TextField(null=True, blank=True)
    Masters_Result = models.TextField(null=True, blank=True)
    SSC_Board = models.TextField(null=True, blank=True)
    HSC_Board = models.TextField(null=True, blank=True)
    Degree_U = models.TextField(null=True, blank=True)
    Honours_U = models.TextField(null=True, blank=True)
    PreMasters_U = models.TextField(null=True, blank=True)
    Masters_U = models.TextField(null=True, blank=True)
    Experience = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True)  # Stored in MEDIA folder

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
class ExStaff(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Index = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    SSC = models.TextField(null=True, blank=True)
    HSC = models.TextField(null=True, blank=True)
    Degree = models.TextField(null=True, blank=True)
    Honours = models.TextField(null=True, blank=True)
    PreMasters = models.TextField(null=True, blank=True)
    Masters = models.TextField(null=True, blank=True)
    SSC_Year = models.TextField(null=True, blank=True)
    HSC_Year = models.TextField(null=True, blank=True)
    Degree_Year = models.TextField(null=True, blank=True)
    Honours_Year = models.TextField(null=True, blank=True)
    PreMasters_Year = models.TextField(null=True, blank=True)
    Masters_Year = models.TextField(null=True, blank=True)
    SSC_Result = models.TextField(null=True, blank=True)
    HSC_Result = models.TextField(null=True, blank=True)
    Degree_Result = models.TextField(null=True, blank=True)
    Honours_Result = models.TextField(null=True, blank=True)
    PreMasters_Result = models.TextField(null=True, blank=True)
    Masters_Result = models.TextField(null=True, blank=True)
    SSC_Board = models.TextField(null=True, blank=True)
    HSC_Board = models.TextField(null=True, blank=True)
    Degree_U = models.TextField(null=True, blank=True)
    Honours_U = models.TextField(null=True, blank=True)
    PreMasters_U = models.TextField(null=True, blank=True)
    Masters_U = models.TextField(null=True, blank=True)
    Experience = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True)  # Stored in MEDIA folder

    def __str__(self):
        return f"{self.Name}   {self.Designation}   {self.Dept}"
    
        
class OtherPeople(models.Model):
    ID = models.IntegerField(primary_key=True)
    Img = models.ImageField(upload_to='images/personnel', blank=True, null=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True, null=True)
    Designation = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100)
    FName = models.CharField(max_length=100, null=True, blank=True)
    MName = models.CharField(max_length=100, null=True, blank=True)
    Joining = models.DateField(null=True, blank=True)
    Mobile = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    PreAddress = models.TextField(null=True, blank=True)
    PerAddress = models.TextField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    Order = models.IntegerField(null=True, blank=True)
    Retirement = models.DateField(null=True, blank=True)

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