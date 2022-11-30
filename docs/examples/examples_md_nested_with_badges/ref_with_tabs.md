# Schema Docs

- [1. [Optional] Property root > objectA](#objectA)
  - [1.1. [Optional] Property root > objectA > signature](#objectA_signature)
    - [1.1.1. Property `root > objectA > signature > oneOf > item 0`](#objectA_signature_oneOf_i0)
      - [1.1.1.1. [Optional] Property root > objectA > signature > oneOf > item 0 > signers](#objectA_signature_oneOf_i0_signers)
    - [1.1.2. Property `root > objectA > signature > oneOf > item 1`](#objectA_signature_oneOf_i1)
      - [1.1.2.1. [Optional] Property root > objectA > signature > oneOf > item 1 > chain](#objectA_signature_oneOf_i1_chain)
    - [1.1.3. Property `root > objectA > signature > oneOf > Signature`](#objectA_signature_oneOf_i2)
- [2. [Optional] Property root > objectB](#objectB)
  - [2.1. [Optional] Property root > objectB > signature](#objectB_signature)

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="objectA"></a>1. [Optional] Property root > objectA</strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="objectA_signature"></a>1.1. [Optional] Property root > objectA > signature</strong>  

</summary>
<blockquote>

**Title:** Signature

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `combining`                                                                                                                       |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |
| **Defined in**            | #/definitions/signature                                                                                                           |

<blockquote>

| One of(Option)                           |
| ---------------------------------------- |
| [item 0](#objectA_signature_oneOf_i0)    |
| [item 1](#objectA_signature_oneOf_i1)    |
| [Signature](#objectA_signature_oneOf_i2) |

<blockquote>

#### <a name="objectA_signature_oneOf_i0"></a>1.1.1. Property `root > objectA > signature > oneOf > item 0`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

<details>
<summary><strong> <a name="objectA_signature_oneOf_i0_signers"></a>1.1.1.1. [Optional] Property root > objectA > signature > oneOf > item 0 > signers</strong>  

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

#### <a name="objectA_signature_oneOf_i1"></a>1.1.2. Property `root > objectA > signature > oneOf > item 1`

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

<details>
<summary><strong> <a name="objectA_signature_oneOf_i1_chain"></a>1.1.2.1. [Optional] Property root > objectA > signature > oneOf > item 1 > chain</strong>  

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

#### <a name="objectA_signature_oneOf_i2"></a>1.1.3. Property `root > objectA > signature > oneOf > Signature`

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
<summary><strong> <a name="objectB"></a>2. [Optional] Property root > objectB</strong>  

</summary>
<blockquote>

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

<details>
<summary><strong> <a name="objectB_signature"></a>2.1. [Optional] Property root > objectB > signature</strong>  

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