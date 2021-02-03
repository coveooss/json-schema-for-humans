

# Schema Docs

| Node | 
| ---- |
| [All of(Requirement) 1](#allOf_i0) |
| [All of(Requirement) 2](#allOf_i1) |
| [All of(Requirement) 3](#allOf_i2) |
##  1.  Property `root > allOf > item 0`

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i0_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i0_if_country)|No|const|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="allOf_i0_if_country"></a>1.  Property `root > allOf > item 0 > if > country`

Type: `const`

            Specific value: `"United States of America"`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

**[Then](#tab-pane_allOf_i0_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i0_then_postal_code)|No|object|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="allOf_i0_then_postal_code"></a>1.  Property `root > allOf > item 0 > then > postal_code`

Type: `object`

            Must match regular expression: `[0-9]{5}(-[0-9]{4})?` [Test](https://regex101.com/?regex=[0-9]{5}(-[0-9]{4})?)

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |
##  2.  Property `root > allOf > item 1`

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i1_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i1_if_country)|No|const|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="allOf_i1_if_country"></a>1.  Property `root > allOf > item 1 > if > country`

Type: `const`

            Specific value: `"Canada"`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

**[Then](#tab-pane_allOf_i1_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i1_then_postal_code)|No|object|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="allOf_i1_then_postal_code"></a>1.  Property `root > allOf > item 1 > then > postal_code`

Type: `object`

            Must match regular expression: `[A-Z][0-9][A-Z] [0-9][A-Z][0-9]` [Test](https://regex101.com/?regex=[A-Z][0-9][A-Z] [0-9][A-Z][0-9])

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |
##  3.  Property `root > allOf > item 2`

Type: `object`

## Conditional Subschema
If the conditions in the "If" tab are respected, then the conditions in the "Then" tab should be respected.
Otherwise, the conditions in the "Else" tab should be respected.
**[If](#tab-pane_allOf_i2_if"):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [country](#allOf_i2_if_country)|No|const|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="allOf_i2_if_country"></a>1.  Property `root > allOf > item 2 > if > country`

Type: `const`

            Specific value: `"Netherlands"`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

**[Then](#tab-pane_allOf_i2_then):**

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [postal_code](#allOf_i2_then_postal_code)|No|object|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="allOf_i2_then_postal_code"></a>1.  Property `root > allOf > item 2 > then > postal_code`

Type: `object`

            Must match regular expression: `[0-9]{4} [A-Z]{2}` [Test](https://regex101.com/?regex=[0-9]{4} [A-Z]{2})

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#street_address)|No|string|No|No| No|-|
| [country](#country)|No|enum (of string)|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="street_address"></a>1.  Property `root > street_address`

Type: `string`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="country"></a>2.  Property `root > country`

Type: `enum (of string)`

            Must be one of:
                * "United States of America"
                * "Canada"
                * "Netherlands"

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-03 at 22:04:48 +0100