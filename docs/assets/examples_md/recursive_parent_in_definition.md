

# Person

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships)|No|object|No|No| No|Relationships between this person and others|

##  <a name="relationships"></a>1.  Property `Person > relationships`

      {'depth': 1, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_parent_in_definition.json', 'path_to_element': ['relationships'], 'html_id': 'relationships', 'breadcrumb_name': 'relationships', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488790>, 'parent_key': 'relationships', 'ref_path': '#/definitions/person/properties/relationships', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488280>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488280>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Relationships between this person and others

Type: `object`

**Description:** Relationships between this person and others

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother)|No|object|No|No| No|A human being|

###  <a name="relationships_mother"></a>1.1.  Property `Person > relationships > mother`

      {'depth': 2, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_parent_in_definition.json', 'path_to_element': ['definitions', 'person', 'properties', 'relationships', 'mother'], 'html_id': 'relationships_mother', 'breadcrumb_name': 'mother', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488280>, 'parent_key': 'mother', 'ref_path': '#/definitions/person', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488c10>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488c10>, 'is_displayed': True, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** A human being

Type: `object`

**Description:** A human being

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [relationships](#relationships_mother_relationships)|No|object|No|No| No|Relationships between this person and others|

####  <a name="relationships_mother_relationships"></a>1.1.1.  Property `Person > relationships > mother > relationships`

      {'depth': 3, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_parent_in_definition.json', 'path_to_element': ['definitions', 'person', 'relationships'], 'html_id': 'relationships_mother_relationships', 'breadcrumb_name': 'relationships', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488c10>, 'parent_key': 'relationships', 'ref_path': '', 'literal': None, 'keywords': {'type': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488310>, 'description': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488040>}, 'array_items': [], 'links_to': None, 'refers_to': None, 'is_displayed': True, '_refers_to_merged': None, 'properties': {'mother': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488b50>}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** Relationships between this person and others

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [mother](#relationships_mother_relationships_mother)|No|object|No|No| No|A human being|

#####  <a name="relationships_mother_relationships_mother"></a>1.1.1.1.  Property `Person > relationships > mother > relationships > mother`

      {'depth': 4, 'file': '/home/vagrant/projects/json-schema-for-humans/tests/cases/recursive_parent_in_definition.json', 'path_to_element': ['definitions', 'person', 'relationships', 'mother'], 'html_id': 'relationships_mother_relationships_mother', 'breadcrumb_name': 'mother', 'parent': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488220>, 'parent_key': 'mother', 'ref_path': '#/definitions/person', 'literal': None, 'keywords': {}, 'array_items': [], 'links_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488520>, 'refers_to': <json_schema_for_humans.generate.SchemaNode object at 0x7fb122488c10>, 'is_displayed': False, '_refers_to_merged': None, 'properties': {}, 'additional_properties': None, 'no_additional_properties': False, 'pattern_properties': {}}

Type: `object`

**Description:** A human being
    Same definition as [mother](#relationships_mother)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-02 at 22:00:59 +0100