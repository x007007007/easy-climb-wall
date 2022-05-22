from django.db import models


class HttpMethod(models.Model):
    GET = 'GET'
    OPTIONAL = 'OPTIONAL'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    HEAD = 'HEAD'

    name = models.CharField(
        choices=(
            (GET, GET),
            (POST, POST),
            (HEAD, HEAD),
            (PATCH, PATCH),
            (DELETE, DELETE),
            (PUT, PUT),
            (OPTIONAL, OPTIONAL),
        ),
        max_length=16
    )