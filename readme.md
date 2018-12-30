![](https://img.shields.io/badge/python-3.6-blue.svg)


```shell=
$ python run.py
```

```shell=
$ git clone https://github.com/kehanlu/Tacobro.git
$ cd tacobro
$ pip install -r requirements.txt
```

## Branch

- master/ 
- release/ 放在伺服器上的版本
- dev/{user} 開發版本

## Controller

RESTFUL STYLE

[Document](https://github.com/kehanlu/Tacobro/wiki/Controller)

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
