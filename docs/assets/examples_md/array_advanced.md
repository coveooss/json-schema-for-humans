

# Schema Docs

Type: `object`

**Description:** A little food fun

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [fruits](#fruits)|No|array of string|No|No| No|5 to 8 fruits that you like|
| [vegetables](#vegetables)|No|array|No|No| No|-|

##  <a name="fruits"></a>1.  Property `root > fruits`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/array_advanced.json', 'path_to_element': ['fruits'], 'html_id': 'fruits', 'breadcrumb_name': 'fruits', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243ca00>, 'parent_key': 'fruits', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243ceb0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243cd90>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243c250>, 'minItems': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243cdc0>, 'maxItems': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243c970>, 'uniqueItems': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243c760>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array of string`

**Description:** 5 to 8 fruits that you like

<table>
 	<tr>
    <td><b>Min items</b></td>
    <td>5</td>
 	</tr>
	<tr>
    <td><b>Max items</b></td>
    <td>8</td>
	</tr>
	<tr>
    <td><b>Items unicity</b></td>
    <td>True</td>
 	</tr>
</table>

###  1. Each item of this array must be

Type: `string`

##  <a name="vegetables"></a>2.  Property `root > vegetables`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/array_advanced.json', 'path_to_element': ['vegetables'], 'html_id': 'vegetables', 'breadcrumb_name': 'vegetables', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243ca00>, 'parent_key': 'vegetables', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243c580>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243cca0>, 'contains': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12243ce20>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array`

<table>
 	<tr>
    <td><b>Min items</b></td>
    <td>N/A</td>
 	</tr>
	<tr>
    <td><b>Max items</b></td>
    <td>N/A</td>
	</tr>
	<tr>
    <td><b>Items unicity</b></td>
    <td>False</td>
 	</tr>
</table>

###  2. Each item of this array must be

Type: `object`

###  2. At least one of the items must be

Type: `const`

            Specific value: `"eggplant"`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:01:00 +0100