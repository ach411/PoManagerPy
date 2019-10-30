# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProdManager(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ProdManager'


class ShippingManager(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShippingManager'


class BillingManager(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BillingManager'


class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    account_payable_email = models.CharField(db_column='accountPayableEmail', max_length=255)  # Field name made lowercase.
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'Customer'


class Currency(models.Model):
    name = models.CharField(max_length=255)
    tla = models.CharField(max_length=3)
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Currency'


class Price(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    creation_date = models.DateField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Price'


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    price = models.ForeignKey(Price, on_delete=models.PROTECT)
    unit = models.ForeignKey('Unit', on_delete=models.PROTECT)
    pn = models.CharField(max_length=255, blank=True, null=True)
    cust_pn = models.CharField(db_column='custPn', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField()
    moq = models.IntegerField()
    active = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    prod_manager = models.ForeignKey(ProdManager, on_delete=models.PROTECT, db_column='prodManager_id')  # Field name made lowercase.
    shipping_manager = models.ForeignKey('ShippingManager', on_delete=models.PROTECT, db_column='shippingManager_id')  # Field name made lowercase.
    billing_manager = models.ForeignKey(BillingManager, on_delete=models.PROTECT, db_column='billingManager_id')  # Field name made lowercase.
    prod_name = models.CharField(db_column='prodName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    elifesheet = models.IntegerField()

    def __str__(self):
        return self.description

    @property
    def last_rev(self):
        active_rev = Revision.objects.filter(product = self).order_by('revision_cust').filter(active=1)
        if active_rev:
            return active_rev.reverse()[0].revision_cust
        else:
            return None

    class Meta:
        managed = False
        db_table = 'Product'


class AlertBpo(models.Model):
    product = models.OneToOneField('Product', models.PROTECT)
    threshold_qty = models.IntegerField(db_column='thresholdQty')  # Field name made lowercase.
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'AlertBpo'


class Bpo(models.Model):
    revision = models.ForeignKey('Revision', on_delete=models.PROTECT)
    price = models.ForeignKey('Price', on_delete=models.PROTECT)
    num = models.CharField(max_length=255)
    qty = models.IntegerField()
    start_date = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    file_path = models.CharField(db_column='filePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    buyer_email = models.CharField(db_column='buyerEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    paired_bpo = models.OneToOneField('self', models.SET_NULL, db_column='pairedBpo_id', null=True)  # Field name made lowercase.

    def __str__(self):
        return self.num

    class Meta:
        managed = False
        db_table = 'Bpo'


class Carrier(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Carrier'


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Category'


class Invoice(models.Model):
    num = models.CharField(max_length=255)
    file_path = models.CharField(db_column='filePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proforma_invoice_path = models.CharField(db_column='proformaInvoicePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoice_date = models.DateField(db_column='invoiceDate', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Invoice'


class Notification(models.Model):
    shipment = models.ForeignKey('Shipment', on_delete=models.CASCADE, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True)
    notification_source_class = models.CharField(db_column='notificationSourceClass', max_length=255)  # Field name made lowercase.
    notification_category = models.ForeignKey('Notificationcategory', on_delete=models.PROTECT, db_column='notificationCategory_id')  # Field name made lowercase.
    po_item = models.ForeignKey('PoItem', on_delete=models.CASCADE, db_column='poItem_id', blank=True, null=True)  # Field name made lowercase.
    bpo = models.ForeignKey(Bpo, on_delete=models.CASCADE, blank=True, null=True)
    rma = models.ForeignKey('Rma', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Notification'


class NotificationCategory(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    send_to = models.CharField(db_column='sendTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cc_to = models.CharField(db_column='ccTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bcc_to = models.CharField(db_column='bccTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attached_file = models.CharField(db_column='attachedFile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    list_message = models.TextField(db_column='listMessage', blank=True, null=True)  # Field name made lowercase.
    list_class = models.CharField(db_column='listClass', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotificationCategory'


class PartReplacement(models.Model):
    rma = models.ForeignKey('Rma', on_delete=models.PROTECT)
    product = models.ForeignKey('Product', on_delete=models.PROTECT, blank=True, null=True)
    old_part = models.CharField(db_column='oldPart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    new_part = models.CharField(db_column='newPart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PartReplacement'


class Po(models.Model):
    bpo = models.ForeignKey(Bpo, on_delete=models.PROTECT, blank=True, null=True)
    num = models.CharField(max_length=255)
    rel_num = models.CharField(db_column='relNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    file_path = models.CharField(db_column='filePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    buyer_email = models.CharField(db_column='buyerEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Po'


class PoItem(models.Model):
    revision = models.ForeignKey('Revision', on_delete=models.PROTECT)
    po = models.ForeignKey(Po, on_delete=models.CASCADE)
    price = models.ForeignKey('Price', on_delete=models.PROTECT)
    status = models.ForeignKey('Status', on_delete=models.PROTECT)
    line_num = models.IntegerField(db_column='lineNum', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    qty = models.IntegerField()
    shipped_qty = models.IntegerField(db_column='shippedQty')  # Field name made lowercase.
    approved = models.IntegerField()
    approved_date = models.DateTimeField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateField(db_column='dueDate')  # Field name made lowercase.
    promise_date = models.DateField(db_column='promiseDate', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    @property
    def extended_price(self):
        return self.price.price * self.qty

    class Meta:
        managed = False
        db_table = 'PoItem'


class ProblemCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(db_column='Description')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProblemCategory'


class RepairLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        managed = False
        db_table = 'RepairLocation'


class RepairStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'RepairStatus'


class Revision(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    active = models.IntegerField()
    revision = models.CharField(max_length=255, blank=True, null=True)
    revision_cust = models.CharField(db_column='revisionCust', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    drawing_path = models.CharField(db_column='drawingPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Revision'


class Rma(models.Model):
    shipment = models.ForeignKey('Shipment', on_delete=models.PROTECT, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, blank=True, null=True)
    num = models.CharField(max_length=255)
    cust_serial_num = models.CharField(db_column='custSerialNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    problem_description = models.TextField(db_column='problemDescription')  # Field name made lowercase.
    investigation_result = models.TextField(db_column='investigationResult', blank=True, null=True)  # Field name made lowercase.
    correction = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
    reception_date = models.DateTimeField(db_column='receptionDate', blank=True, null=True)  # Field name made lowercase.
    repair_date = models.DateTimeField(db_column='repairDate', blank=True, null=True)  # Field name made lowercase.
    shippedbackdate = models.DateTimeField(db_column='shippedBackDate', blank=True, null=True)  # Field name made lowercase.
    repair_findings = models.TextField(db_column='repairFindings', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    contact_email = models.CharField(db_column='contactEmail', max_length=255)  # Field name made lowercase.
    rpo_file_path = models.CharField(db_column='rpoFilePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rpo_num = models.CharField(db_column='rpoNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cust_file_path = models.CharField(db_column='custFilePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    serial_num = models.ForeignKey('SerialNumber', on_delete=models.PROTECT, db_column='serialNum_id')  # Field name made lowercase.
    problem_category = models.ForeignKey(ProblemCategory, on_delete=models.PROTECT, db_column='problemCategory_id', blank=True, null=True)  # Field name made lowercase.
    repair_status = models.ForeignKey(RepairStatus, on_delete=models.PROTECT, db_column='repairStatus_id')  # Field name made lowercase.
    repair_location = models.ForeignKey(RepairLocation, on_delete=models.PROTECT, db_column='repairLocation_id')  # Field name made lowercase.
    credited = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Rma'


class SerialNumber(models.Model):
    serial_number = models.CharField(db_column='SerialNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mac_address = models.CharField(db_column='macAddress', max_length=12, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    shipment_item = models.ForeignKey('ShipmentItem', on_delete=models.PROTECT, db_column='shipmentItem_id', blank=True, null=True)  # Field name made lowercase.
    certificate_file_name = models.CharField(db_column='certificateFileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    file_path = models.CharField(db_column='filePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipment_batch = models.ForeignKey('Shipmentbatch', on_delete=models.PROTECT, db_column='shipmentBatch_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SerialNumber'


class Shipment(models.Model):
    carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT, blank=True, null=True)
    shipping_date = models.DateField(db_column='shippingDate', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    tracking_num = models.CharField(db_column='trackingNum', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shipment'


class ShipmentBatch(models.Model):
    num = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(db_column='productName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    waiting_for_removal = models.IntegerField(db_column='waitingForRemoval')  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    modified_date = models.DateTimeField(db_column='modifiedDate', blank=True, null=True)  # Field name made lowercase.
    file_path = models.CharField(db_column='filePath', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipment_item = models.ForeignKey('ShipmentItem', on_delete=models.PROTECT, db_column='shipmentItem_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShipmentBatch'


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, blank=True, null=True)
    created_date = models.DateTimeField(db_column='createdDate', blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField()
    po_item = models.ForeignKey(PoItem, on_delete=models.PROTECT, db_column='poItem_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShipmentItem'


class Status(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Status'


class Unit(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Unit'


class UploadElifesheetPending(models.Model):
    shipment_item = models.OneToOneField(ShipmentItem, models.PROTECT, db_column='shipmentItem_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UploadElifesheetPending'


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'product_category'
        unique_together = (('product', 'category'),)


class SpareParts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, primary_key=True, related_name='parent_product')
    spare_parts = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='child_product')

    class Meta:
        managed = False
        db_table = 'spare_parts'
        unique_together = (('product', 'spare_parts'),)
