#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location_qu(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class Location_zuo(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class Location_ceng(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class Location_hao(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)

    def __unicode__(self):
        return self.name

class bbx_info(models.Model):
    master = models.CharField(max_length=20, verbose_name=u'捐建信士')
    identity_card = models.CharField(max_length=20, verbose_name=u'身份证')
    address = models.TextField(u'地址')
    contact_way = models.CharField(max_length=20, verbose_name=u'联系方式')
    location_qu = models.ForeignKey(Location_qu, verbose_name=u'区')
    location_zuo = models.ForeignKey(Location_zuo, verbose_name=u'座')
    location_ceng = models.ForeignKey(Location_ceng, verbose_name=u'层')
    location_hao = models.ForeignKey(Location_hao, verbose_name=u'号')
    relatives = models.CharField(max_length=20, verbose_name=u'亲属名')
    Relationship = models.CharField(max_length=20, verbose_name = u'亲属关系')
