```shell=
$ python run.py
```

## Template

### View
```python
return Template("index.html").render(request, {
                "name": "Test",
                "age": 20,
                "ouo?": True,
                "secret": "S3CR3T"
            })
```

### HTML file
```html
<!-- 普通的傳變數進去 -->
Name: {{ name }}<br>
Age: {{ age }}<br>

<!-- 傳不存在的變數進去會 replace 成空白 -->
Test: {{ MUMI_JUMP_JUMP }}

{% if ouo? %} <!-- condition 只支援傳 boolean 進去 -->
ouo {{ secret }} <!-- 可以在 if 裡面擺 template tag ㄛ -->
{% else %}
QAQ
{% endif %}
```