

# User Preference

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [favorite_os](#favorite_os)|No|enum (of string)|No|No| No|-|
| [favorite_colors](#favorite_colors)|No|array of enum (of string)|No|No| No|-|
| [desired_number_of_shoes](#desired_number_of_shoes)|No|integer|No|No| No|-|

##  <a name="favorite_os"></a>1.  Property `User Preference > favorite_os`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_default.json', 'path_to_element': ['favorite_os'], 'html_id': 'favorite_os', 'breadcrumb_name': 'favorite_os', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398be0>, 'parent_key': 'favorite_os', 'ref_path': '', 'literal': None, 'keywords': {'enum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398190>, 'default': '"Linux"'}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `enum (of string)`
         Default: `"Linux"`

            Must be one of:
                * "Windows"
                * "Mac"
                * "Linux"

##  <a name="favorite_colors"></a>2.  Property `User Preference > favorite_colors`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_default.json', 'path_to_element': ['favorite_colors'], 'html_id': 'favorite_colors', 'breadcrumb_name': 'favorite_colors', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398be0>, 'parent_key': 'favorite_colors', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223984f0>, 'items': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398850>, 'default': '["white", "blue"]'}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array of enum (of string)`
         Default: `["white", "blue"]`

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

Type: `enum (of string)`

            Must be one of:
                * "green"
                * "blue"
                * "orange"
                * "red"
                * "white"
                * "black"

##  <a name="desired_number_of_shoes"></a>3.  Property `User Preference > desired_number_of_shoes`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_default.json', 'path_to_element': ['desired_number_of_shoes'], 'html_id': 'desired_number_of_shoes', 'breadcrumb_name': 'desired_number_of_shoes', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398be0>, 'parent_key': 'desired_number_of_shoes', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398a90>, 'minimum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223982e0>, 'maximum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398430>, 'default': '2'}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `integer`
         Default: `2`

        Value must be greater or equal to `0` and lesser or equal to `2`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:58 +0100