# Person

- [1. [Optional] Property Person > firstName](#firstName)
- [2. [Optional] Property Person > lastName](#lastName)
- [3. [Optional] Property Person > age](#age)
- [4. [Optional] Property Person > driverLicenseId](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

<p><strong>Title:</strong> Person</p>

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

<details>
<summary>
<strong> <a name="firstName"></a>1. [Optional] Property Person > firstName</strong>  

</summary>

<p><strong>Title:</strong> Person</p>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
</table>

<p><strong>Description:</strong> The person's first name.</p>

</details>

<details>
<summary>
<strong> <a name="lastName"></a>2. [Optional] Property Person > lastName</strong>  

</summary>

<p><strong>Title:</strong> Person</p>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
</table>

<p><strong>Description:</strong> The person's last name.</p>

</details>

<details>
<summary>
<strong> <a name="age"></a>3. [Optional] Property Person > age</strong>  

</summary>

<p><strong>Title:</strong> Person</p>

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

<p><strong>Description:</strong> Age in years which must be equal to or greater than zero.</p>

<table>
  <tr>
    <th>Restrictions</th>
    <th> </th>
  </tr>
  <tr>
    <td><strong>Minimum</strong></td>
    <td>&ge; 0</td>
  </tr>
</table>

</details>

<details>
<summary>
<strong> <a name="driverLicenseId"></a>4. [Optional] Property Person > driverLicenseId</strong>  

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
<summary>All of(Requirement)</summary>

<table>
  <tr>
    <th>All of(Requirement)</th>
  </tr>
  <tr>
    <td><a href="#driverLicenseId_allOf_i0">no driver licence</a></td>
  </tr>
  <tr>
    <td><a href="#driverLicenseId_allOf_i1">driver licence id</a></td>
  </tr>
</table>

<details>
<summary>
### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`</summary>

<p><strong>Title:</strong> no driver licence</p>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>null</code></td>
  </tr>
</table>

</details>
<details>
<summary>
### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`</summary>

<p><strong>Title:</strong> driver licence id</p>

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
</table>

</details>

</details>

</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)