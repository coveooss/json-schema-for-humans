# Schema Docs

- [1. Property `root > billing_address`](#billing_address)
  - [1.1. Property `root > billing_address > street_address`](#billing_address_street_address)
  - [1.2. Property `root > billing_address > city`](#billing_address_city)
  - [1.3. Property `root > billing_address > state`](#billing_address_state)
  - [1.4. Property `root > billing_address > futureProperty`](#billing_address_futureProperty)
- [2. Property `root > shipping_address`](#shipping_address)

Type: `object`

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|-  [billing_address](#billing_address)|No|object|No| No|-|
|-  [shipping_address](#shipping_address)|No|object|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="billing_address"></a>1. Property `root > billing_address`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

Defined in: #/definitions/address

| Property | Pattern | Type | Deprecated | Additional | Description |
| -------- | ------- | ---- | ---------- | ---------- | ----------- |
|+  [street_address](#billing_address_street_address)|No|string|No| No|-|
|+  [city](#billing_address_city)|No|string|No| No|-|
|+  [state](#billing_address_state)|No|string|No| No|-|
|-  [futureProperty](#billing_address_futureProperty)|No|null|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="billing_address_street_address"></a>1.1. Property `root > billing_address > street_address`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

### <a name="billing_address_city"></a>1.2. Property `root > billing_address > city`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

### <a name="billing_address_state"></a>1.3. Property `root > billing_address > state`

![made-with-Markdown](https://img.shields.io/badge/Required-blue)
Type: `string`

### <a name="billing_address_futureProperty"></a>1.4. Property `root > billing_address > futureProperty`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `null`

## <a name="shipping_address"></a>2. Property `root > shipping_address`

![made-with-Markdown](https://img.shields.io/badge/Optional-yellow)
Type: `object`

Same definition as [billing_address](#billing_address)

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-11 at 21:24:27 +0100