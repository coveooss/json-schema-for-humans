{% if schema.kw_min_items %}
<p><strong>Minimum items:</strong> {{ schema.kw_min_items.literal }}</p>
{% endif %}
{% if schema.kw_max_items %}
<p><strong>Maximum items:</strong> {{ schema.kw_max_items.literal }}</p>
{% endif %}
{% if schema.kw_unique_items and schema.kw_unique_items.literal is true %}
<p><strong>Unique items:</strong> Yes</p>
{% endif %}
{% if not schema.array_additional_items %}
<span class="badge info">No Additional Items</span>
{% endif %}

{% if schema.array_items_def %}
<p><strong>Each item of this array must be:</strong></p>
<a id="{{ schema.array_items_def.html_id }}"></a>

{% with schema=schema.array_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}

{% endif %}

{% if schema.tuple_validation_items %}
<h5>Tuple Validation</h5>
{% for item in schema.tuple_validation_items %}
/// tab | Item {{ loop.index }}

<a id="{{ item.html_id }}"></a>

{% with schema=item, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}

///
{% endfor %}

{% endif %}

{% if schema.kw_contains and schema.kw_contains.literal != {} %}
<p><strong>At least one of the items must be:</strong></p>
<a id="{{ schema.kw_contains.html_id }}"></a>

{% with schema=schema.kw_contains, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}

{% endif %}

{% if schema.array_additional_items_def %}
<p><strong>All other items must be:</strong></p>
<a id="{{ schema.array_additional_items_def.html_id }}"></a>

{% with schema=schema.array_additional_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
{% include "content.md" %}
{% endwith %}

{% endif %}
