import re


def path(rule, view_f, login_required=False, admin_required=False):
    rule = re.sub(r"<(?P<name>\w+):int>", "(?P<\g<name>>\d+)", rule)
    rule = re.sub(r"<(?P<name>\w+):str>", "(?P<\g<name>>\w+)", rule)
    rule += '/?$'
    return rule, view_f, login_required, admin_required
