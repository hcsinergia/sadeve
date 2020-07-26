
{% extends "admin/base.html" %}
# {% block title %}{{title}} | {{ site_title}}{% endblock% }
{% block title %}
{{SADeVe}} | {{'123'}}
{% endblock% }

{%  block branding %}
<h1 id="site-map"><a href="{% url 'admin:index' %}"> SADeVe Administracion </a> </h1>
{% endblock% }

{%  block nav-global %}{% endblock %}
