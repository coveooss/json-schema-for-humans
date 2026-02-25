<h4>{% if operator == "allOf" %}All of{% elif operator == "anyOf" %}Any of{% elif operator == "oneOf" %}One of{% endif %}</h4>

{% for node in current_node.array_items %}
/// tab | {{ node.definition_name or (("Requirement" if operator == "allOf" else "Option") ~ " " ~ loop.index) }}

<a id="{{ node.html_id }}"></a>

{% with schema=node, skip_headers=False, depth=depth+1 %}
{% include "content.md" %}
{% endwith %}

///
{% endfor %}
