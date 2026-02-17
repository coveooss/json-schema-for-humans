{% set depth = 0 %}
<h1>{{ schema.keywords.get("title").literal | default("Schema Docs") }}</h1>

{% with schema=schema, skip_headers=False, depth=depth %}
{% include "content.md" %}
{% endwith %}

<hr/>
{% if config.with_footer %}
<footer>
<em>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a>{% if config.footer_show_time %} on {{ get_local_time() }}{% endif %}</em>
</footer>
{% endif %}
