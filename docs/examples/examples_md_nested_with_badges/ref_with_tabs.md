# Schema Docs

- [1. [Optional] Property root > objectA](#objectA-65637441)
  - [1.1. [Optional] Property root > objectA > signature](#objectA_signature-74757265)
    - [1.1.1. Property `root > objectA > signature > oneOf > item 0`](#objectA_signature_oneOf_i0-665f6930)
      - [1.1.1.1. [Optional] Property root > objectA > signature > oneOf > item 0 > signers](#objectA_signature_oneOf_i0_signers-6e657273)
    - [1.1.2. Property `root > objectA > signature > oneOf > item 1`](#objectA_signature_oneOf_i1-665f6931)
      - [1.1.2.1. [Optional] Property root > objectA > signature > oneOf > item 1 > chain](#objectA_signature_oneOf_i1_chain-6861696e)
    - [1.1.3. Property `root > objectA > signature > oneOf > Signature`](#objectA_signature_oneOf_i2-665f6932)
- [2. [Optional] Property root > objectB](#objectB-65637442)
  - [2.1. [Optional] Property root > objectB > signature](#objectB_signature-74757265)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="objectA-65637441"></a>1. [Optional] Property root > objectA</strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="objectA_signature-74757265"></a>1.1. [Optional] Property root > objectA > signature</strong>  

</summary>
<blockquote>

**Title:** Signature

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/signature                                                                                                           |

<blockquote>

| One of(Option)                                    |
| ------------------------------------------------- |
| [item 0](#objectA_signature_oneOf_i0-665f6930)    |
| [item 1](#objectA_signature_oneOf_i1-665f6931)    |
| [Signature](#objectA_signature_oneOf_i2-665f6932) |

<blockquote>

#### <a name="objectA_signature_oneOf_i0-665f6930"></a>1.1.1. Property `root > objectA > signature > oneOf > item 0`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

<details>
<summary><strong> <a name="objectA_signature_oneOf_i0_signers-6e657273"></a>1.1.1.1. [Optional] Property root > objectA > signature > oneOf > item 0 > signers</strong>  

</summary>
<blockquote>

**Title:** Signature

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** Unique top level property for Multiple Signatures. (multisignature)

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

</blockquote>
</details>

</blockquote>
<blockquote>

#### <a name="objectA_signature_oneOf_i1-665f6931"></a>1.1.2. Property `root > objectA > signature > oneOf > item 1`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

<details>
<summary><strong> <a name="objectA_signature_oneOf_i1_chain-6861696e"></a>1.1.2.1. [Optional] Property root > objectA > signature > oneOf > item 1 > chain</strong>  

</summary>
<blockquote>

**Title:** Signature

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** Unique top level property for Signature Chains. (signaturechain)

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

</blockquote>
</details>

</blockquote>
<blockquote>

#### <a name="objectA_signature_oneOf_i2-665f6932"></a>1.1.3. Property `root > objectA > signature > oneOf > Signature`

**Title:** Signature

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |
| **Same definition as**    | [Signature](#objectA_signature_oneOf_i0_signers_items)                                                   |

**Description:** Unique top level property for simple signatures. (signaturecore)

</blockquote>

</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><strong> <a name="objectB-65637442"></a>2. [Optional] Property root > objectB</strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="objectB_signature-74757265"></a>2.1. [Optional] Property root > objectB > signature</strong>  

</summary>
<blockquote>

**Title:** Signature

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Same definition as**    | [signature](#objectA_signature)                                                                                                   |

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)