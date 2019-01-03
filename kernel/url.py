import re


def path(rule, view_f, login_required=False):
    rule = re.sub("<(?P<name>\w+):int>", "(?P<\g<name>>\d+)", rule)
    rule = re.sub("<(?P<name>\w+):str>", "(?P<\g<name>>\w+)", rule)
    rule += '/?$'
    return rule, view_f, login_required
