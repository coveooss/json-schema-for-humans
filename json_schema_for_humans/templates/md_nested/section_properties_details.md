{% for sub_property in schema.iterate_properties %}
  {%- if sub_property.is_additional_properties and not sub_property.is_additional_properties_schema -%}
    {% continue %}
  {% endif %}

  {% set html_id = sub_property.html_id %}

  {% set description = sub_property | get_description %}
<details>
<summary>
  <strong>
  {%- if sub_property is deprecated -%}~~{%- endif -%}
  <a name="{{ html_id }}"></a>{{ sub_property.property_display_name | escape }}
  {%- if sub_property is deprecated -%}~~ ❗{%- endif -%}
  </strong>
  {%- if not skip_required and sub_property.property_name and sub_property.is_required_property -%}
    {{ " " }}<code>Required</code>
  {%- endif -%}
  {%- if sub_property.is_pattern_property %} <code>Pattern</code>{%- endif -%}

</summary>

  {% if sub_property.is_pattern_property %}
<blockquote>
All properties whose name matches the regular expression
<code>{{ sub_property.property_name }}</code> (<a href="https://regex101.com/?regex={{ sub_property.property_name | urlencode }}">Test</a>)
must respect the following conditions
</blockquote>
  {% endif %}

  {% with schema=sub_property, skip_headers=False, depth=depth+1 %}
    {% include "content.md" %}
  {% endwith %}

</details>

{% endfor %}