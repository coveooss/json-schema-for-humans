{% filter md_escape_for_table %}
{%- if config.show_breadcrumbs %}
  {%- for node in schema.nodes_from_root -%}
    {{ node.name_for_breadcrumbs }}{%- if not loop.last %} > {% endif -%}
  {%- endfor -%}
{%- else -%}
  {%- if schema.property_name -%}
    {{- schema.property_name -}}
  {%- else -%}
    {{ schema.name_for_breadcrumbs }}
  {%- endif -%}
{% endif %}
{% endfilter %}
