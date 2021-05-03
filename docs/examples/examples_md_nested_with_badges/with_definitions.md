# Schema Docs

- [1. [Optional] Property root > billing_address](#billing_address)
  - [1.1. [Required] Property root > billing_address > street_address](#billing_address_street_address)
  - [1.2. [Required] Property root > billing_address > city](#billing_address_city)
  - [1.3. [Required] Property root > billing_address > state](#billing_address_state)
  - [1.4. [Optional] Property root > billing_address > futureProperty](#billing_address_futureProperty)
- [2. [Optional] Property root > shipping_address](#shipping_address)

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="billing_address"></a>1. [Optional] Property root > billing_address</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/address                                                                                               |
|                           |                                                                                                                     |

<details>
<summary><strong> <a name="billing_address_street_address"></a>1.1. [Required] Property root > billing_address > street_address</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary><strong> <a name="billing_address_city"></a>1.2. [Required] Property root > billing_address > city</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary><strong> <a name="billing_address_state"></a>1.3. [Required] Property root > billing_address > state</strong>  

</summary>
<blockquote>

| Type                      | `string`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

<details>
<summary><strong> <a name="billing_address_futureProperty"></a>1.4. [Optional] Property root > billing_address > futureProperty</strong>  

</summary>
<blockquote>

| Type                      | `null`                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
|                           |                                                                                                                     |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="shipping_address"></a>2. [Optional] Property root > shipping_address</strong>  

</summary>
<blockquote>

| Type                      | `object`                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Additional properties** | [![badge](https://img.shields.io/badge/Any+type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | `[billing_address](#billing_address)`                                                                               |
|                           |                                                                                                                     |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on date