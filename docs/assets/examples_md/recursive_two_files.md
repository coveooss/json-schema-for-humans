

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No|A human being|

##  <a name="person"></a>1.  Property `Person > person`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_two_files.json', 'path_to_element': ['person'], 'html_id': 'person', 'breadcrumb_name': 'person', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488bb0>, 'parent_key': 'person', 'ref_path': '#/definitions/person', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488550>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488550>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** A human being

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [children](#person_children)|No|array|No|No| No|The children they had|
| [siblings](#person_siblings)|No|object|No|No| No|Person definition from second file. Not the same!|

###  <a name="person_children"></a>1.1.  Property `Person > person > children`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_two_files.json', 'path_to_element': ['definitions', 'person', 'children'], 'html_id': 'person_children', 'breadcrumb_name': 'children', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488550>, 'parent_key': 'children', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488040>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488eb0>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224889d0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array`

**Description:** The children they had

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

####  1.1. Each item of this array must be

Type: `object`

**Description:** Person definition from second file. Not the same!
    Same definition as [siblings](#person_siblings)

###  <a name="person_siblings"></a>1.2.  Property `Person > person > siblings`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_two_files.json', 'path_to_element': ['definitions', 'person', 'siblings'], 'html_id': 'person_siblings', 'breadcrumb_name': 'siblings', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488550>, 'parent_key': 'siblings', 'ref_path': 'recursive_two_files2.json#/definitions/person', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224882b0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224882b0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Person definition from second file. Not the same!

Type: `object`

**Description:** Person definition from second file. Not the same!

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:56 +0100