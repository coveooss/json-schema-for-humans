<h1>Schema Docs</h1>

<code>Type: object</code>

<p>Testing $ref</p>

<details>
<summary>
  <strong><a name="a_gift"></a>a_gift</strong></summary>

<code>Type: string</code>

<p>A gift, or is it?</p>

</details>

<details>
<summary>
  <strong><a name="file_prefix"></a>file_prefix</strong></summary>

<code>Type: string</code>

<p>A gift, or is it?</p>

<a href="#a_gift">Same definition as a_gift</a>

</details>

<details>
<summary>
  <strong><a name="anchor_with_slash"></a>anchor_with_slash</strong></summary>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="anchor_with_slash_propertyA"></a>propertyA</strong></summary>

<code>Type: string</code>

<p>Description for object_def/items/propertyA</p>

</details>

</details>

<details>
<summary>
  <strong><a name="anchor_no_slash"></a>anchor_no_slash</strong></summary>

<code>Type: array of string</code>

<p>Description for array_def</p>

<h5>Array items: root > anchor_no_slash > anchor_no_slash items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="anchor_nested_reference"></a>anchor_nested_reference</strong></summary>

<code>Type: string</code>

</details>

<details>
<summary>
  <strong><a name="same_file_anchor_with_slash"></a>same_file_anchor_with_slash</strong></summary>

<code>Type: string</code>

<p>Description for string_def</p>

</details>

<details>
<summary>
  <strong><a name="same_file_anchor_no_slash"></a>same_file_anchor_no_slash</strong></summary>

<code>Type: object</code>

<a href="#anchor_with_slash">Same definition as anchor_with_slash</a>

</details>

<details>
<summary>
  <strong><a name="same_file_nested_reference"></a>same_file_nested_reference</strong></summary>

<code>Type: string</code>

<a href="#anchor_nested_reference">Same definition as anchor_nested_reference</a>

</details>

<details>
<summary>
  <strong><a name="other_file_anchor"></a>other_file_anchor</strong></summary>

<code>Type: object</code>

<p>The delivery is a gift, no prices displayed</p>

<details>
<summary>
  <strong><a name="other_file_anchor_with_wrap"></a>with_wrap</strong></summary>

<code>Type: boolean</code>

</details>

</details>

<details>
<summary>
  <strong><a name="other_file_dot_anchor"></a>other_file_dot_anchor</strong></summary>

<code>Type: object</code>

<p>The delivery is a gift, no prices displayed</p>

<a href="#other_file_anchor">Same definition as other_file_anchor</a>

</details>

<details>
<summary>
  <strong><a name="other_file_dot_dot_anchor"></a>other_file_dot_dot_anchor</strong></summary>

<code>Type: object</code>

<p>The delivery is a gift, no prices displayed</p>

<a href="#other_file_anchor">Same definition as other_file_anchor</a>

</details>

<details>
<summary>
  <strong><a name="other_file_only"></a>other_file_only</strong></summary>

<code>Type: object</code>

<p>Test schema with a not</p>

<details>
<summary>
  <strong><a name="other_file_only_not_a_string"></a>not_a_string</strong> <code>Required</code></summary>

<h4>Must <strong>not</strong> be:</h4>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

</details>

<details>
<summary>
  <strong><a name="multi_hierarchy_reference"></a>multi_hierarchy_reference</strong></summary>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="multi_hierarchy_reference_propertyA"></a>propertyA</strong></summary>

<code>Type: string</code>

<p>Contents of propertyA in final.json</p>

</details>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>