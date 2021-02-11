# Schema Docs

- [1. Property `root > address`](#address)
  - [1.1. Property `root > address > street_address`](#address_street_address)
  - [1.2. Property `root > address > city`](#address_city)
  - [1.3. Property `root > address > state`](#address_state)

Type: `object`

**Description:** Testing $ref with URL with YAML destination

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [address](#address)|No|object|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="address"></a>1. Property `root > address`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

Defined in: https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/yaml.yaml#/definitions/address

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|+  [street_address](#address_street_address)|No|string|No| No|-|
|+  [city](#address_city)|No|string|No| No|-|
|+  [state](#address_state)|No|string|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="address_street_address"></a>1.1. Property `root > address > street_address`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

### <a name="address_city"></a>1.2. Property `root > address > city`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

### <a name="address_state"></a>1.3. Property `root > address > state`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:26 +0100