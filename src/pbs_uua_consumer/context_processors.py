from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

""" We make available to templates a set of values useful for
quick integration.
"""


def openid_config(request):
    popup_mode = getattr(settings, 'OPENID_USE_POPUP_MODE', False)
    sso_url = mark_safe(u"%s?next=%s" % (reverse('login_begin'), request.get_full_path()),)
    sso_admin_url = mark_safe(u"%s?next=%s" % (reverse('login_begin_admin'), request.get_full_path()),)
    sso_js_url = getattr(settings, 'OPENID_SSO_SERVER_JS_URL', '')

    if popup_mode:
        base_href = u'%s?next=%s" onClick="javascript:loadPopup();return false;'
        href =  base_href % (reverse('login_begin_popup', kwargs={'popup_mode': 0}), request.get_full_path())
        admin_href = base_href % (reverse('login_begin_admin_popup', kwargs={'popup_mode': 0}), request.get_full_path())
    else:
        base_href = u'%s?next=%s'
        href = base_href % (reverse('login_begin'), request.get_full_path())
        admin_href = base_href % (reverse('login_begin_admin'), request.get_full_path())

    openid_login_link = mark_safe(u'<a id="uua_login" href="%s">Login with your PBS account</a>' % href)
    openid_admin_login_link = mark_safe(u'<a id="uua_login" href="%s">Login with your PBS account</a>' % admin_href)

    return {'popup_mode': popup_mode,  # True or False, as it's set in OPENID_USE_POPUP_MODE
            'sso_url': sso_url,  # request based, contains the url for a correct OpenId request initiation
            'sso_admin_url': sso_admin_url,
            'sso_js_url': sso_js_url,  # path to the location of js files provided by login.pbs.org
            'openid_login_link': openid_login_link,  # generated anchor linked to the OpenId begin method
            'openid_admin_login_link': openid_admin_login_link} # generated anchor linked to the OpenId begin method for admin logins
