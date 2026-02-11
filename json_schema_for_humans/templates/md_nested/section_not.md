<h4>Must <strong>not</strong> be:</h4>
<blockquote>
{% with schema=schema.kw_not, skip_headers=False, depth=depth+1, skip_required=True %}
    {% include "content.md" %}
{% endwith %}
</blockquote>