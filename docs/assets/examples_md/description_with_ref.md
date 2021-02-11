# Schema Docs

- [1. Property `root > outer`](#outer)
  - [1.1. Property `root > outer > inner`](#outer_inner)
- [2. Property `root > outer2`](#outer2)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|+  [outer](#outer)|No|object|No| No|We should see this|
|-  [outer2](#outer2)|No|object|No| No|We should see this too|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

## <a name="outer"></a>1. Property `root > outer`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `object`

**Description:** We should see this

Defined in: #/definitions/inner schema

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|+  [inner](#outer_inner)|No|string|No| No|inner description|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") | - |        

### <a name="outer_inner"></a>1.1. Property `root > outer > inner`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

**Description:** inner description

## <a name="outer2"></a>2. Property `root > outer2`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

**Description:** We should see this too

Same definition as [outer](#outer)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:28 +0100