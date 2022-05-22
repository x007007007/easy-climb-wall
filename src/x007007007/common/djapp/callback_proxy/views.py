from loguru import logger
import re
from django.shortcuts import get_object_or_404
from .models import ConfigModel, HistoryModel
from rest_framework import response
from rest_framework import serializers
from rest_framework import generics
import json
import celery
from django.utils import timezone
# Create your views here.


class CallbackAPIView(
    generics.CreateAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.ListAPIView,
    generics.GenericAPIView,
):
    _object = None

    http_header_re = re.compile('^HTTP_')

    def get_object(self):
        if self._object is None:
            obj = get_object_or_404(
                ConfigModel,
                postfix_url=self.kwargs['postfix']
            )
            self._object = obj
        return self._object

    def get_serializer_class(self):
        obj = self.get_object()
        serializer_kwargs = {}
        for item in obj.configapischemaitem_set.values():
            serializer_field_cls = getattr(serializers, item['type'])
            if item['extra']:
                field = serializer_field_cls(**item['extra'])
            else:
                field = serializer_field_cls()
            serializer_kwargs[item['name']] = field
        return type('Serializer', (serializers.Serializer,), serializer_kwargs)

    def _allowed_methods(self):
        if res := [
            x.upper() for x in self.get_object().allow_method_set.values_list('name', flat=True)
        ]:
            return res
        else:
            return super(CallbackAPIView, self).allowed_methods

    def dispatch(self, request, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?
        try:
            self.initial(request, *args, **kwargs)

            if request.method.upper() in self.http_method_names:
                response = self.callbymethod(
                    self.get_object(),
                    request,
                    *args,
                    **kwargs
                )
            else:
                response = self.http_method_not_allowed(request, *args, **kwargs)
        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response

    def callbymethod(self, config: ConfigModel, request, *args, **kwargs):
        if config.action:
            self.run_action(config, request)
        return response.Response(
        )

    def run_action(self, config: ConfigModel, request):
        try:
            data = json.dumps(request.data)
        except:
            data = request.data
        record = HistoryModel.objects.create(
            config=config,
            request=data,
            header=dict(request.headers),
            params=request.META['QUERY_STRING']
        )
        return record.run_action()