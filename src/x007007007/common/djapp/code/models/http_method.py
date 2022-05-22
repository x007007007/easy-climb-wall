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

    def __str__(self):
        return f"<{self.__class__.__name__} ({self.id}) {self.name}>"
