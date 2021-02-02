

# Schema Docs

Type: `object`

**Description:** A schema with an array

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [fruits](#fruits)|No|array of string|No|No| No|-|
| [vegetables](#vegetables)|No|array|No|No| No|-|

##  <a name="fruits"></a>1.  Property `root > fruits`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/array.json', 'path_to_element': ['fruits'], 'html_id': 'fruits', 'breadcrumb_name': 'fruits', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca400>, 'parent_key': 'fruits', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223cafd0>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca550>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array of string`

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

###  1. Each item of this array must be

Type: `string`

##  <a name="vegetables"></a>2.  Property `root > vegetables`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/array.json', 'path_to_element': ['vegetables'], 'html_id': 'vegetables', 'breadcrumb_name': 'vegetables', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca400>, 'parent_key': 'vegetables', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca880>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca430>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

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

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [veggieName](#vegetables_items_veggieName)|No|string|Yes|No| No|The name of the vegetable.|
| [veggieLike](#vegetables_items_veggieLike)|No|boolean|Yes|No| No|Do I like this vegetable?|

###  <a name="vegetables_items_veggieName"></a>2.1.  Property `root > vegetables > items > veggieName`

      {'depth': 3, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/array.json', 'path_to_element': ['definitions', 'veggie', 'veggieName'], 'html_id': 'vegetables_items_veggieName', 'breadcrumb_name': 'veggieName', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca790>, 'parent_key': 'veggieName', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223cadc0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223cadf0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** The name of the vegetable.

###  <a name="vegetables_items_veggieLike"></a>2.2.  Property `root > vegetables > items > veggieLike`

      {'depth': 3, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/array.json', 'path_to_element': ['definitions', 'veggie', 'veggieLike'], 'html_id': 'vegetables_items_veggieLike', 'breadcrumb_name': 'veggieLike', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca790>, 'parent_key': 'veggieLike', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223cac40>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ca280>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `boolean`

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100