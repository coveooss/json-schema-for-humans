# Schema Docs

- [1. [Optional] Property root > signingTimeInfo](#signingTimeInfo)
  - [1.1. [Required] Property root > signingTimeInfo > signingTime](#signingTimeInfo_signingTime)
  - [1.2. [Optional] Property root > signingTimeInfo > signingTimeBounds](#signingTimeInfo_signingTimeBounds)
    - [1.2.1. [Optional] Property root > signingTimeInfo > signingTimeBounds > lowerBound](#signingTimeInfo_signingTimeBounds_lowerBound)
    - [1.2.2. [Optional] Property root > signingTimeInfo > signingTimeBounds > upperBound](#signingTimeInfo_signingTimeBounds_upperBound)

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
<strong> <a name="signingTimeInfo"></a>1. [Optional] Property root > signingTimeInfo</strong>  

</summary>

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/dss2-SigningTimeInfoType</h1></td>
  </tr>
</table>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTime"></a>1.1. [Required] Property root > signingTimeInfo > signingTime</strong>  

</summary>

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
    <td>Yes</td>
  </tr>
  <tr>
    <td><strong>Format</strong></td>
    <td><code>utc-millisec</code></td>
  </tr>
</table>

</details>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds"></a>1.2. [Optional] Property root > signingTimeInfo > signingTimeBounds</strong>  

</summary>

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries</h1></td>
  </tr>
</table>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds_lowerBound"></a>1.2.1. [Optional] Property root > signingTimeInfo > signingTimeBounds > lowerBound</strong>  

</summary>

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
  <tr>
    <td><strong>Format</strong></td>
    <td><code>utc-millisec</code></td>
  </tr>
</table>

</details>

<details>
<summary>
<strong> <a name="signingTimeInfo_signingTimeBounds_upperBound"></a>1.2.2. [Optional] Property root > signingTimeInfo > signingTimeBounds > upperBound</strong>  

</summary>

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
  <tr>
    <td><strong>Format</strong></td>
    <td><code>utc-millisec</code></td>
  </tr>
</table>

</details>

</details>

</details>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)