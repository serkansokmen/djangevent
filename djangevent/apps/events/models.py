from django.db import models


class Session(models.Model):
    name = models.CharField('Name', max_length=50)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    address = models.CharField('Address', max_length=254)
    city = models.CharField('Address', max_length=50)
    province = models.CharField('Province', max_length=2)

    def __unicode__(self):
        return self.address


class Event(models.Model):
    name = models.CharField('Name', max_length=50)
    date = models.DateField('Date')
    time = models.TimeField('Time')
    location = models.ForeignKey(Location, verbose_name='Location')
    image = models.ImageField('Image', upload_to="events/%Y/%m/%d/")
    sessions = models.ManyToManyField(Session)

    def get_image_url(self):
        return self.image.url

    def __unicode__(self):
        return self.name
