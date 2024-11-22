from django.db import models

class IpInfo(models.Model):
    asn = models.CharField(max_length=50)
    org = models.CharField(max_length=100)
    blacklist = models.BooleanField()
    ip = models.CharField(max_length=45)
    country = models.TextField()


    class Meta:
        db_table = 'ip_info'  # Optional: specify exact table name if needed


class TcpConnection(models.Model):
    source = models.TextField()
    timestamp = models.TextField()
    sport = models.IntegerField()

    class Meta:
        db_table = 'tcp_connection'  # Optional: specify exact table name if needed


class HttpRequeste(models.Model):
    timestamp = models.TextField()
    ip = models.CharField(max_length=45)
    original_url = models.TextField()
    user_agent = models.TextField()
    headers = models.JSONField()      # Requires Django 3.1+ and a supported database backend
    fw_res = models.TextField()
    body = models.TextField()
    method = models.CharField(max_length=10)
    query = models.JSONField()
    cookies = models.TextField()

    class Meta:
        db_table = 'http_request'  # Optional: specify exact table name if needed
