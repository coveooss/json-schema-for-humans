{% if schema.kw_min_items %}<code>Min items: {{ schema.kw_min_items.literal }}</code> {% endif %}
{% if schema.kw_max_items %}<code>Max items: {{ schema.kw_max_items.literal }}</code> {% endif %}
{% if schema.kw_unique_items and schema.kw_unique_items.literal is true %}<code>Unique items: yes</code> {% endif %}

{% if schema.array_items_def %}
<h5>Array items: {% with schema=schema.array_items_def %}{%- include "breadcrumbs.md" %}{% endwith %}</h5>
<blockquote>
{% with schema=schema.array_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
    {% include "content.md" %}
{% endwith %}
</blockquote>
{% endif %}

{% if schema.tuple_validation_items %}
{% for item in schema.tuple_validation_items %}
<h5>Item {{ loop.index }}: {% with schema=item %}{%- include "breadcrumbs.md" %}{% endwith %}</h5>
<blockquote>
{% with schema=item, skip_headers=False, depth=depth+1, skip_required=True %}
    {% include "content.md" %}
{% endwith %}
</blockquote>
{% endfor %}
{% endif %}

{% if schema.kw_contains and schema.kw_contains.literal != {} %}
<h5>At least one of the items must be:</h5>
<blockquote>
{% with schema=schema.kw_contains, skip_headers=False, depth=depth+1, skip_required=True %}
    {% include "content.md" %}
{% endwith %}
</blockquote>
{% endif %}

{% if schema.array_additional_items_def %}
<h5>Additional items must be:</h5>
<blockquote>
{% with schema=schema.array_additional_items_def, skip_headers=False, depth=depth+1, skip_required=True %}
    {% include "content.md" %}
{% endwith %}
</blockquote>
{% endif %}
