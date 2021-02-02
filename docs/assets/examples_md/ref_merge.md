

# Test

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [aProperty](#aProperty)|No|enum (of string)|No|No| No|This is the description from the definition|
| [aDictPropertyARequired](#aDictPropertyARequired)|No|object|No|No| No|-|

##  <a name="aProperty"></a>1.  Property `Test > aProperty`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/ref_merge.json', 'path_to_element': ['aProperty'], 'html_id': 'aProperty', 'breadcrumb_name': 'aProperty', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1225197f0>, 'parent_key': 'aProperty', 'ref_path': '#/definitions/aProperty', 'literal': None, 'keywords': {'default': '"Default from property"', 'enum': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1225193a0>}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122519d30>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122519d30>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `enum (of string)`
         Default: `"Default from property"`

**Description:** This is the description from the definition

Type: `enum (of string)`
         Default: `"Default from property"`

**Description:** This is the description from the definition

            Must be one of:
                * "value1"
                * "value2"

##  <a name="aDictPropertyARequired"></a>2.  Property `Test > aDictPropertyARequired`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/ref_merge.json', 'path_to_element': ['aDictPropertyARequired'], 'html_id': 'aDictPropertyARequired', 'breadcrumb_name': 'aDictPropertyARequired', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1225197f0>, 'parent_key': 'aDictPropertyARequired', 'ref_path': '#/definitions/aDictProperty', 'literal': None, 'keywords': {'required': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cf730>}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cfd00>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cfd00>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`
         Default: `{"a": "a", "b": "b"}`

Type: `object`
         Default: `{"a": "a", "b": "b"}`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [a](#aDictPropertyARequired_a)|No|string|Yes|No| No|-|
| [b](#aDictPropertyARequired_b)|No|string|Yes|No| No|-|

###  <a name="aDictPropertyARequired_a"></a>2.1.  Property `Test > aDictPropertyARequired > a`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/ref_merge.json', 'path_to_element': ['definitions', 'aDictProperty', 'a'], 'html_id': 'aDictPropertyARequired_a', 'breadcrumb_name': 'a', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cfd00>, 'parent_key': 'a', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cf760>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="aDictPropertyARequired_b"></a>2.2.  Property `Test > aDictPropertyARequired > b`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/ref_merge.json', 'path_to_element': ['definitions', 'aDictProperty', 'b'], 'html_id': 'aDictPropertyARequired_b', 'breadcrumb_name': 'b', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cfd00>, 'parent_key': 'b', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224cfb20>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100