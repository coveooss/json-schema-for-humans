

# Schema Docs

Type: `object`

**Description:** JSON Schema for an fstab entry

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [storage](#storage)|No|object|Yes|No| No|-|

##  <a name="storage"></a>1.  Property `root > storage`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/combining_oneOf.json', 'path_to_element': ['storage'], 'html_id': 'storage', 'breadcrumb_name': 'storage', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460820>, 'parent_key': 'storage', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457fd0>, 'oneOf': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457100>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

| Node | 
| ---- |
| [diskDevice](#storage_oneOf_i0) |
| [diskUUID](#storage_oneOf_i1) |
| [nfs](#storage_oneOf_i2) |
| [tmpfs](#storage_oneOf_i3) |
###  <a name="storage"></a>1.1.  Property `root > storage > oneOf > diskDevice`

Type: `object`

Type: `object`

###  <a name="storage"></a>1.2.  Property `root > storage > oneOf > diskUUID`

Type: `object`

Type: `object`

###  <a name="storage"></a>1.3.  Property `root > storage > oneOf > nfs`

Type: `object`

Type: `object`

###  <a name="storage"></a>1.4.  Property `root > storage > oneOf > tmpfs`

Type: `object`

Type: `object`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:01:00 +0100