

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subType1](#subType1)|No|object|No|No| No|A sub type with additionalProperties false.|
| [subType2](#subType2)|No|object|No|No| No|A sub type with additionalProperties true.|
| [additionalProperties](#additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Should-conform-blue)](#additionalProperties "Each additional property must conform to the following schema")|additionalProperties schema.|

##  <a name="subType1"></a>1.  Property `Person > subType1`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['subType1'], 'html_id': 'subType1', 'breadcrumb_name': 'subType1', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381070>, 'parent_key': 'subType1', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223817c0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381190>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {'subProp1': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381bb0>}, 'additional_properties': None, 'no_additional_properties': True, 'pattern_properties': {}}

Type: `object`

**Description:** A sub type with additionalProperties false.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subProp1](#subType1_subProp1)|No|number|No|No| No|-|
| additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="subType1_subProp1"></a>1.1.  Property `Person > subType1 > subProp1`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['subType1', 'subProp1'], 'html_id': 'subType1_subProp1', 'breadcrumb_name': 'subProp1', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381790>, 'parent_key': 'subProp1', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223814c0>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `number`

##  <a name="subType2"></a>2.  Property `Person > subType2`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['subType2'], 'html_id': 'subType2', 'breadcrumb_name': 'subType2', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381070>, 'parent_key': 'subType2', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb1223813d0>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381a90>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {'subProp2': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381fa0>}, 'additional_properties': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381640>, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** A sub type with additionalProperties true.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [subProp2](#subType2_subProp2)|No|number|No|No| No|-|
| [additionalProperties](#subType2_additionalProperties)|No|object|No|No|  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.")|-|

###  <a name="subType2_subProp2"></a>2.1.  Property `Person > subType2 > subProp2`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['subType2', 'subProp2'], 'html_id': 'subType2_subProp2', 'breadcrumb_name': 'subProp2', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381e20>, 'parent_key': 'subProp2', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381d30>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `number`

###  <a name="subType2_additionalProperties"></a>2.2.  Property `Person > subType2 > additionalProperties`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['subType2', 'additionalProperties'], 'html_id': 'subType2_additionalProperties', 'breadcrumb_name': 'additionalProperties', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381e20>, 'parent_key': 'additionalProperties', 'ref_path': '', 'literal': True, 'keywords': {}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

##  <a name="additionalProperties"></a>3.  Property `Person > additionalProperties`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['additionalProperties'], 'html_id': 'additionalProperties', 'breadcrumb_name': 'additionalProperties', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381070>, 'parent_key': 'additionalProperties', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381a30>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381f10>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {'propA': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381670>}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** additionalProperties schema.

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [propA](#additionalProperties_propA)|No|number|No|No| No|-|

###  <a name="additionalProperties_propA"></a>3.1.  Property `Person > additionalProperties > propA`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/additional_properties.json', 'path_to_element': ['additionalProperties', 'propA'], 'html_id': 'additionalProperties_propA', 'breadcrumb_name': 'propA', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381820>, 'parent_key': 'propA', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122381490>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `number`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:01:00 +0100