import urllib2

def urllib(url, data, fail_silently):
    request = urllib2.Request(url)

    try:
        urllib2.urlopen(request)
    except Exception:
        if not fail_silently:
            raise
