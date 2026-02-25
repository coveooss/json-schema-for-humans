{% set admonition_types = ['quote', 'example', 'bug', 'tip', 'abstract', 'info'] %}
{% for sub_property in schema.iterate_properties %}
{% if sub_property.is_additional_properties and not sub_property.is_additional_properties_schema %}
{% continue %}
{% endif %}

{% set html_id = sub_property.html_id %}

<a id="{{ html_id }}"></a>

/// details | <strong>{{ sub_property.property_display_name | escape }}</strong>{% if sub_property.is_required_property %} ==Required=={% endif %}{% if sub_property is deprecated %} <span class='badge deprecated'>Deprecated</span>{% endif %}{% if sub_property.is_pattern_property %} <span class='badge pattern'>Pattern</span>{% endif %}

    type: {{ admonition_types[depth % 6] }}

{% if sub_property.is_pattern_property %}
<p><em>Pattern Property</em>: All properties whose name matches the regular expression
<code>{{ sub_property.property_name }}</code> (<a href="https://regex101.com/?regex={{ sub_property.property_name | urlencode }}">Test</a>)
must respect the following conditions</p>

{% endif %}
{% if sub_property.is_additional_properties %}
{% if sub_property.is_additional_properties_schema %}
<p><em>Each additional property must conform to the following schema</em></p>

{% else %}
<p><em>Additional Properties of any type are allowed.</em></p>

{% endif %}
{% endif %}
{% with schema=sub_property, skip_headers=False, depth=depth+1 %}
{% include "content.md" %}
{% endwith %}

///

{% endfor %}
