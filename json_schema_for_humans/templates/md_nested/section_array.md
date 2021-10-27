{{ schema | md_array_restrictions | md_generate_table }}

{% if schema.kw_items %}
{{ schema | md_array_items_restrictions | md_generate_table }}

{% for item in schema.kw_items %}
    {% filter md_heading(depth+1, item.html_id) %}
    {% with schema=item %}{%- include "breadcrumbs.md" %}{% endwith %}
    {% endfilter %}
    {% with schema=item, skip_headers=False, depth=depth+1, skip_required=True %}
        {% include "content.md" %}
    {% endwith %}
{% endfor %}
{% endif %}

{% if schema.kw_contains and schema.kw_contains.literal != {} %}
{{ "At least one of the items must be" | md_heading(depth+1) }}
{% with schema=schema.kw_contains, skip_headers=False, depth=depth+1, skip_required=True %}
    {% include "content.md" %}
{% endwith %}
{% endif %}