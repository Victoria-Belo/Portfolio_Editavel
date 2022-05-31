# --*************************************************************
# --FEITO POR VICKSTUFF, 2021 - https://github.com/Victoria-Belo
# --*************************************************************
from django.db import models
import uuid


class Base(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Feature(models.Model):
    icons_choice = {
        ('lni-layout', 'quadro'),
        ('lni-tab', 'responsivo'),
        ('lni-rocket', 'foguete'),
        ('lni-database', 'dados'),
        ('lni-leaf', 'folha'),
        ('lni-pencil', 'caneta'),
    }
    title = models.CharField(max_length=60, unique=True, blank=False)
    about = models.TextField(max_length=150)
    icon_select = models.CharField(max_length=20, choices=icons_choice)

    def __str__(self):
        return self.title

class About(models.Model):
    icons_choice = {
        ('lni-pencil', 'caneta'),
        ('lni-cog', 'web_dev'),
        ('lni-stats-up', 'grafico'),
        ('lni-layers', 'ui_ux_design'),
        ('lni-tab', 'app_dev'),
        ('lni-briefcase', 'marketing'),
    }

    title = models.CharField(max_length=40, unique=True, blank=False)
    about = models.TextField(max_length=150)
    icon_select = models.CharField(max_length=20, choices=icons_choice)

    def __str__(self):
        return self.title

class Team(Base):
    name = models.CharField(max_length=50, blank=False)
    office = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='img/')
    facebook = models.CharField(max_length=100, default='')
    linkedIn = models.CharField(max_length=100, default='')
    tumbrl = models.CharField(max_length=100, default='')
    twiiter = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'office', 'photo']

class Note(Base):
    title = models.CharField(max_length=100, blank=False)
    sub_title = models.CharField(max_length=80)
    note = models.TextField(max_length=500)
    notice = models.CharField(max_length=100, blank=True)

    # criar fk para usuario e criar model para usuario se cadastrar

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'sub_title', 'note', 'notice', 'create_at', 'update_at']
