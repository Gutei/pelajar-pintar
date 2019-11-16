import uuid
from django.db import models
from django.utils import timezone

from django.conf import settings

# Create your models here.
class School(models.Model):

    TK = 0
    PAUD = 1
    SD = 2
    MI = 3
    SMP = 4
    MTS = 5
    SMA = 6
    SMK = 7
    MA = 8

    LEVEL = (
        (TK, 'TK'),
        (PAUD, 'PAUD'),
        (SD, 'SD'),
        (MI, 'MI'),
        (SMP, 'SMP'),
        (MTS, 'MTs'),
        (SMA, 'SMA'),
        (SMK, 'SMK'),
        (MA, 'MA'),
    )

    NEGERI = 0
    SWASTA = 1

    TYPE = (
        (NEGERI, 'Negeri'),
        (SWASTA, 'Swasta'),
    )

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school_number = models.CharField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    level = models.CharField(choices=LEVEL, max_length=8, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='school/logo', null=True, blank=True)
    image = models.ImageField(upload_to='school/image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = self.name
        return "{}".format(name)

    class Meta:
        db_table = 'schools'


class AbstractSchool(models.Model):
    # add additional fields in here
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.hex

    class Meta:
        db_table = 'abstract_schools'


class SchoolContact(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_contacts'


class SchoolMajor(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=True, blank=True)
    image = models.ImageField(upload_to='major/image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_majors'

class SchoolExtracurricular(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='ekskul/image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_extracurriculars'


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='teacher/photo', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'techers'


class TeacherContact(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey('Teacher', null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'techer_contacts'


class SchoolAchievement(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='achievement/image', null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_achievements'

class SchoolActivity(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='activity/image', null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school_activities'


class StudentRegistration(models.Model):

    MALE    = 0
    FEMALE  = 1

    GENDERS = (
        (MALE, 'Laki-laki'),
        (FEMALE, 'Perempuan'),
    )

    ISLAM   = 0
    KRISTEN = 1
    KATOLIK = 2
    BUDHA   = 3
    HINDU   = 4
    OTHERS  = 5

    FAITHS = (
        (ISLAM, 'Islam'),
        (KRISTEN, 'Kristen'),
        (KATOLIK, 'Katholik'),
        (BUDHA, 'Budha'),
        (HINDU, 'Hindu'),
        (OTHERS, 'Lain-lain'),
    )

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    MONTHS = (
        (JANUARY, 'January'),
        (FEBRUARY, 'February'),
        (MARCH, 'March'),
        (APRIL, 'April'),
        (MAY, 'May'),
        (JUNE, 'June'),
        (JULY, 'July'),
        (AUGUST, 'August'),
        (SEPTEMBER, 'September'),
        (OCTOBER, 'October'),
        (NOVEMBER, 'November'),
        (DECEMBER, 'December')
    )

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    from_school = models.CharField(max_length=128, null=True, blank=True)
    to_school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    registration_number = models.PositiveIntegerField(null=True, blank=True)
    periode = models.CharField(max_length=128, null=True, blank=True)
    registration_year = models.CharField(max_length=4, null=True, blank=True)
    registration_month = models.CharField(choices=MONTHS, max_length=32, null=True, blank=True)
    student_name = models.CharField(max_length=128, null=True, blank=True)
    nisn = models.CharField(max_length=128, null=True, blank=True)
    national_exam_number = models.CharField(max_length=128, null=True, blank=True)
    graduation_year = models.CharField(max_length=4, null=True, blank=True)
    skhun_number = models.CharField(max_length=128, null=True, blank=True)
    average_national_exam_scores = models.DecimalField(max_digits=11, decimal_places=2, default=0,)
    parent_name = models.CharField(max_length=128, null=True, blank=True)
    mother_name = models.CharField(max_length=128, null=True, blank=True)
    number_of_siblings = models.PositiveIntegerField(default=0)
    gender = models.PositiveSmallIntegerField(choices=GENDERS, default=MALE)
    birth_date = models.DateTimeField(null=True, blank=True)
    birth_place = models.CharField(max_length=128, null=True, blank=True)
    faith = models.PositiveSmallIntegerField(choices=FAITHS, default=ISLAM)
    student_phone = models.CharField(max_length=20, null=True, blank=True)
    parent_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image_student = models.ImageField(upload_to='registration/student', null=True, blank=True)
    image_skhun = models.ImageField(upload_to='registration/skhun', null=True, blank=True)

    class Meta:
        db_table = 'student_registrations'



class SchoolToken(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    token = models.TextField(null=True, blank=True)
    expired_date = models.DateTimeField(null=True, blank=True)
    is_expired = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'school_tokens'

class StudentRegistrationToken(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    token = models.TextField(null=True, blank=True)
    expired_date = models.DateTimeField(null=True, blank=True)
    is_expired = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_registration_tokens'


class SchoolMagazine(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = 'school_magazines'


class SchoolMagazineActivity(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    magazine = models.ForeignKey('SchoolMagazine', null=True, blank=True, on_delete=models.CASCADE)
    activity = models.ForeignKey('SchoolActivity', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'school_magazine_activities'


class Province(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        name = self.name
        return "{}".format(name)

    class Meta:
        db_table = 'provinces'


class City(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    province = models.ForeignKey('Province', null=True, blank=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        name = self.name
        return "{}".format(name)

    class Meta:
        db_table = 'cities'