# Delivery Schema

**Title:** Delivery Schema

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary>

## <a name="shipping_address"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `shipping_address`  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                               |
|                           |                                                                                                                     |

**Description:** Exact address

<details>
<summary>

### <a name="shipping_address_street_address"></a>![badge](https://img.shields.io/badge/Required-blue) Property `street_address`  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary>

### <a name="shipping_address_city"></a>![badge](https://img.shields.io/badge/Required-blue) Property `city`  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary>

### <a name="shipping_address_state"></a>![badge](https://img.shields.io/badge/Required-blue) Property `state`  

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
<summary>

## <a name="billing_address"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `billing_address`  

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
<summary>

## <a name="delivery_info"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `delivery_info`  

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

### <a name="delivery_info_oneOf_i0"></a>Property `classic`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/classic                                                                                               |
|                           |                                                                                                                     |

<details>
<summary>

#### <a name="delivery_info_oneOf_i0_price"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `price`  

</summary>
<blockquote>

| Type                      | `number`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

### <a name="delivery_info_oneOf_i1"></a>Property `gift`

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/gift                                                                                                  |
|                           |                                                                                                                     |

**Description:** The delivery is a gift, no prices displayed

<details>
<summary>

#### <a name="delivery_info_oneOf_i1_with_wrap"></a>![badge](https://img.shields.io/badge/Optional-yellow) Property `with_wrap`  

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
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date