{% if schema.kw_if %}
    {% set first_property =  schema.kw_if | get_first_property %}

    {% if schema.kw_then %}
<h5>If (<code>{{ first_property.property_name | escape }} = {{ first_property.const_value | python_to_json }}</code>)</h5>
<blockquote>
{% with schema=schema.kw_then, skip_headers=False, depth=depth %}
    {% include "content.md" %}
{% endwith %}
</blockquote>
    {% endif %}
    {% if schema.kw_else %}
<h5>Else (<code>{{ first_property.property_name | escape }} != {{ first_property.const_value | python_to_json }}</code>)</h5>
<blockquote>
{% with schema=schema.kw_else, skip_headers=False, depth=depth %}
    {% include "content.md" %}
{% endwith %}
</blockquote>
    {% endif %}
{% endif %}