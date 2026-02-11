{% for sub_property in schema.iterate_properties %}
  {%- if sub_property.is_additional_properties and not sub_property.is_additional_properties_schema -%}
    {% continue %}
  {% endif %}

  {% set html_id = sub_property.html_id %}

  {% set description = sub_property | get_description %}
<a id="{{ html_id }}"></a>
??? quote "[{% if sub_property is deprecated %}~~{% endif %}{% with schema=sub_property %}{% include "breadcrumbs.md" %}{% endwith %}{% if sub_property is deprecated %}~~{% endif %}{% if not skip_required and sub_property.property_name and sub_property.is_required_property %} `Required`{% endif %}](#{{ html_id }})"

  {% if sub_property.is_pattern_property %}
    !!! info "Pattern Property"
        All properties whose name matches the regular expression
        `{{ sub_property.property_name }}` ([Test](https://regex101.com/?regex={{ sub_property.property_name | urlencode }}))
        must respect the following conditions

  {% endif %}
{% filter indent(4) %}
{% with schema=sub_property, skip_headers=False, depth=depth+1 %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

{% endfor %}
