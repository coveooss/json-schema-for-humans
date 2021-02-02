

# Circular reference Schema

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [person](#person)|No|object|No|No| No|-|

##  <a name="person"></a>1.  Property `Circular reference Schema > person`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/circular.json', 'path_to_element': ['person'], 'html_id': 'person', 'breadcrumb_name': 'person', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adf40>, 'parent_key': 'person', 'ref_path': '#/definitions/a', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad9d0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad9d0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [a1](#person_a1)|No|string|No|No| No|Description from b|

###  <a name="person_a1"></a>1.1.  Property `Circular reference Schema > person > a1`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/circular.json', 'path_to_element': ['definitions', 'a', 'a1'], 'html_id': 'person_a1', 'breadcrumb_name': 'a1', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad9d0>, 'parent_key': 'a1', 'ref_path': '#/definitions/b', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad670>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad670>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`
         Default: `"Default from c"`

**Description:** Description from b

Type: `string`
         Default: `"Default from c"`

**Description:** Description from b

Type: `string`
         Default: `"Default from c"`

**Description:** Description from b

Type: `string`
         Default: `"Default from c"`

**Description:** Description from b

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:58 +0100