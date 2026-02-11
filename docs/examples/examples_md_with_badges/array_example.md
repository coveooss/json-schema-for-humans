# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > fruits`](#fruits)
  - [1.1. root > fruits > fruits items](#fruits_items)

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

**Description:** A schema with an array

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
<li><a href="#">fruits</a></li>
</ul></td>
    <td>No</td>
    <td>array of string</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

## <a name="fruits"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > fruits`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array of string</code></td>
  </tr>
</table>

**Example:**

```json
[
    "apple",
    "banana"
]
```

<table>
  <tr>
    <th></th>
    <th>Array restrictions</th>
  </tr>
  <tr>
    <td><strong>Min items</strong></td>
    <td>N/A</td>
  </tr>
  <tr>
    <td><strong>Max items</strong></td>
    <td>N/A</td>
  </tr>
  <tr>
    <td><strong>Items unicity</strong></td>
    <td>False</td>
  </tr>
  <tr>
    <td><strong>Additional items</strong></td>
    <td>False</td>
  </tr>
  <tr>
    <td><strong>Tuple validation</strong></td>
    <td>See below</td>
  </tr>
</table>

<table>
  <tr>
    <th>Each item of this array must be</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="#fruits_items">fruits items</a></td>
    <td>-</td>
  </tr>
</table>

### <a name="fruits_items"></a>1.1. root > fruits > fruits items

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

**Example:**

```json
"apple"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
