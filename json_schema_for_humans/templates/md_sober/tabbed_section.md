#### {% if operator == "allOf" %}All of{% elif operator == "anyOf" %}Any of{% elif operator == "oneOf" %}One of{% endif %}

{% for node in current_node.array_items %}
<a id="{{ node.html_id }}"></a>
??? quote "[{% with schema=node %}{% include "breadcrumbs.md" %}{% endwith %}](#{{ node.html_id }})"

{% filter indent(4) %}
{% with schema=node, skip_headers=False, depth=depth+1 %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

{% endfor %}
