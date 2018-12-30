import re


def path(rule, view_f):
    rule = re.sub("<(?P<name>\w+):int>", "(?P<\g<name>>\d+)", rule)
    rule = re.sub("<(?P<name>\w+):int>", "(?P<\g<name>>\d+)", rule)
    rule += '/?$'
    return rule, view_f
