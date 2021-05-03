# Delivery Schema

- [1. [Optional] Property Delivery Schema > shipping_address](#shipping_address)
  - [1.1. [Required] Property Delivery Schema > shipping_address > street_address](#shipping_address_street_address)
  - [1.2. [Required] Property Delivery Schema > shipping_address > city](#shipping_address_city)
  - [1.3. [Required] Property Delivery Schema > shipping_address > state](#shipping_address_state)
- [2. [Optional] Property Delivery Schema > billing_address](#billing_address)
- [3. [Optional] Property Delivery Schema > delivery_info](#delivery_info)
  - [3.1. Property `Delivery Schema > delivery_info > oneOf > classic`](#delivery_info_oneOf_i0)
    - [3.1.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 0 > price](#delivery_info_oneOf_i0_price)
  - [3.2. Property `Delivery Schema > delivery_info > oneOf > gift`](#delivery_info_oneOf_i1)
    - [3.2.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 1 > with_wrap](#delivery_info_oneOf_i1_with_wrap)

**Title:** Delivery Schema

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="shipping_address"></a>1. [Optional] Property Delivery Schema > shipping_address</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                               |
|                           |                                                                                                                     |

**Description:** Exact address

<details>
<summary><strong> <a name="shipping_address_street_address"></a>1.1. [Required] Property Delivery Schema > shipping_address > street_address</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary><strong> <a name="shipping_address_city"></a>1.2. [Required] Property Delivery Schema > shipping_address > city</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary><strong> <a name="shipping_address_state"></a>1.3. [Required] Property Delivery Schema > shipping_address > state</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="billing_address"></a>2. [Optional] Property Delivery Schema > billing_address</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[shipping_address](#shipping_address)`                                                                             |
|                           |                                                                                                                     |

**Description:** Exact address

</blockquote>
</details>

<details>
<summary><strong> <a name="delivery_info"></a>3. [Optional] Property Delivery Schema > delivery_info</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/delivery_info                                                                                         |
|                           |                                                                                                                     |

**Description:** Delivery info depending on the delivery type

<blockquote>

| One of(Option)                     |
| ---------------------------------- |
| [classic](#delivery_info_oneOf_i0) |
| [gift](#delivery_info_oneOf_i1)    |
|                                    |

<blockquote>

### <a name="delivery_info_oneOf_i0"></a>3.1. Property `Delivery Schema > delivery_info > oneOf > classic`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/classic                                                                                               |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="delivery_info_oneOf_i0_price"></a>3.1.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 0 > price</strong>  

</summary>
<blockquote>

| Type                      | `number`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

</blockquote>
<blockquote>

### <a name="delivery_info_oneOf_i1"></a>3.2. Property `Delivery Schema > delivery_info > oneOf > gift`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/gift                                                                                                  |
|                           |                                                                                                                     |

**Description:** The delivery is a gift, no prices displayed

<details>
<summary><strong> <a name="delivery_info_oneOf_i1_with_wrap"></a>3.2.1. [Optional] Property Delivery Schema > delivery_info > oneOf > item 1 > with_wrap</strong>  

</summary>
<blockquote>

| Type                      | `boolean`                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date