{% if config.show_breadcrumbs %}
<nav>{% for node in schema.nodes_from_root %}{% if loop.first %}root{% else %}<a href="#{{ node.html_id }}">{{ node.name_for_breadcrumbs }}</a>{% endif %}{% if not loop.last %} &rarr; {% endif %}{% endfor %}</nav>
{% endif %}
