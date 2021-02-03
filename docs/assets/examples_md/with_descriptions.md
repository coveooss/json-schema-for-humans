

# Delivery Schema

Type: `object`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [shipping_address](#shipping_address)|No|object|No|No| No|Exact address|
| [billing_address](#billing_address)|No|object|No|No| No|Exact address|
| [delivery_info](#delivery_info)|No|object|No|No| No|Delivery info depending on the delivery type|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="shipping_address"></a>1.  Property `Delivery Schema > shipping_address`

Type: `object`

**Description:** Exact address
Defined in: #/definitions/address

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [street_address](#shipping_address_street_address)|No|string|Yes|No| No|-|
| [city](#shipping_address_city)|No|string|Yes|No| No|-|
| [state](#shipping_address_state)|No|string|Yes|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="shipping_address_street_address"></a>1.1.  Property `Delivery Schema > shipping_address > street_address`

Type: `string`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="shipping_address_city"></a>1.2.  Property `Delivery Schema > shipping_address > city`

Type: `string`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="shipping_address_state"></a>1.3.  Property `Delivery Schema > shipping_address > state`

Type: `string`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

##  <a name="billing_address"></a>2.  Property `Delivery Schema > billing_address`

Type: `object`

**Description:** Exact address
    Same definition as [shipping_address](#shipping_address)

##  <a name="delivery_info"></a>3.  Property `Delivery Schema > delivery_info`

Type: `object`

**Description:** Delivery info depending on the delivery type
Defined in: #/definitions/delivery_info

| Node | 
| ---- |
| [classic](#delivery_info_oneOf_i0) |
| [gift](#delivery_info_oneOf_i1) |
###  <a name="delivery_info"></a>3.1.  Property `Delivery Schema > delivery_info > oneOf > classic`

Type: `object`

Defined in: #/definitions/classic

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [price](#delivery_info_oneOf_i0_price)|No|number|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="delivery_info_oneOf_i0_price"></a>3.1.  Property `Delivery Schema > delivery_info > oneOf > item 0 > price`

Type: `number`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="delivery_info"></a>3.2.  Property `Delivery Schema > delivery_info > oneOf > gift`

Type: `object`

**Description:** The delivery is a gift, no prices displayed
Defined in: #/definitions/gift

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
| [with_wrap](#delivery_info_oneOf_i1_with_wrap)|No|boolean|No|No| No|-|
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

###  <a name="delivery_info_oneOf_i1_with_wrap"></a>3.1.  Property `Delivery Schema > delivery_info > oneOf > item 1 > with_wrap`

Type: `boolean`

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

| Property | Pattern | Type | Required | Deprecated | Additional | Description |
| -------- | ------- | ---- | -------- | ---------- | ---------- | ----------- |
  | additionalProperties | - | - | - | - |  [![made-with-Markdown](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") | - |

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2021-02-03 at 22:04:47 +0100