from django.db import models

RATING_CHOICE = zip(range(11), range(11))

class Address(models.Model):
    street = models.CharField(max_length=250, blank=True, default='')
    city = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='India')
    pincode = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s , %s, %s' % (self.street, self.city, self.state)

class College(models.Model):
    COLLEGE_TYPE = (
        ('Arts/Commerce/Science', 'Arts/Commerce/Science'),
        ('Engineering', 'Engineering'),
        ('Management', 'Management'),
        ('Law', 'Law'),
        ('Medical', 'Medical/Dental'),
        ('Others', 'Others')
        )
    YEAR_CHOICES = zip(range(1900, 2012), range(1900, 2012))

    name=models.CharField(max_length=200)
    college_type=models.CharField(max_length = 40, choices = COLLEGE_TYPE)
    address = models.ForeignKey(Address)
    about = models.TextField(default='Not Available')
    estd = models.PositiveIntegerField(choices=YEAR_CHOICES)
    website = models.URLField(blank=True, null=True)
    rating = models.PositiveIntegerField(choices = RATING_CHOICE)
    thumbnail = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPE = (
        ('Academics', 'Academics'),
        ('Seminar/Workshop', 'Seminar/Workshop'),
        ('Party', 'Party'),
        ('Festival', 'Festival'),
        ('Conference/Meetup', 'Conference/Meetup'),
        ('Competition', 'Competition'),
        ('Misc', 'Misc')
            )
    INVITATION_TYPE=(
        ('Open', 'Open to Anyone'),
        ('Restricted', 'Passes/Special Invitation Required'),
        ('In-Campus', 'In-Campus'),
            )

    name = models.CharField(max_length=250)
    event_type=models.CharField(max_length=40, choices=EVENT_TYPE)
    host=models.ForeignKey(College)
    venue = models.ForeignKey(Address)
    about=models.TextField(blank=True, default='Not Available')
    start_date=models.DateField()
    end_date=models.DateField()
    participate=models.CharField(max_length=20, choices=INVITATION_TYPE)
    website=models.URLField(blank=True, null=True)
    fb_page=models.URLField(blank=True, null=True)
    popularity=models.PositiveIntegerField(choices = RATING_CHOICE)
    gallery_link=models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'%s at %s' % (self.name, self.host.name)

class Club(models.Model):
    CLUB_TYPE=(
        ('Engg and Tech', 'Engg and Tech'),
        ('Applied Sciences', 'Applied Sciences'),
        ('Social/NGO', 'Social/NGO'),
        ('Drama/Arts/Literature', 'Drama/Arts/Literature'),
        ('Music', 'Music/Bands'),
        ('Management', 'Management/Finance'),
        ('Others', 'Others'),
            )
    MEMBERSHIP_CHOICE = (
        ('OpenAll', 'Open to anyone'),
        ('OpenSome', 'Some Criteria'),
        ('Selection', 'Through Apply and Selection'),
        ('Closed', 'Closed'),
            )

    name=models.CharField(max_length=250)
    club_type=models.CharField(max_length=40, choices=CLUB_TYPE)
    about=models.TextField(blank=True, default='Not Available')
    estd=models.DateField()
    college=models.ForeignKey(College)
    website=models.URLField(blank=True, null=True)
    membership=models.CharField(max_length=20, choices=MEMBERSHIP_CHOICE)
    popularity=models.PositiveIntegerField(choices= RATING_CHOICE)
    thumbnail = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["-popularity"]

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.college.name)

class Note(models.Model):
    NOTE_TYPE=(
        ('PDF', 'PDF'),
        ('Word', 'Word Document'),
        ('Presentation File', 'Presentation File'),
        ('Images', 'Images'),
        ('Video/Audio', 'Video/Audio'),
        ('Other', 'Other'),
            )
    COURSE_CHOICES = (
            ('Computer Science','Computer Science'),
            ('Electronics and Communication', 'Electronics and Communication'),
            ('Mechanical and Automation', 'Mechanical and Automation'),
            ('Civil', 'Civil'),
            ('Biotech', 'Biotech'),
            )
    name = models.CharField(max_length=200)
    related_course=models.CharField(max_length=100, choices=COURSE_CHOICES)
    note_type=models.CharField(max_length=40, choices=NOTE_TYPE)
    submitted_by=models.CharField(max_length=100, blank=True, null=True)
    date_updated=models.DateField(auto_now=True)
    link=models.URLField()
    thumbnail = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.related_course)


