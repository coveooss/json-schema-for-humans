{% set skip_headers = skip_headers or False %}
{% set depth = depth or 0 %}

{% set keys = schema.keywords %}
{% set type_name = schema.type_name %}

{% if not skip_headers %}
{% if config.show_breadcrumbs %}
{% include "breadcrumbs.md" %}
{% endif %}

{% if schema.title and schema.title | length > 0 and schema.depth > 0 %}
<h4>{{ schema.title }}</h4>
{% endif %}

{% if not schema is combining %}
<span class="badge type">Type: {{ type_name }}</span>
{% endif %}
{% if schema.format %}
<span class="badge format">Format: {{ schema.format }}</span>
{% endif %}
{% set default_value = schema.default_value %}
{% if default_value %}
<span class="badge default">Default: {{ default_value }}</span>
{% endif %}

{% set description = (schema | get_description) %}
{% include "section_description.md" %}
{% endif %}

{% if schema.should_be_a_link(config) %}
<a href="#{{ schema.links_to.html_id }}">Same definition as {{ schema.links_to.link_name }}</a>
{% elif schema.refers_to %}
{% with schema=schema.refers_to_merged, skip_headers=True, depth=depth %}
{% include "content.md" %}
{% endwith %}
{% else %}

{% if schema.explicit_no_additional_properties %}
<span class="badge info">No Additional Properties</span>
{% endif %}

{% if schema.kw_all_of %}
{% with operator="allOf", current_node=schema.kw_all_of, skip_required=True %}
{% include "tabbed_section.md" %}
{% endwith %}
{% endif %}
{% if schema.kw_any_of %}
{% with operator="anyOf", current_node=schema.kw_any_of, skip_required=True %}
{% include "tabbed_section.md" %}
{% endwith %}
{% endif %}
{% if schema.kw_one_of %}
{% with operator="oneOf", current_node=schema.kw_one_of, skip_required=True %}
{% include "tabbed_section.md" %}
{% endwith %}
{% endif %}
{% if schema.kw_not %}
{% include "section_not.md" %}
{% endif %}

{% if schema.kw_enum %}
<h5>Must be one of:</h5>
<ul>
{% for enum_choice in schema.kw_enum.array_items %}
<li><code>{{ enum_choice.literal | python_to_json }}</code>{% if schema.kw_meta_enum %}: {{ (schema.enum_description(enum_choice.literal) | get_description_literal) }}{% endif %}</li>
{% endfor %}
</ul>
{% endif %}
{% if schema.is_const %}
<span class="badge">Specific value: <code>{{ schema.const_value | python_to_json }}</code></span>
{% endif %}

{% if schema.kw_pattern %}
<span class="badge">Must match regex: <code>{{ schema.kw_pattern.literal | escape }}</code></span>
{% endif %}

{% if schema.has_conditional %}
{% with skip_headers=False, depth=depth+1 %}
{% include "section_conditional_subschema.md" %}
{% endwith %}
{% endif %}

{% include "section_undocumented_required_properties.md" %}
{% include "badge_type.md" %}

{% if type_name.startswith("array") %}
{% include "section_array.md" %}
{% endif %}

{% set examples = schema.examples %}
{% if examples %}
{% include "section_examples.md" %}
{% endif %}

{% if schema.is_object %}
{% with skip_required=False %}
{% include "section_properties_details.md" %}
{% endwith %}
{% endif %}
{% endif %}
