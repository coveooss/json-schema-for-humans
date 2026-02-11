# Person

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > person`](#person)
  - [1.1. Person > person > person](#person_items)
    - [1.1.1. Property `Person > person > person items > children`](#person_items_children)
      - [1.1.1.1. Person > person > person items > children > person](#person_items_children_items)

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
<li><a href="#">person</a></li>
</ul></td>
    <td>No</td>
    <td>array</td>
    <td>No</td>
    <td>-</td>
    <td>A list of people</td>
  </tr>
</table>

## <a name="person"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Person > person`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array</code></td>
  </tr>
</table>

**Description:** A list of people

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
    <td><a href="#person_items">person</a></td>
    <td>A human being</td>
  </tr>
</table>

### <a name="person_items"></a>1.1. Person > person > person

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
    <td><h1>/definitions/person</h1></td>
  </tr>
</table>

**Description:** A human being

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
<li><a href="#">children</a></li>
</ul></td>
    <td>No</td>
    <td>array</td>
    <td>No</td>
    <td>-</td>
    <td>The children they had</td>
  </tr>
</table>

#### <a name="person_items_children"></a>1.1.1. Property `Person > person > person items > children`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>array</code></td>
  </tr>
</table>

**Description:** The children they had

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
    <td><a href="#person_items_children_items">person</a></td>
    <td>A human being</td>
  </tr>
</table>

##### <a name="person_items_children_items"></a>1.1.1.1. Person > person > person items > children > person

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
    <td><strong>Same definition as</strong></td>
    <td><a href="#person_items">person_items</a></td>
  </tr>
</table>

**Description:** A human being

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
