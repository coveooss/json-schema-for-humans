# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo`](#signingTimeInfo)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > signingTimeInfo > signingTime`](#signingTimeInfo_signingTime)
  - [1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds`](#signingTimeInfo_signingTimeBounds)
    - [1.2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > lowerBound`](#signingTimeInfo_signingTimeBounds_lowerBound)
    - [1.2.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > upperBound`](#signingTimeInfo_signingTimeBounds_upperBound)

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
<li><a href="#">signingTimeInfo</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/dss2-SigningTimeInfoType</td>
    <td>-</td>
  </tr>
</table>

## <a name="signingTimeInfo"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo`

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
    <td><h1>/definitions/dss2-SigningTimeInfoType</h1></td>
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
<li><a href="#">signingTime</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">signingTimeBounds</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries</td>
    <td>-</td>
  </tr>
</table>

### <a name="signingTimeInfo_signingTime"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > signingTimeInfo > signingTime`

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
    <td><strong>Format</strong></td>
    <td><code>utc-millisec</code></td>
  </tr>
</table>

### <a name="signingTimeInfo_signingTimeBounds"></a>1.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds`

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
    <td><h1>/definitions/dss2-SigningTimeInfoType%3ASigningTimeBoundaries</h1></td>
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
<li><a href="#">lowerBound</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">upperBound</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

#### <a name="signingTimeInfo_signingTimeBounds_lowerBound"></a>1.2.1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > lowerBound`

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
    <td><strong>Format</strong></td>
    <td><code>utc-millisec</code></td>
  </tr>
</table>

#### <a name="signingTimeInfo_signingTimeBounds_upperBound"></a>1.2.2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > signingTimeInfo > signingTimeBounds > upperBound`

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
    <td><strong>Format</strong></td>
    <td><code>utc-millisec</code></td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
