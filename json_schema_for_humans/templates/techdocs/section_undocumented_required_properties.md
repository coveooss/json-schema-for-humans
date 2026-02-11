{% set undocumented_required_properties = schema | get_undocumented_required_properties %}
{% if undocumented_required_properties%}
<h5>The following properties are required:</h5>
<ul>
{% for required_property in undocumented_required_properties %}
<li><code>{{ required_property }}</code></li>
{% endfor %}
</ul>
{% endif %}