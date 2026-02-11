<strong>Example{{ "s" if examples|length > 1 else "" }}:</strong>

{% for example in examples %}
{% set example_id = schema.html_id ~ "_ex" ~ loop.index %}
<pre><code class="language-{% if not examples_as_yaml %}json{% else %}yaml{% endif %}">
{%- if not examples_as_yaml -%}
{{ example }}
{%- else -%}
{{ example | yaml_example }}
{%- endif -%}
</code></pre>
{% endfor %}