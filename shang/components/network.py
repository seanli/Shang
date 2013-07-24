from django.utils import simplejson
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')
    return client_ip


# Status Codes: http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
def build_response(response, mimetype='application/json', status=200):
    return HttpResponse(simplejson.dumps(response, cls=DjangoJSONEncoder), mimetype=mimetype, status=status)
