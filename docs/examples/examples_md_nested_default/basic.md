# Person

- [1. [Optional] Property Person > firstName](#firstName)
- [2. [Optional] Property Person > lastName](#lastName)
- [3. [Optional] Property Person > age](#age)
- [4. [Optional] Property Person > driverLicenseId](#driverLicenseId)
  - [4.1. Property `Person > driverLicenseId > allOf > no driver licence`](#driverLicenseId_allOf_i0)
  - [4.2. Property `Person > driverLicenseId > allOf > driver licence id`](#driverLicenseId_allOf_i1)

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
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

<details>
<summary>
<strong> <a name="firstName"></a>1. [Optional] Property Person > firstName</strong>  

</summary>
<blockquote>

**Title:** Person

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** The person's first name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="lastName"></a>2. [Optional] Property Person > lastName</strong>  

</summary>
<blockquote>

**Title:** Person

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** The person's last name.

</blockquote>
</details>

<details>
<summary>
<strong> <a name="age"></a>3. [Optional] Property Person > age</strong>  

</summary>
<blockquote>

**Title:** Person

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>integer</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

**Description:** Age in years which must be equal to or greater than zero.

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

</blockquote>
</details>

<details>
<summary>
<strong> <a name="driverLicenseId"></a>4. [Optional] Property Person > driverLicenseId</strong>  

</summary>
<blockquote>

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
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
  <tr>
    <td><strong>Additional properties</strong></td>
    <td>Any type allowed</td>
  </tr>
</table>

<blockquote>

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

<blockquote>

### <a name="driverLicenseId_allOf_i0"></a>4.1. Property `Person > driverLicenseId > allOf > no driver licence`

**Title:** no driver licence

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>null</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

</blockquote>
<blockquote>

### <a name="driverLicenseId_allOf_i1"></a>4.2. Property `Person > driverLicenseId > allOf > driver licence id`

**Title:** driver licence id

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>string</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

</blockquote>

</blockquote>

</blockquote>
</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)