

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No|A human being|

##  <a name="person"></a>1.  Property `Person > person`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive.json', 'path_to_element': ['person'], 'html_id': 'person', 'breadcrumb_name': 'person', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fda90>, 'parent_key': 'person', 'ref_path': '#/definitions/person', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd370>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd370>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** A human being

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [children](#person_children)|No|array|No|No| No|The children they had|

###  <a name="person_children"></a>1.1.  Property `Person > person > children`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive.json', 'path_to_element': ['definitions', 'person', 'children'], 'html_id': 'person_children', 'breadcrumb_name': 'children', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd370>, 'parent_key': 'children', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd3d0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fdcd0>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224fd4c0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

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

**Description:** A human being
    Same definition as [person](#person)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100