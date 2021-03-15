from django.conf import settings 
from django.db import models 
from django.utils import timezone 


class Profili(models.Model):
     nome = models.CharField(max_length=200, primary_key=True)
     testo = models.TextField()
     parole = models.IntegerField()
     vocabolario = models.IntegerField()
     n_hashtag = models.IntegerField()
     v_hashtag = models.IntegerField()
     n_tag = models.IntegerField()
     v_tag = models.IntegerField()
     post_medi = models.IntegerField()
     parole_medie = models.IntegerField()
     caratteri_medi = models.IntegerField()
     hashtag_medi = models.IntegerField()
     tag_medi = models.FloatField()
     casual = models.IntegerField()
     professional = models.IntegerField()
     designed = models.IntegerField()
     grafica = models.IntegerField()
     gruppo = models.IntegerField()
     singolo = models.IntegerField()
     scena = models.IntegerField()  

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.nome

class Teatri(models.Model):
     codifica = models.ForeignKey(Profili, on_delete=models.CASCADE)
     nome_teatro = models.CharField(max_length=200)
     cat_foto = models.CharField(max_length=200)
     soggetto = models.CharField(max_length=200)
     likes = models.IntegerField()

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.nome_teatro

class Frequenze(models.Model):
     Id_freq = models.ForeignKey(Profili, on_delete=models.CASCADE)
     nome_f = models.CharField(max_length=200)
     tipo = models.CharField(max_length=200)
     freq = models.IntegerField()

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.nome_f


class Tag(models.Model):
     Id_tag = models.ForeignKey(Profili, on_delete=models.CASCADE)
     nome_tag = models.CharField(max_length=200)
     freq_t = models.IntegerField()

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.nome_tag

class Hashtag(models.Model):
     Id_hashtag = models.ForeignKey(Profili, on_delete=models.CASCADE)
     nome_hashtag = models.CharField(max_length=200)
     freq_h = models.IntegerField()

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.nome_hashtag