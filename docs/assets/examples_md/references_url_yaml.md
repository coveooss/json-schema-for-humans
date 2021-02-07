# Schema Docs

- [1. Property `root > address`](#address)
  - [1.1. Property `root > address > street_address`](#address_street_address)
  - [1.2. Property `root > address > city`](#address_city)
  - [1.3. Property `root > address > state`](#address_state)

Type: `object`

**Description:** Testing $ref with URL with YAML destination
| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [address](#address)|No|object|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="address"></a>1. Property `root > address`

Type: `object`

Defined in: https://raw.githubusercontent.com/coveooss/json-schema-for-humans/master/tests/cases/yaml.yaml#/definitions/address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#address_street_address)|No|string|Yes|No| No|-|
| [city](#address_city)|No|string|Yes|No| No|-|
| [state](#address_state)|No|string|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

### <a name="address_street_address"></a>1.1. Property `root > address > street_address`

Type: `string`

### <a name="address_city"></a>1.2. Property `root > address > city`

Type: `string`

### <a name="address_state"></a>1.3. Property `root > address > state`

Type: `string`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 02:06:48 +0100