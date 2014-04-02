import pprint
import urllib2

def urllib(url, data, fail_silently):
    request = urllib2.Request(url)

    try:
        urllib2.urlopen(request)
    except Exception:
        if not fail_silently:
            raise

def console(url, data, fail_silently):
    print "-" * 80
    print "django-hipchat:"
    pprint.pprint(data, indent=4)

def disabled(url, data, fail_silently):
    pass
