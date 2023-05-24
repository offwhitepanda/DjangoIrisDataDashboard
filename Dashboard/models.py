from django.db import models


class Species(models.Model):
    species_id = models.IntegerField(primary_key=True)
    species = models.CharField(max_length=100)

    def __str__(self):
        return self.species

    class Meta:
        managed = False  # Specify that Django should not manage the table creation
        db_table = 'Species'  # Set the name of the pre-existing table

class Observation(models.Model):
    row_id = models.AutoField(primary_key=True, db_column='_rowid_')
    sepal_length = models.FloatField(max_length=5)
    sepal_width = models.FloatField(max_length=5)
    petal_length = models.FloatField(max_length=5)
    petal_width = models.FloatField(max_length=5)
    species_id = models.IntegerField
    species = models.ForeignKey(Species, on_delete=models.PROTECT, db_column='species_id')

    def get_attribute(self,attribute):
        
        return self.__getattribute__(attribute)


    class Meta:
        managed = False  # Specify that Django should not manage the table creation
        db_table = 'Observation'  # Set the name of the pre-existing table
