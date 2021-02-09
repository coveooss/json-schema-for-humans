# Schema Docs

- [1. Property `root > outer`](#outer)
  - [1.1. Property `root > outer > inner`](#outer_inner)
- [2. Property `root > outer2`](#outer2)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [outer](#outer)|No|Combination|Yes|No| No|We should see this|
| [outer2](#outer2)|No|Combination|No|No| No|We should see this too|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

## <a name="outer"></a>1. Property `root > outer`

Type: `object`

**Description:** <p>We should see this</p>

Defined in: #/definitions/inner schema

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [inner](#outer_inner)|No|Combination|Yes|No| No|inner description|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

### <a name="outer_inner"></a>1.1. Property `root > outer > inner`

Type: `string`

**Description:** <p>inner description</p>

## <a name="outer2"></a>2. Property `root > outer2`

Type: `object`

**Description:** <p>We should see this too</p>

Same definition as [outer](#outer)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:34 +0100