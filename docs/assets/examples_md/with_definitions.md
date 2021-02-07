# Schema Docs

- [1. Property `root > billing_address`](#billing_address)
  - [1.1. Property `root > billing_address > street_address`](#billing_address_street_address)
  - [1.2. Property `root > billing_address > city`](#billing_address_city)
  - [1.3. Property `root > billing_address > state`](#billing_address_state)
- [2. Property `root > shipping_address`](#shipping_address)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [billing_address](#billing_address)|No|object|No|No| No|-|
| [shipping_address](#shipping_address)|No|object|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

## <a name="billing_address"></a>1. Property `root > billing_address`

Type: `object`

Defined in: #/definitions/address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#billing_address_street_address)|No|string|Yes|No| No|-|
| [city](#billing_address_city)|No|string|Yes|No| No|-|
| [state](#billing_address_state)|No|string|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

### <a name="billing_address_street_address"></a>1.1. Property `root > billing_address > street_address`

Type: `string`

### <a name="billing_address_city"></a>1.2. Property `root > billing_address > city`

Type: `string`

### <a name="billing_address_state"></a>1.3. Property `root > billing_address > state`

Type: `string`

## Property `root > shipping_address`

Type: `object`

Same definition as [billing_address](#billing_address)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-07 at 02:06:48 +0100