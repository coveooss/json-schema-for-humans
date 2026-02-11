{{ "Must be one of:" | md_render }}
{% for enum_choice in schema.kw_enum.array_items %}
* {{ enum_choice.literal | python_to_json }}
{% endfor %}