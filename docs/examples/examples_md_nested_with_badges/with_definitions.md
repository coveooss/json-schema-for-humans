# Schema Docs

- [1. [Optional] Propertyroot > billing_address](#billing_address)
  - [1.1. [Required] Propertyroot > billing_address > street_address](#billing_address_street_address)
  - [1.2. [Required] Propertyroot > billing_address > city](#billing_address_city)
  - [1.3. [Required] Propertyroot > billing_address > state](#billing_address_state)
  - [1.4. [Optional] Propertyroot > billing_address > futureProperty](#billing_address_futureProperty)
- [2. [Optional] Propertyroot > shipping_address](#shipping_address)

|          |          |
| -------- | -------- |
| **Type** | `object` |

<details>
<summary>
<strong> <a name="billing_address"></a>1. [Optional] Propertyroot > billing_address</strong>  

</summary>
<blockquote>

|                |                       |
| -------------- | --------------------- |
| **Type**       | `object`              |
| **Defined in** | #/definitions/address |

<details>
<summary>
<strong> <a name="billing_address_street_address"></a>1.1. [Required] Propertyroot > billing_address > street_address</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address_city"></a>1.2. [Required] Propertyroot > billing_address > city</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address_state"></a>1.3. [Required] Propertyroot > billing_address > state</strong>  

</summary>
<blockquote>

|          |          |
| -------- | -------- |
| **Type** | `string` |

</blockquote>
</details>

<details>
<summary>
<strong> <a name="billing_address_futureProperty"></a>1.4. [Optional] Propertyroot > billing_address > futureProperty</strong>  

</summary>
<blockquote>

|          |        |
| -------- | ------ |
| **Type** | `null` |

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="shipping_address"></a>2. [Optional] Propertyroot > shipping_address</strong>  

</summary>
<blockquote>

|                        |                                     |
| ---------------------- | ----------------------------------- |
| **Type**               | `object`                            |
| **Same definition as** | [billing_address](#billing_address) |

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)