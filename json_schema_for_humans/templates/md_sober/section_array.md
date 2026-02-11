{% if schema.kw_min_items %}`Min items: {{ schema.kw_min_items.literal }}` {% endif %}
{% if schema.kw_max_items %}`Max items: {{ schema.kw_max_items.literal }}` {% endif %}
{% if schema.kw_unique_items and schema.kw_unique_items.literal is true %}`Unique items: yes` {% endif %}

{% if schema.array_items_def %}
??? tip "Array items: {% with schema=schema.array_items_def %}{%- include "breadcrumbs.md" %}{% endwith %}"

{% filter indent(4) %}
{% with schema=schema.array_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

{% endif %}

{% if schema.tuple_validation_items %}
{% for item in schema.tuple_validation_items %}
??? tip "Item {{ loop.index }}: {% with schema=item %}{%- include "breadcrumbs.md" %}{% endwith %}"

{% filter indent(4) %}
{% with schema=item, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

{% endfor %}
{% endif %}

{% if schema.kw_contains and schema.kw_contains.literal != {} %}
??? tip "At least one of the items must be:"

{% filter indent(4) %}
{% with schema=schema.kw_contains, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

{% endif %}

{% if schema.array_additional_items_def %}
??? tip "Additional items must be:"

{% filter indent(4) %}
{% with schema=schema.array_additional_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}
{% endfilter %}

{% endif %}
