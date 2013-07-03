from django.db import models
from django.contrib.auth.models import User
from athumb.fields import ImageWithThumbsField


class Session(models.Model):

    LEVELS = [
        ('Introductory', 'Introductory'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    name = models.CharField(u'Name', max_length=50)
    creator = models.ForeignKey(User, verbose_name=u'Creator')
    duration = models.CharField(u'Duration', max_length=50)
    level = models.CharField(u'Level', choices=LEVELS, max_length=50)
    abstract = models.TextField(u'Abstract', max_length=2000)
    vote_count = models.IntegerField('Vote count')

    def __unicode__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(u'Address', max_length=254)
    city = models.CharField(u'Address', max_length=50)
    province = models.CharField(u'Province', max_length=2)

    def __unicode__(self):
        return self.address


class Event(models.Model):
    name = models.CharField(u'Name', max_length=50)
    date = models.DateField(u'Date')
    time = models.TimeField(u'Time')
    location = models.ForeignKey(Location, verbose_name=u'Location')
    image = ImageWithThumbsField(
        'Image',
        upload_to="events/%Y/%m/%d/",
        thumbs=(
            ('thumb', {'size': (80, 80), 'crop': True}),
            ('large', {'size': (980, 400), 'crop': 'smart'}),
        ),
        blank=True, null=True,
        # storage=PUBLIC_MEDIA_BUCKET)
    )
    sessions = models.ManyToManyField(Session)

    def get_image_url(self):
        if not self.image:
            return ''
        return self.image.generate_url(thumb_name='large')

    def get_thumb_url(self):
        if not self.image:
            return ''
        return self.image.generate_url(thumb_name='thumb')

    def __unicode__(self):
        return self.name
