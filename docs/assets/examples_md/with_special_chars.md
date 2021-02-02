

# Personne

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [prénom](#pr_nom)|No|string|No|No| No|Le prénom de la personne.|
| [nomDeFamille](#nomDeFamille)|No|string|No|No| No|Le nom de famille de la personne.|
| [âge](#a_ge)|No|integer|No|No| No|L'âge en années qui doit être plus grand ou égal à 0.|
| [0 de quoi d'autre](#a0_de_quoi_d_autre)|No|string|No|No| No|-|

##  <a name="pr_nom"></a>1.  Property `Personne > prénom`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_special_chars.json', 'path_to_element': ['prénom'], 'html_id': 'pr_nom', 'breadcrumb_name': 'prénom', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e7f0>, 'parent_key': 'prénom', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248ed60>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460bb0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** Le prénom de la personne.

##  <a name="nomDeFamille"></a>2.  Property `Personne > nomDeFamille`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_special_chars.json', 'path_to_element': ['nomDeFamille'], 'html_id': 'nomDeFamille', 'breadcrumb_name': 'nomDeFamille', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e7f0>, 'parent_key': 'nomDeFamille', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460040>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224600d0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** Le nom de famille de la personne.

##  <a name="a_ge"></a>3.  Property `Personne > âge`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_special_chars.json', 'path_to_element': ['âge'], 'html_id': 'a_ge', 'breadcrumb_name': 'âge', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e7f0>, 'parent_key': 'âge', 'ref_path': '', 'literal': None, 'keywords': {'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224609a0>, 'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224603d0>, 'minimum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122465940>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `integer`

**Description:** L'âge en années qui doit être plus grand ou égal à 0.

        Value must be greater or equal to `0`

##  <a name="a0_de_quoi_d_autre"></a>4.  Property `Personne > 0 de quoi d'autre`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_special_chars.json', 'path_to_element': ["0 de quoi d'autre"], 'html_id': 'a0_de_quoi_d_autre', 'breadcrumb_name': "0 de quoi d'autre", 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248e7f0>, 'parent_key': "0 de quoi d'autre", 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224652e0>, 'examples': ['"🖖"', '"صباح الخير"', '"你好"']}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Examples:** 

```
    <div class="highlight"><pre><span></span><span class="s2">&quot;🖖&quot;</span>
</pre></div>

```
```
    <div class="highlight"><pre><span></span><span class="s2">&quot;صباح الخير&quot;</span>
</pre></div>

```
```
    <div class="highlight"><pre><span></span><span class="s2">&quot;你好&quot;</span>
</pre></div>

```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:57 +0100