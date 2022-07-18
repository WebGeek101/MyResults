from django.db import models

# Create your models here.
class markscard( models.Model ):
    sem=models.IntegerField(primary_key=True)
    subcode=models.CharField(max_length=100)
    sub=models.CharField(max_length=100)
    marks=models.IntegerField(10)
    class Meta:
        db_table="markscard"

    def __str__(self):
        return self.sem
   

