

# Schema Docs

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [outer](#outer)|No|object|Yes|No| No|We should see this|
| [outer2](#outer2)|No|object|No|No| No|We should see this too|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

##  <a name="outer"></a>1.  Property `root > outer`

Type: `object`

**Description:** We should see this
Defined in: #/definitions/inner schema

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [inner](#outer_inner)|No|string|Yes|No| No|inner description|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |

###  <a name="outer_inner"></a>1.1.  Property `root > outer > inner`

Type: `string`

**Description:** inner description

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="outer2"></a>2.  Property `root > outer2`

Type: `object`

**Description:** We should see this too
    Same definition as [outer](#outer)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-03 at 22:04:48 +0100