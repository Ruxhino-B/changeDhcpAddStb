from django.db import models


class Attributes(models.Model):
    description = models.CharField(max_length=64, blank=True, null=True)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attributes'


# class DelAttr(models.Model):
#     id = models.PositiveIntegerField()
#     username = models.CharField(max_length=64)
#     attribute = models.CharField(max_length=64)
#     op = models.CharField(max_length=2)
#     value = models.CharField(max_length=512, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'del_attr'


class IpList(models.Model):
    ipaddress = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_list'


class IpPools(models.Model):
    city_id = models.IntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=64, blank=True, null=True)
    stb_mac = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_pools'


class ManyStb(models.Model):
    mac = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'many_stb'


class MsanRegionMap(models.Model):
    nename = models.CharField(db_column='NeName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    neip = models.CharField(db_column='NeIP', max_length=128, blank=True, null=True)  # Field name made lowercase.
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msan_region_map'


class PhoneNr(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mac_add = models.CharField(db_column='Mac_add', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone_nr'
        unique_together = (('id', 'mac_add'),)


class Pools(models.Model):
    city_id = models.IntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=64, blank=True, null=True)
    stb_mac = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pools'


class Radacct(models.Model):
    radacctid = models.BigAutoField(primary_key=True)
    acctsessionid = models.CharField(max_length=64)
    acctuniqueid = models.CharField(unique=True, max_length=32)
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    realm = models.CharField(max_length=64, blank=True, null=True)
    nasipaddress = models.CharField(max_length=15)
    nasportid = models.CharField(max_length=15, blank=True, null=True)
    nasporttype = models.CharField(max_length=32, blank=True, null=True)
    acctstarttime = models.DateTimeField(blank=True, null=True)
    acctstoptime = models.DateTimeField(blank=True, null=True)
    acctsessiontime = models.PositiveIntegerField(blank=True, null=True)
    acctauthentic = models.CharField(max_length=32, blank=True, null=True)
    connectinfo_start = models.CharField(max_length=50, blank=True, null=True)
    connectinfo_stop = models.CharField(max_length=50, blank=True, null=True)
    acctinputoctets = models.BigIntegerField(blank=True, null=True)
    acctoutputoctets = models.BigIntegerField(blank=True, null=True)
    calledstationid = models.CharField(max_length=50)
    callingstationid = models.CharField(max_length=50)
    acctterminatecause = models.CharField(max_length=32)
    servicetype = models.CharField(max_length=32, blank=True, null=True)
    framedprotocol = models.CharField(max_length=32, blank=True, null=True)
    framedipaddress = models.CharField(max_length=15)
    acctstartdelay = models.PositiveIntegerField(blank=True, null=True)
    acctstopdelay = models.PositiveIntegerField(blank=True, null=True)
    xascendsessionsvrkey = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'radacct'


class Radcheck(models.Model):
    username = models.CharField(unique=True, max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radcheck'
        unique_together = (('id', 'username'),)


class Radgroupcheck(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radgroupcheck'


class Radgroupreply(models.Model):
    groupname = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=253)

    class Meta:
        managed = False
        db_table = 'radgroupreply'


class Radpostauth(models.Model):
    username = models.CharField(max_length=64)
    pass_field = models.CharField(db_column='pass', max_length=64)  # Field renamed because it was a Python reserved word.
    reply = models.CharField(max_length=32)
    authdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'radpostauth'


class Radreply(models.Model):
    username = models.CharField(max_length=64)
    attribute = models.CharField(max_length=64)
    op = models.CharField(max_length=2)
    value = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'radreply'
        unique_together = (('id', 'username'),)

#
# class Radreply1111(models.Model):
#     id = models.PositiveIntegerField()
#     username = models.CharField(max_length=64)
#     attribute = models.CharField(max_length=64)
#     op = models.CharField(max_length=2)
#     value = models.CharField(max_length=512)
#
#     class Meta:
#         managed = False
#         db_table = 'radreply_11_11'


# class Radrpl(models.Model):
#     id = models.PositiveIntegerField()
#     username = models.CharField(max_length=64)
#     attribute = models.CharField(max_length=64)
#     op = models.CharField(max_length=2)
#     value = models.CharField(max_length=512)
#
#     class Meta:
#         managed = False
#         db_table = 'radrpl'


class Radusergroup(models.Model):
    username = models.CharField(max_length=64)
    groupname = models.CharField(max_length=64)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radusergroup'


# class Recover(models.Model):
#     id = models.IntegerField()
#     city_id = models.IntegerField(blank=True, null=True)
#     ipaddress = models.CharField(max_length=64, blank=True, null=True)
#     stb_mac = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'recover'


class Regions(models.Model):
    city = models.CharField(max_length=64, blank=True, null=True)
    subnet = models.CharField(max_length=64, blank=True, null=True)
    gateway = models.CharField(max_length=64, blank=True, null=True)
    network = models.CharField(max_length=64, blank=True, null=True)
    dns = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class StbMacHistory(models.Model):
    city_id = models.IntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=64, blank=True, null=True)
    stb_mac = models.CharField(max_length=64, blank=True, null=True)
    date_deleted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stb_mac_history'


class TmpUser(models.Model):
    username = models.CharField(primary_key=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'tmp_user'


class Userlog(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    username = models.CharField(max_length=32)
    userip = models.CharField(db_column='userIp', max_length=45)  # Field name made lowercase.
    action = models.CharField(max_length=255, blank=True, null=True)
    logtime = models.DateTimeField(db_column='logTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userlog'
