{% set admonition_types = ['quote', 'example', 'bug', 'tip', 'abstract', 'info'] %}
{% if schema.kw_if %}
{% set first_property = schema.kw_if | get_first_property %}

{% if schema.kw_then %}
/// details | <strong>If</strong> <code>{{ first_property.property_name | escape }}</code> = <code>{{ first_property.const_value | python_to_json }}</code>
    type: {{ admonition_types[depth % 6] }}

{% with schema=schema.kw_then, skip_headers=False, depth=depth %}
{% include "content.md" %}
{% endwith %}

///

{% endif %}

{% if schema.kw_else %}
/// details | <strong>Else</strong> <code>{{ first_property.property_name | escape }}</code> != <code>{{ first_property.const_value | python_to_json }}</code>
    type: {{ admonition_types[depth % 6] }}

{% with schema=schema.kw_else, skip_headers=False, depth=depth %}
{% include "content.md" %}
{% endwith %}

///

{% endif %}
{% endif %}
