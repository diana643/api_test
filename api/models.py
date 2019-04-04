from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.CharField(u'Nom', max_length=100, default='no_nom')
    email = models.CharField(u'Email', max_length=100, default='no_email')
    psw = models.CharField(u'PSW', max_length=50, default="no_psw")

    def __unicode__(self):
        return '%d: %s'%(self.pk, self.nom)
