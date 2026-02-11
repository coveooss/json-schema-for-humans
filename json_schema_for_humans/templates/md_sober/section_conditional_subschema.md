{% if schema.kw_if %}
    {% set first_property =  schema.kw_if | get_first_property %}

    {% if schema.kw_then %}
??? quote "If (`{{ first_property.property_name | escape }} = {{ first_property.const_value | python_to_json }}`)"

{% filter indent(4) %}
{% with schema=schema.kw_then, skip_headers=False, depth=depth %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

    {% endif %}
    {% if schema.kw_else %}
??? quote "Else (`{{ first_property.property_name | escape }} != {{ first_property.const_value | python_to_json }}`)"

{% filter indent(4) %}
{% with schema=schema.kw_else, skip_headers=False, depth=depth %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

    {% endif %}
{% endif %}