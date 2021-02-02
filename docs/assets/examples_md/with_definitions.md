

# Schema Docs

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [billing_address](#billing_address)|No|object|No|No| No|-|
| [shipping_address](#shipping_address)|No|object|No|No| No|-|

##  <a name="billing_address"></a>1.  Property `root > billing_address`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_definitions.json', 'path_to_element': ['billing_address'], 'html_id': 'billing_address', 'breadcrumb_name': 'billing_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457460>, 'parent_key': 'billing_address', 'ref_path': '#/definitions/address', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ca0>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ca0>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#billing_address_street_address)|No|string|Yes|No| No|-|
| [city](#billing_address_city)|No|string|Yes|No| No|-|
| [state](#billing_address_state)|No|string|Yes|No| No|-|

###  <a name="billing_address_street_address"></a>1.1.  Property `root > billing_address > street_address`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_definitions.json', 'path_to_element': ['definitions', 'address', 'street_address'], 'html_id': 'billing_address_street_address', 'breadcrumb_name': 'street_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ca0>, 'parent_key': 'street_address', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224576a0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="billing_address_city"></a>1.2.  Property `root > billing_address > city`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_definitions.json', 'path_to_element': ['definitions', 'address', 'city'], 'html_id': 'billing_address_city', 'breadcrumb_name': 'city', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ca0>, 'parent_key': 'city', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ac0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="billing_address_state"></a>1.3.  Property `root > billing_address > state`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_definitions.json', 'path_to_element': ['definitions', 'address', 'state'], 'html_id': 'billing_address_state', 'breadcrumb_name': 'state', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ca0>, 'parent_key': 'state', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457820>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

##  <a name="shipping_address"></a>2.  Property `root > shipping_address`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_definitions.json', 'path_to_element': ['shipping_address'], 'html_id': 'shipping_address', 'breadcrumb_name': 'shipping_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457460>, 'parent_key': 'shipping_address', 'ref_path': '#/definitions/address', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457b80>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122457ca0>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

    Same definition as [billing_address](#billing_address)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:57 +0100