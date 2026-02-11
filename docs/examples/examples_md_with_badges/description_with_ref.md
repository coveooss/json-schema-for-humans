# Schema Docs

- [1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer`](#outer)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer > inner`](#outer_inner)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > outer2`](#outer2)

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
<li><a href="#">outer</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>In #/definitions/inner schema</td>
    <td>We should see this</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">outer2</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>Same as <a href="#">outer</a></td>
    <td>We should see this too</td>
  </tr>
</table>

## <a name="outer"></a>1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer`

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
  <tr>
    <td><strong>Defined in</strong></td>
    <td><h1>/definitions/inner schema</h1></td>
  </tr>
</table>

**Description:** We should see this

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
<li><a href="#">inner</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>inner description</td>
  </tr>
</table>

### <a name="outer_inner"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > outer > inner`

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

**Description:** inner description

## <a name="outer2"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > outer2`

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
  <tr>
    <td><strong>Same definition as</strong></td>
    <td><a href="#outer">outer</a></td>
  </tr>
</table>

**Description:** We should see this too

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
