# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > fruits`](#fruits)
  - [1.1. root > fruits > fruits items](#fruits_items)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > vegetables`](#vegetables)
  - [2.1. root > vegetables > veggie](#vegetables_items)
    - [2.1.1. Property `root > vegetables > vegetables items > veggieName`](#vegetables_items_veggieName)
    - [2.1.2. Property `root > vegetables > vegetables items > veggieLike`](#vegetables_items_veggieLike)

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
  <tr>
    <td><ul>
<li><a href="#">vegetables</a></li>
</ul></td>
    <td>No</td>
    <td>array</td>
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

## <a name="vegetables"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > vegetables`

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
    <td><a href="#vegetables_items">veggie</a></td>
    <td>-</td>
  </tr>
</table>

### <a name="vegetables_items"></a>2.1. root > vegetables > veggie

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
    <td><h1>/definitions/veggie</h1></td>
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
<li><a href="#">veggieName</a></li>
</ul></td>
    <td>No</td>
    <td>string</td>
    <td>No</td>
    <td>-</td>
    <td>The name of the vegetable.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">veggieLike</a></li>
</ul></td>
    <td>No</td>
    <td>boolean</td>
    <td>No</td>
    <td>-</td>
    <td>Do I like this vegetable?</td>
  </tr>
</table>

#### <a name="vegetables_items_veggieName"></a>2.1.1. Property `root > vegetables > vegetables items > veggieName`

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

**Description:** The name of the vegetable.

#### <a name="vegetables_items_veggieLike"></a>2.1.2. Property `root > vegetables > vegetables items > veggieLike`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>boolean</code></td>
  </tr>
</table>

**Description:** Do I like this vegetable?

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
