# Delivery Schema

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > shipping_address`](#shipping_address-72657373)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > street_address`](#shipping_address_street_address-72657373)
  - [1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > city`](#shipping_address_city-63697479)
  - [1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > state`](#shipping_address_state-74617465)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > billing_address`](#billing_address-72657373)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > delivery_info`](#delivery_info-696e666f)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0-665f6930)
    - [3.1.1. Property `Delivery Schema > delivery_info > oneOf > item 0 > price`](#delivery_info_oneOf_i0_price-72696365)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1-665f6931)
    - [3.2.1. Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`](#delivery_info_oneOf_i1_with_wrap-77726170)

**Title:** Delivery Schema

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                          | Pattern | Type   | Deprecated | Definition                                              | Title/Description                            |
| ------------------------------------------------- | ------- | ------ | ---------- | ------------------------------------------------------- | -------------------------------------------- |
| - [shipping_address](#shipping_address-72657373 ) | No      | object | No         | In #/definitions/address                                | Exact address                                |
| - [billing_address](#billing_address-72657373 )   | No      | object | No         | Same as [shipping_address](#shipping_address-72657373 ) | Exact address                                |
| - [delivery_info](#delivery_info-696e666f )       | No      | object | No         | In #/definitions/delivery_info                          | Delivery info depending on the delivery type |

## <a name="shipping_address-72657373"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > shipping_address`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                                             |

**Description:** Exact address

| Property                                                       | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [street_address](#shipping_address_street_address-72657373 ) | No      | string | No         | -          | -                 |
| + [city](#shipping_address_city-63697479 )                     | No      | string | No         | -          | -                 |
| + [state](#shipping_address_state-74617465 )                   | No      | string | No         | -          | -                 |

### <a name="shipping_address_street_address-72657373"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > street_address`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="shipping_address_city-63697479"></a>1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > city`

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="shipping_address_state-74617465"></a>1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `Delivery Schema > shipping_address > state`

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="billing_address-72657373"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > billing_address`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [shipping_address](#shipping_address)                                                                                             |

**Description:** Exact address

## <a name="delivery_info-696e666f"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Delivery Schema > delivery_info`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/delivery_info                                                                                                       |

**Description:** Delivery info depending on the delivery type

| One of(Option)                              |
| ------------------------------------------- |
| [classic](#delivery_info_oneOf_i0-665f6930) |
| [gift](#delivery_info_oneOf_i1-665f6931)    |

### <a name="delivery_info_oneOf_i0-665f6930"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/classic                                                                                                             |

| Property                                           | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [price](#delivery_info_oneOf_i0_price-72696365 ) | No      | number | No         | -          | -                 |

#### <a name="delivery_info_oneOf_i0_price-72696365"></a>3.1.1. Property `Delivery Schema > delivery_info > oneOf > item 0 > price`

|          |          |
| -------- | -------- |
| **Type** | `number` |

### <a name="delivery_info_oneOf_i1-665f6931"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/gift                                                                                                                |

**Description:** The delivery is a gift, no prices displayed

| Property                                                   | Pattern | Type    | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------- |
| - [with_wrap](#delivery_info_oneOf_i1_with_wrap-77726170 ) | No      | boolean | No         | -          | -                 |

#### <a name="delivery_info_oneOf_i1_with_wrap-77726170"></a>3.2.1. Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
