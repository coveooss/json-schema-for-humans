# Person

- [1. Property `Person > subType1`](#subType1)
  - [1.1. Property `Person > subType1 > subProp1`](#subType1_subProp1)
- [2. Property `Person > subType2`](#subType2)
  - [2.1. Property `Person > subType2 > subProp2`](#subType2_subProp2)
- [3. Property `Person > anInt`](#anInt)
- [4. Property `Person > additionalProperties`](#additionalProperties)
  - [4.1. Property `Person > additionalProperties > propA`](#additionalProperties_propA)

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
    <td><a href="#additionalProperties">Each additional property must conform to the schema</a></td>
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
<li><a href="#">subType1</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>A sub type with additionalProperties false.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">subType2</a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>A sub type with additionalProperties true.</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#">anInt</a></li>
</ul></td>
    <td>No</td>
    <td>integer</td>
    <td>No</td>
    <td>-</td>
    <td>This is an integer, it should not show additional properties. (issue #132)</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#"></a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>additionalProperties schema.</td>
  </tr>
</table>

## <a name="subType1"></a>1. Property `Person > subType1`

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
    <td>Not allowed</td>
  </tr>
</table>

**Description:** A sub type with additionalProperties false.

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
<li><a href="#">subProp1</a></li>
</ul></td>
    <td>No</td>
    <td>number</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

### <a name="subType1_subProp1"></a>1.1. Property `Person > subType1 > subProp1`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

## <a name="subType2"></a>2. Property `Person > subType2`

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

**Description:** A sub type with additionalProperties true.

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
<li><a href="#">subProp2</a></li>
</ul></td>
    <td>No</td>
    <td>number</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><ul>
<li><a href="#"></a></li>
</ul></td>
    <td>No</td>
    <td>object</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

### <a name="subType2_subProp2"></a>2.1. Property `Person > subType2 > subProp2`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

## <a name="anInt"></a>3. Property `Person > anInt`

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

**Description:** This is an integer, it should not show additional properties. (issue #132)

## <a name="additionalProperties"></a>4. Property `Person > additionalProperties`

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

**Description:** additionalProperties schema.

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
<li><a href="#">propA</a></li>
</ul></td>
    <td>No</td>
    <td>number</td>
    <td>No</td>
    <td>-</td>
    <td>-</td>
  </tr>
</table>

### <a name="additionalProperties_propA"></a>4.1. Property `Person > additionalProperties > propA`

<table>
  <tr>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><strong>Type</strong></td>
    <td><code>number</code></td>
  </tr>
  <tr>
    <td><strong>Required</strong></td>
    <td>No</td>
  </tr>
</table>

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
