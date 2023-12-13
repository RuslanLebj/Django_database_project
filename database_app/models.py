# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=15, blank=True, null=True)
    client_surname = models.CharField(max_length=15, blank=True, null=True)
    client_patronymic = models.CharField(max_length=15, blank=True, null=True)
    client_birth = models.DateField(blank=True, null=True)
    client_phone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class CommercialOrganization(models.Model):
    id_commercial_organization = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=50, blank=True, null=True)
    link = models.CharField(max_length=30, blank=True, null=True)
    tin = models.CharField(max_length=12, blank=True, null=True)
    fk_id_establishment_form = models.ForeignKey('EstablishmentForm', models.DO_NOTHING,
                                                 db_column='fk_id_establishment_form', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commercial_organization'


class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=53, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class EstablishmentForm(models.Model):
    id_establishment_form = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establishment_form'


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    order_address = models.CharField(max_length=30, blank=True, null=True)
    order_status = models.BooleanField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    fk_id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='fk_id_client', blank=True, null=True)
    fk_id_sales_point = models.ForeignKey('SalesPoint', models.DO_NOTHING, db_column='fk_id_sales_point', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_'


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_type = models.CharField(max_length=30, blank=True, null=True)
    product_size = models.CharField(max_length=10, blank=True, null=True)
    fk_id_commercial_organization = models.ForeignKey(CommercialOrganization, models.DO_NOTHING, db_column='fk_id_commercial_organization', blank=True, null=True)
    fk_id_brand = models.ForeignKey(Brand, models.DO_NOTHING, db_column='fk_id_brand', blank=True, null=True)
    fk_id_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='fk_id_country', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Receipt(models.Model):
    id_receipt = models.AutoField(primary_key=True)
    receipt_product_amount = models.SmallIntegerField(blank=True, null=True)
    receipt_product_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fk_id_order = models.ForeignKey(Order, models.DO_NOTHING, db_column='fk_id_order', blank=True, null=True)
    fk_id_product = models.ForeignKey(Product, models.DO_NOTHING, db_column='fk_id_product', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receipt'


class SalesPoint(models.Model):
    id_sales_point = models.AutoField(primary_key=True)
    sales_point_address = models.CharField(max_length=30, blank=True, null=True)
    sales_point_name = models.CharField(max_length=20, blank=True, null=True)
    fk_id_commercial_organization = models.ForeignKey(CommercialOrganization, models.DO_NOTHING, db_column='fk_id_commercial_organization', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_point'
