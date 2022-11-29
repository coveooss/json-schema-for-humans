# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > billing_address`](#billing_address-72657373)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > billing_address > street_address`](#billing_address_street_address-72657373)
  - [1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `root > billing_address > city`](#billing_address_city-63697479)
  - [1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `root > billing_address > state`](#billing_address_state-74617465)
  - [1.4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > billing_address > futureProperty`](#billing_address_futureProperty-65727479)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > shipping_address`](#shipping_address-72657373)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                          | Pattern | Type   | Deprecated | Definition                                            | Title/Description |
| ------------------------------------------------- | ------- | ------ | ---------- | ----------------------------------------------------- | ----------------- |
| - [billing_address](#billing_address-72657373 )   | No      | object | No         | In #/definitions/address                              | -                 |
| - [shipping_address](#shipping_address-72657373 ) | No      | object | No         | Same as [billing_address](#billing_address-72657373 ) | -                 |

## <a name="billing_address-72657373"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > billing_address`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                                             |

| Property                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#billing_address_street_address-72657373 ) | No      | string | No         | -          | -                 |
| + [city](#billing_address_city-63697479 )                     | No      | string | No         | -          | -                 |
| + [state](#billing_address_state-74617465 )                   | No      | string | No         | -          | -                 |
| - [futureProperty](#billing_address_futureProperty-65727479 ) | No      | null   | No         | -          | -                 |

### <a name="billing_address_street_address-72657373"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > billing_address > street_address`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="billing_address_city-63697479"></a>1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `root > billing_address > city`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="billing_address_state-74617465"></a>1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `root > billing_address > state`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="billing_address_futureProperty-65727479"></a>1.4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > billing_address > futureProperty`

|          |        |
| -------- | ------ |
| **Type** | `null` |

## <a name="shipping_address-72657373"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > shipping_address`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [billing_address](#billing_address)                                                                                               |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
