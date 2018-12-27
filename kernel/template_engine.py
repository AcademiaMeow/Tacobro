import re

class Template():
    def __init__(self, file):
        self.file = file

    def render(self, request, params):
        template_html = open("templates/" + self.file).read()

        def _gen_condition(matched):
            condition = matched.group(1).strip()
            if_statement = matched.group(2).strip()
            else_statement = matched.group(3).strip()

            if condition in params:
                if type(params[condition]) != bool:
                    raise ValueError(condition + " should be bool.")
                return if_statement if params[condition] else else_statement
            else:
                return ""

        template_html = re.sub("{%[\s]*if[\s]*(\S+)[\s]*%}([\s\S\n]*){%[\s]*else[\s]*%}([\s\S\n]*){% endif %}", _gen_condition, template_html)

        def _get_value(matched):
            key = matched.group(1)
            return str(params[matched.group(1)]) if key in params else ""

        template_html = re.sub(
            "{{[ \t\n\r]*(\S+)[\s]*}}",
            _get_value, template_html)

        return template_html
