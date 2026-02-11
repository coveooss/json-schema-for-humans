{# Display description #}
{% if description %}
{{ ("**Description:** " ~ description) | md_render }}
{% endif %}