{%- set type_name = schema.type_name -%}
{%- if type_name == "string" -%}
    {%- if schema.kw_min_length -%}
<code>Min length: {{ schema.kw_min_length.literal }}</code>
    {%- endif -%}
    {%- if schema.kw_max_length -%}
<code>Max length: {{ schema.kw_max_length.literal }}</code>
    {%- endif -%}
{%- endif -%}
{%- if type_name in ["integer", "number"] -%}
    {%- set restriction_text = (schema | get_numeric_restrictions_text("", "")) -%}
    {%- if restriction_text -%}
<code>{{ restriction_text }}</code>
    {%- endif -%}
{%- endif -%}
