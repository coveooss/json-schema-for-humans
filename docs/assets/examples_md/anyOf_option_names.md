

# Schema Docs

Type: `object`

**Description:** JSON Schema for an fstab entry

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [storage](#storage)|No|object|Yes|No| No|-|

##  <a name="storage"></a>1.  Property `root > storage`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/anyOf_option_names.json', 'path_to_element': ['storage'], 'html_id': 'storage', 'breadcrumb_name': 'storage', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223adf40>, 'parent_key': 'storage', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad6d0>, 'anyOf': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223ad490>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

| Node | 
| ---- |
| [diskDevice](#storage_anyOf_i0) |
| [diskUUID](#storage_anyOf_i1) |
| [Any of(Option) 3](#storage_anyOf_i2) |
| [tmpfs](#storage_anyOf_i3) |
###  <a name="storage"></a>1.1.  Property `root > storage > anyOf > diskDevice`

Type: `object`

Type: `object`

###  <a name="storage"></a>1.2.  Property `root > storage > anyOf > diskUUID`

Type: `object`

Type: `object`

###  <a name="storage"></a>1.3.  Property `root > storage > anyOf > item 2`

Type: `object`

###  <a name="storage"></a>1.4.  Property `root > storage > anyOf > tmpfs`

Type: `object`

Type: `object`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100