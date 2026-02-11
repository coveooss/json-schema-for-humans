<h4>Must be one of:</h4>
<ul>
{% for enum_choice in schema.kw_enum.array_items %}
<li><code>{{ enum_choice.literal | python_to_json }}</code>
{%- if schema.kw_meta_enum %}: {{ (schema.enum_description(enum_choice.literal) | get_description_literal) }}{% endif -%}
</li>
{% endfor %}
</ul>