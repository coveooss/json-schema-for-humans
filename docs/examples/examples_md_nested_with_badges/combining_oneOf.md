# Schema Docs

- [1. [Required] Property root > storage](#storage)
  - [1.1. Property `root > storage > oneOf > diskDevice`](#storage_oneOf_i0)
  - [1.2. Property `root > storage > oneOf > diskUUID`](#storage_oneOf_i1)
  - [1.3. Property `root > storage > oneOf > nfs`](#storage_oneOf_i2)
  - [1.4. Property `root > storage > oneOf > tmpfs`](#storage_oneOf_i3)

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

<p><strong>Description:</strong> JSON Schema for an fstab entry</p>

<details>
<summary>
<strong> <a name="storage"></a>1. [Required] Property root > storage</strong>  

</summary>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>combining</code></td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td><img src="https://img.shields.io/badge/Any%20type-allowed-green" alt="Any type: allowed" /></td>
  </tr>
</table>

<details>
<summary>One of(Option)</summary>

<table>
  <tr>
    <th>One of(Option)</th>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i0">diskDevice</a></td>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i1">diskUUID</a></td>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i2">nfs</a></td>
  </tr>
  <tr>
    <td><a href="#storage_oneOf_i3">tmpfs</a></td>
  </tr>
</table>

<details>
<summary>
### <a name="storage_oneOf_i0"></a>1.1. Property `root > storage > oneOf > diskDevice`</summary>

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/diskDevice</h1></td>
  </tr>
</table>

</details>
<details>
<summary>
### <a name="storage_oneOf_i1"></a>1.2. Property `root > storage > oneOf > diskUUID`</summary>

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/diskUUID</h1></td>
  </tr>
</table>

</details>
<details>
<summary>
### <a name="storage_oneOf_i2"></a>1.3. Property `root > storage > oneOf > nfs`</summary>

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/nfs</h1></td>
  </tr>
</table>

</details>
<details>
<summary>
### <a name="storage_oneOf_i3"></a>1.4. Property `root > storage > oneOf > tmpfs`</summary>

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/tmpfs</h1></td>
  </tr>
</table>

</details>

</details>

</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)