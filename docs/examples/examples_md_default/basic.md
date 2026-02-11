# Person

- [1. Property `Person > firstName`](#firstName)
- [2. Property `Person > lastName`](#lastName)
- [3. Property `Person > age`](#age)
- [4. Property `Person > driverLicenseId`](#driverLicenseId)
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

<table>
  <tr>
    <th>Property</th>
    <th>Pattern</th>
    <th>Type</th>
    <th>Deprecated</th>
    <th>Definition</th>
    <th>Title/Description</th>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">firstName</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Person</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">lastName</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>Person</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">age</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>Person</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">driverLicenseId</a></li>
</ul></td>
    <td>No</td>
    <td>Combination</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

## <a name="firstName"></a>1. Property `Person > firstName`

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

## <a name="lastName"></a>2. Property `Person > lastName`

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

## <a name="age"></a>3. Property `Person > age`

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

## <a name="driverLicenseId"></a>4. Property `Person > driverLicenseId`

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

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
