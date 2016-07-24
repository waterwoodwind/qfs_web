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
        verbose_name_plural = '区设置'

    def __unicode__(self):
        return self.name

class Location_zuo(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)
        verbose_name_plural = '座设置'

    def __unicode__(self):
        return self.name

class Location_ceng(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)
        verbose_name_plural = '层设置'

    def __unicode__(self):
        return self.name

class Location_hao(models.Model):
    name = models.CharField(max_length=50)

    def natural_key(self):
        return (self.name)

    class Meta:
        unique_together = (('name'),)
        verbose_name_plural = '号设置'

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
    Donation_certificate_1 = models.FileField(upload_to='Donation_1/',blank=True, verbose_name=u'捐建证书第一页')
    Donation_certificate_2 = models.FileField(upload_to='Donation_2/',blank=True, verbose_name=u'捐建证书第二页')
    receipt = models.FileField(upload_to='receipt/',blank=True, verbose_name=u'收据')
    Conversion_certificate = models.FileField(upload_to='receipt/',blank=True, verbose_name=u'皈依证')
    master_id_scan = models.FileField(upload_to='master_id_scan/',blank=True, verbose_name=u'本人身份证')
    relatives_id_scan = models.FileField(upload_to='relatives_id_scan/',blank=True, verbose_name=u'亲属身份证')

    class Meta:
        ordering = ["identity_card"]
        verbose_name_plural = u'百宝箱信息'

    def __unicode__(self):
        return self.identity_card

