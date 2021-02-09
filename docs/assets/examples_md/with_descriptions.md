# Delivery Schema

- [1. Property `Delivery Schema > shipping_address`](#shipping_address)
  - [1.1. Property `Delivery Schema > shipping_address > street_address`](#shipping_address_street_address)
  - [1.2. Property `Delivery Schema > shipping_address > city`](#shipping_address_city)
  - [1.3. Property `Delivery Schema > shipping_address > state`](#shipping_address_state)
- [2. Property `Delivery Schema > billing_address`](#billing_address)
- [3. Property `Delivery Schema > delivery_info`](#delivery_info)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0)
    - [3.1.1. Property `Delivery Schema > delivery_info > oneOf > item 0 > price`](#delivery_info_oneOf_i0_price)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1)
    - [3.2.1. Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`](#delivery_info_oneOf_i1_with_wrap)

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [shipping_address](#shipping_address)|No|Combination|No|No| No|Exact address|
| [billing_address](#billing_address)|No|Combination|No|No| No|Exact address|
| [delivery_info](#delivery_info)|No|Combination|No|No| No|Delivery info depending on the delivery type|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

## <a name="shipping_address"></a>1. Property `Delivery Schema > shipping_address`

Type: `object`

**Description:** <p>Exact address</p>

Defined in: #/definitions/address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#shipping_address_street_address)|No|Combination|Yes|No| No|-|
| [city](#shipping_address_city)|No|Combination|Yes|No| No|-|
| [state](#shipping_address_state)|No|Combination|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

### <a name="shipping_address_street_address"></a>1.1. Property `Delivery Schema > shipping_address > street_address`

Type: `string`

### <a name="shipping_address_city"></a>1.2. Property `Delivery Schema > shipping_address > city`

Type: `string`

### <a name="shipping_address_state"></a>1.3. Property `Delivery Schema > shipping_address > state`

Type: `string`

## <a name="billing_address"></a>2. Property `Delivery Schema > billing_address`

Type: `object`

**Description:** <p>Exact address</p>

Same definition as [shipping_address](#shipping_address)

## <a name="delivery_info"></a>3. Property `Delivery Schema > delivery_info`

Type: `object`

**Description:** <p>Delivery info depending on the delivery type</p>

Defined in: #/definitions/delivery_info

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

| One of(Option) | 
| ---- |
| [classic](#delivery_info_oneOf_i0) |
| [gift](#delivery_info_oneOf_i1) |
### <a name="delivery_info_oneOf_i0"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`
Type: `object`

Defined in: #/definitions/classic

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [price](#delivery_info_oneOf_i0_price)|No|Combination|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

#### <a name="delivery_info_oneOf_i0_price"></a>3.1.1. Property `Delivery Schema > delivery_info > oneOf > item 0 > price`

Type: `number`

### <a name="delivery_info_oneOf_i1"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`
Type: `object`

**Description:** <p>The delivery is a gift, no prices displayed</p>

Defined in: #/definitions/gift

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [with_wrap](#delivery_info_oneOf_i1_with_wrap)|No|Combination|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |        

#### <a name="delivery_info_oneOf_i1_with_wrap"></a>3.2.1. Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`

Type: `boolean`

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-09 at 19:16:34 +0100