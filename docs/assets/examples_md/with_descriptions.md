

# Delivery Schema

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [shipping_address](#shipping_address)|No|object|No|No| No|Exact address|
| [billing_address](#billing_address)|No|object|No|No| No|Exact address|
| [delivery_info](#delivery_info)|No|object|No|No| No|Delivery info depending on the delivery type|

##  <a name="shipping_address"></a>1.  Property `Delivery Schema > shipping_address`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['shipping_address'], 'html_id': 'shipping_address', 'breadcrumb_name': 'shipping_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223816d0>, 'parent_key': 'shipping_address', 'ref_path': '#/definitions/address', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Exact address

Type: `object`

**Description:** Exact address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#shipping_address_street_address)|No|string|Yes|No| No|-|
| [city](#shipping_address_city)|No|string|Yes|No| No|-|
| [state](#shipping_address_state)|No|string|Yes|No| No|-|

###  <a name="shipping_address_street_address"></a>1.1.  Property `Delivery Schema > shipping_address > street_address`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['definitions', 'address', 'street_address'], 'html_id': 'shipping_address_street_address', 'breadcrumb_name': 'street_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>, 'parent_key': 'street_address', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381130>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="shipping_address_city"></a>1.2.  Property `Delivery Schema > shipping_address > city`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['definitions', 'address', 'city'], 'html_id': 'shipping_address_city', 'breadcrumb_name': 'city', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>, 'parent_key': 'city', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381e80>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

###  <a name="shipping_address_state"></a>1.3.  Property `Delivery Schema > shipping_address > state`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['definitions', 'address', 'state'], 'html_id': 'shipping_address_state', 'breadcrumb_name': 'state', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>, 'parent_key': 'state', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223817c0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `string`

##  <a name="billing_address"></a>2.  Property `Delivery Schema > billing_address`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['billing_address'], 'html_id': 'billing_address', 'breadcrumb_name': 'billing_address', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223816d0>, 'parent_key': 'billing_address', 'ref_path': '#/definitions/address', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381250>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Exact address
    Same definition as [shipping_address](#shipping_address)

##  <a name="delivery_info"></a>3.  Property `Delivery Schema > delivery_info`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['delivery_info'], 'html_id': 'delivery_info', 'breadcrumb_name': 'delivery_info', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223816d0>, 'parent_key': 'delivery_info', 'ref_path': '#/definitions/delivery_info', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122472970>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122472970>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Delivery info depending on the delivery type

**Description:** Delivery info depending on the delivery type
| Node | 
| ---- |
| [classic](#delivery_info_oneOf_i0) |
| [gift](#delivery_info_oneOf_i1) |
###  <a name="delivery_info"></a>3.1.  Property `Delivery Schema > delivery_info > oneOf > classic`

Type: `object`

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [price](#delivery_info_oneOf_i0_price)|No|number|No|No| No|-|

###  <a name="delivery_info_oneOf_i0_price"></a>3.1.  Property `Delivery Schema > delivery_info > oneOf > item 0 > price`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['definitions', 'classic', 'price'], 'html_id': 'delivery_info_oneOf_i0_price', 'breadcrumb_name': 'price', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224724c0>, 'parent_key': 'price', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1224729d0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `number`

###  <a name="delivery_info"></a>3.2.  Property `Delivery Schema > delivery_info > oneOf > gift`

Type: `object`

**Description:** The delivery is a gift, no prices displayed

Type: `object`

**Description:** The delivery is a gift, no prices displayed

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [with_wrap](#delivery_info_oneOf_i1_with_wrap)|No|boolean|No|No| No|-|

###  <a name="delivery_info_oneOf_i1_with_wrap"></a>3.1.  Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/with_descriptions.json', 'path_to_element': ['definitions', 'gift', 'with_wrap'], 'html_id': 'delivery_info_oneOf_i1_with_wrap', 'breadcrumb_name': 'with_wrap', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122472340>, 'parent_key': 'with_wrap', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122472400>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `boolean`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:58 +0100