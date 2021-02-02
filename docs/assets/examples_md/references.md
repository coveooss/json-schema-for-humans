

# Schema Docs

Type: `object`

**Description:** Testing $ref

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [a_gift](#a_gift)|No|string|No|No| No|A gift, or is it?|
| [anchor_with_slash](#anchor_with_slash)|No|object|No|No| No|-|
| [anchor_no_slash](#anchor_no_slash)|No|array of string|No|No| No|Description for array_def|
| [anchor_nested_reference](#anchor_nested_reference)|No|string|No|No| No|-|
| [same_file_anchor_with_slash](#same_file_anchor_with_slash)|No|string|No|No| No|Description for string_def|
| [same_file_anchor_no_slash](#same_file_anchor_no_slash)|No|object|No|No| No|-|
| [same_file_nested_reference](#same_file_nested_reference)|No|string|No|No| No|-|
| [other_file_anchor](#other_file_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_dot_anchor](#other_file_dot_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_dot_dot_anchor](#other_file_dot_dot_anchor)|No|object|No|No| No|The delivery is a gift, no prices displayed|
| [other_file_only](#other_file_only)|No|object|No|No| No|Test schema with a not|
| [multi_hierarchy_reference](#multi_hierarchy_reference)|No|object|No|No| No|-|

##  <a name="a_gift"></a>1.  Property `root > a_gift`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['a_gift'], 'html_id': 'a_gift', 'breadcrumb_name': 'a_gift', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'a_gift', 'ref_path': '#/definitions/gift', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adf70>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adf70>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** A gift, or is it?

Type: `string`

**Description:** A gift, or is it?

##  <a name="anchor_with_slash"></a>2.  Property `root > anchor_with_slash`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['anchor_with_slash'], 'html_id': 'anchor_with_slash', 'breadcrumb_name': 'anchor_with_slash', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'anchor_with_slash', 'ref_path': '#/definitions/object_def', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad730>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad730>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propertyA](#anchor_with_slash_propertyA)|No|string|No|No| No|Description for object_def/items/propertyA|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="anchor_with_slash_propertyA"></a>2.1.  Property `root > anchor_with_slash > propertyA`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['definitions', 'object_def', 'propertyA'], 'html_id': 'anchor_with_slash_propertyA', 'breadcrumb_name': 'propertyA', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad730>, 'parent_key': 'propertyA', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ade50>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adfd0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** Description for object_def/items/propertyA

##  <a name="anchor_no_slash"></a>3.  Property `root > anchor_no_slash`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['anchor_no_slash'], 'html_id': 'anchor_no_slash', 'breadcrumb_name': 'anchor_no_slash', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'anchor_no_slash', 'ref_path': '#definitions/array_def', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc40>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc40>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `array of string`

**Description:** Description for array_def

Type: `array of string`

**Description:** Description for array_def

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

###  3. Each item of this array must be

Type: `string`

##  <a name="anchor_nested_reference"></a>4.  Property `root > anchor_nested_reference`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['anchor_nested_reference'], 'html_id': 'anchor_nested_reference', 'breadcrumb_name': 'anchor_nested_reference', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'anchor_nested_reference', 'ref_path': '#/definitions/reference_def', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adfa0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adfa0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

Type: `string`

Type: `string`

##  <a name="same_file_anchor_with_slash"></a>5.  Property `root > same_file_anchor_with_slash`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['same_file_anchor_with_slash'], 'html_id': 'same_file_anchor_with_slash', 'breadcrumb_name': 'same_file_anchor_with_slash', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'same_file_anchor_with_slash', 'ref_path': 'references.json#/definitions/string_def', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223add90>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223add90>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** Description for string_def

Type: `string`

**Description:** Description for string_def

##  <a name="same_file_anchor_no_slash"></a>6.  Property `root > same_file_anchor_no_slash`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['same_file_anchor_no_slash'], 'html_id': 'same_file_anchor_no_slash', 'breadcrumb_name': 'same_file_anchor_no_slash', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'same_file_anchor_no_slash', 'ref_path': 'references.json#definitions/object_def', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad580>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad730>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

    Same definition as [anchor_with_slash](#anchor_with_slash)

##  <a name="same_file_nested_reference"></a>7.  Property `root > same_file_nested_reference`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['same_file_nested_reference'], 'html_id': 'same_file_nested_reference', 'breadcrumb_name': 'same_file_nested_reference', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'same_file_nested_reference', 'ref_path': 'references.json#/definitions/reference_def', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad6a0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adfa0>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

    Same definition as [anchor_nested_reference](#anchor_nested_reference)

##  <a name="other_file_anchor"></a>8.  Property `root > other_file_anchor`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['other_file_anchor'], 'html_id': 'other_file_anchor', 'breadcrumb_name': 'other_file_anchor', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'other_file_anchor', 'ref_path': 'with_descriptions.json#/definitions/gift', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc10>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc10>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** The delivery is a gift, no prices displayed

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [with_wrap](#other_file_anchor_with_wrap)|No|boolean|No|No| No|-|

###  <a name="other_file_anchor_with_wrap"></a>8.1.  Property `root > other_file_anchor > with_wrap`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['definitions', 'gift', 'with_wrap'], 'html_id': 'other_file_anchor_with_wrap', 'breadcrumb_name': 'with_wrap', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc10>, 'parent_key': 'with_wrap', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398610>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `boolean`

##  <a name="other_file_dot_anchor"></a>9.  Property `root > other_file_dot_anchor`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['other_file_dot_anchor'], 'html_id': 'other_file_dot_anchor', 'breadcrumb_name': 'other_file_dot_anchor', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'other_file_dot_anchor', 'ref_path': './with_descriptions.json#/definitions/gift', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad430>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc10>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** The delivery is a gift, no prices displayed
    Same definition as [other_file_anchor](#other_file_anchor)

##  <a name="other_file_dot_dot_anchor"></a>10.  Property `root > other_file_dot_dot_anchor`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['other_file_dot_dot_anchor'], 'html_id': 'other_file_dot_dot_anchor', 'breadcrumb_name': 'other_file_dot_dot_anchor', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'other_file_dot_dot_anchor', 'ref_path': '../cases/with_descriptions.json#/definitions/gift', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad430>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adc10>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** The delivery is a gift, no prices displayed
    Same definition as [other_file_anchor](#other_file_anchor)

##  <a name="other_file_only"></a>11.  Property `root > other_file_only`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['other_file_only'], 'html_id': 'other_file_only', 'breadcrumb_name': 'other_file_only', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'other_file_only', 'ref_path': 'combining_not.json', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398cd0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398cd0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Test schema with a not

Type: `object`

**Description:** Test schema with a not

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [not_a_string](#other_file_only_not_a_string)|No|object|Yes|No| No|-|

###  <a name="other_file_only_not_a_string"></a>11.1.  Property `root > other_file_only > not_a_string`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/combining_not.json', 'path_to_element': ['', 'not_a_string'], 'html_id': 'other_file_only_not_a_string', 'breadcrumb_name': 'not_a_string', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398cd0>, 'parent_key': 'not_a_string', 'ref_path': '', 'literal': None, 'keywords': {'not': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398220>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

#### Must **not** be

Type: `string`

##  <a name="multi_hierarchy_reference"></a>12.  Property `root > multi_hierarchy_reference`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references.json', 'path_to_element': ['multi_hierarchy_reference'], 'html_id': 'multi_hierarchy_reference', 'breadcrumb_name': 'multi_hierarchy_reference', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad280>, 'parent_key': 'multi_hierarchy_reference', 'ref_path': 'reference_schemas/intermediate.json#/properties/cross_file_reference', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398fa0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398fa0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propertyA](#multi_hierarchy_reference_propertyA)|No|string|No|No| No|Contents of propertyA in final.json|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="multi_hierarchy_reference_propertyA"></a>12.1.  Property `root > multi_hierarchy_reference > propertyA`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/reference_schemas/final.json', 'path_to_element': ['definitions', 'final_object_content', 'propertyA'], 'html_id': 'multi_hierarchy_reference_propertyA', 'breadcrumb_name': 'propertyA', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223986d0>, 'parent_key': 'propertyA', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398a30>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122398b50>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** Contents of propertyA in final.json

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100