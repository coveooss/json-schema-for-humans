

# Schema Docs

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [outer](#outer)|No|object|Yes|No| No|We should see this|
| [outer2](#outer2)|No|object|No|No| No|We should see this too|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

##  <a name="outer"></a>1.  Property `root > outer`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/description_with_ref.json', 'path_to_element': ['outer'], 'html_id': 'outer', 'breadcrumb_name': 'outer', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad940>, 'parent_key': 'outer', 'ref_path': '#/definitions/inner schema', 'literal': None, 'keywords': {'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad400>}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adac0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adac0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** We should see this

Type: `object`

**Description:** We should see this

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [inner](#outer_inner)|No|string|Yes|No| No|inner description|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="outer_inner"></a>1.1.  Property `root > outer > inner`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/description_with_ref.json', 'path_to_element': ['definitions', 'inner schema', 'inner'], 'html_id': 'outer_inner', 'breadcrumb_name': 'inner', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adac0>, 'parent_key': 'inner', 'ref_path': '', 'literal': None, 'keywords': {'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122391e50>, 'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122391730>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

**Description:** inner description

##  <a name="outer2"></a>2.  Property `root > outer2`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/description_with_ref.json', 'path_to_element': ['outer2'], 'html_id': 'outer2', 'breadcrumb_name': 'outer2', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad940>, 'parent_key': 'outer2', 'ref_path': '#/definitions/inner schema', 'literal': None, 'keywords': {'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223918b0>}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad520>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adac0>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** We should see this too
    Same definition as [outer](#outer)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:58 +0100