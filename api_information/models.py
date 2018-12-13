from django.db import models

# Create your models here.
class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    schema_name = models.CharField(max_length=200)
    table_name = models.CharField(max_length=200)
    column_name = models.CharField(max_length=200)
    data_type = models.CharField(max_length=30)
    data_type_length = models.IntegerField()
    data_type_precision = models.IntegerField()

class Schemas(models.Model):
    id = models.AutoField(primary_key=True)
    schema_name = models.CharField(max_length=200)
    schema_description = models.CharField(max_length=1000)

class Tables(models.Model):
    id = models.AutoField(primary_key=True)
    schema_name = models.CharField(max_length=200)
    table_name = models.CharField(max_length=200)
    table_description = models.CharField(max_length=1000)

class Columns(models.Model):
    id = models.AutoField(primary_key=True)
    schema_name = models.CharField(max_length=200)
    table_name = models.CharField(max_length=200)
    column_name = models.CharField(max_length=200)
    column_description = models.CharField(max_length=1000)