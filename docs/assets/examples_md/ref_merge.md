# Test

- [1. Property `Test > aProperty`](#aProperty)
- [2. Property `Test > aDictPropertyARequired`](#aDictPropertyARequired)
  - [2.1. Property `Test > aDictPropertyARequired > a`](#aDictPropertyARequired_a)
  - [2.2. Property `Test > aDictPropertyARequired > b`](#aDictPropertyARequired_b)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [aProperty](#aProperty)|No|enum (of string)|No| No|This is the description from the definition|
|-  [aDictPropertyARequired](#aDictPropertyARequired)|No|object|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="aProperty"></a>1. Property `Test > aProperty`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `enum (of string)`
Default: `"Default from property"`

**Description:** This is the description from the definition

Defined in: #/definitions/aProperty

Must be one of:
* "value1"
* "value2"

## <a name="aDictPropertyARequired"></a>2. Property `Test > aDictPropertyARequired`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`
Default: `{"a": "a", "b": "b"}`

Defined in: #/definitions/aDictProperty

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|+  [a](#aDictPropertyARequired_a)|No|string|No| No|-|
|+  [b](#aDictPropertyARequired_b)|No|string|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="aDictPropertyARequired_a"></a>2.1. Property `Test > aDictPropertyARequired > a`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

### <a name="aDictPropertyARequired_b"></a>2.2. Property `Test > aDictPropertyARequired > b`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:29 +0100