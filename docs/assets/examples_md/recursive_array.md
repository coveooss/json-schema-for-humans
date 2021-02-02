

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|array|No|No| No|A list of people|

##  <a name="person"></a>1.  Property `Person > person`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_array.json', 'path_to_element': ['person'], 'html_id': 'person', 'breadcrumb_name': 'person', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b7670>, 'parent_key': 'person', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b72e0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b7610>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b7880>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array`

**Description:** A list of people

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

Type: `object`

**Description:** A human being

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [children](#person_items_children)|No|array|No|No| No|The children they had|

###  <a name="person_items_children"></a>1.1.  Property `Person > person > items > children`

      {'depth': 3, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_array.json', 'path_to_element': ['definitions', 'person', 'children'], 'html_id': 'person_items_children', 'breadcrumb_name': 'children', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b7e20>, 'parent_key': 'children', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b79a0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b7790>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224b7940>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

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
    Same definition as [person](#person_items)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100