# Person

- [1. [Optional] Property Person > subType1](#subType1)
  - [1.1. [Optional] Property Person > subType1 > subProp1](#subType1_subProp1)
- [2. [Optional] Property Person > subType2](#subType2)
  - [2.1. [Optional] Property Person > subType2 > subProp2](#subType2_subProp2)
- [3. [Optional] Property Person > anInt](#anInt)
- [4. Property Person > additionalProperties](#additionalProperties)
  - [4.1. [Optional] Property Person > additionalProperties > propA](#additionalProperties_propA)

**Title:** Person

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><a href="#additionalProperties"><img src="https://img.shields.io/badge/Should-conform-blue" alt="Should-conform" /></a></td>
  </tr>
</table>

<details>
<summary>
<strong> <a name="subType1"></a>1. [Optional] Property Person > subType1</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Not%20allowed-red" alt="Not allowed" /></td>
  </tr>
</table>

**Description:** A sub type with additionalProperties false.

<details>
<summary>
<strong> <a name="subType1_subProp1"></a>1.1. [Optional] Property Person > subType1 > subProp1</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
</table>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="subType2"></a>2. [Optional] Property Person > subType2</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
</table>

**Description:** A sub type with additionalProperties true.

<details>
<summary>
<strong> <a name="subType2_subProp2"></a>2.1. [Optional] Property Person > subType2 > subProp2</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
</table>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>
<strong> <a name="anInt"></a>3. [Optional] Property Person > anInt</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>integer</code></td>
  </tr>
</table>

**Description:** This is an integer, it should not show additional properties. (issue #132)

</blockquote>
</details>

<details>
<summary>
<strong> <a name="additionalProperties"></a>4. Property Person > additionalProperties</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>object</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
</table>

**Description:** additionalProperties schema.

<details>
<summary>
<strong> <a name="additionalProperties_propA"></a>4.1. [Optional] Property Person > additionalProperties > propA</strong>  

</summary>
<blockquote>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
</table>

</blockquote>
</details>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)