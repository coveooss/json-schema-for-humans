

# Schema Docs

Type: `object`

**Description:** Testing $ref with URL with YAML destination

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [address](#address)|No|object|No|No| No|-|

##  <a name="address"></a>1.  Property `root > address`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/references_url_yaml.json', 'path_to_element': ['address'], 'html_id': 'address', 'breadcrumb_name': 'address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb12248ebb0>, 'parent_key': 'address', 'ref_path': 'https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/yaml.yaml#/definitions/address', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460b80>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460b80>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#address_street_address)|No|string|Yes|No| No|-|
| [city](#address_city)|No|string|Yes|No| No|-|
| [state](#address_state)|No|string|Yes|No| No|-|

###  <a name="address_street_address"></a>1.1.  Property `root > address > street_address`

      {'depth': 2, 'file': 'https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/yaml.yaml', 'path_to_element': ['definitions', 'address', 'street_address'], 'html_id': 'address_street_address', 'breadcrumb_name': 'street_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460b80>, 'parent_key': 'street_address', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460970>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="address_city"></a>1.2.  Property `root > address > city`

      {'depth': 2, 'file': 'https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/yaml.yaml', 'path_to_element': ['definitions', 'address', 'city'], 'html_id': 'address_city', 'breadcrumb_name': 'city', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460b80>, 'parent_key': 'city', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460790>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="address_state"></a>1.3.  Property `root > address > state`

      {'depth': 2, 'file': 'https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/yaml.yaml', 'path_to_element': ['definitions', 'address', 'state'], 'html_id': 'address_state', 'breadcrumb_name': 'state', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460b80>, 'parent_key': 'state', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122460d90>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:57 +0100