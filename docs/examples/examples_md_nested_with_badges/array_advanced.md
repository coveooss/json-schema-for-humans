<h1>Schema Docs</h1>

<code>Type: object</code>

<p>A little food fun</p>

<details>
<summary>
  <strong><a name="fruits"></a>fruits</strong></summary>

<code>Type: array of string</code>

<p>5 to 8 fruits that you like</p>

<code>Min items: 5</code> <code>Max items: 8</code> <code>Unique items: yes</code> 
<h5>Array items: root > fruits > fruits items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="vegetables"></a>vegetables</strong></summary>

<code>Type: array</code>

<h5>Array items: root > vegetables > vegetables items</h5>
<blockquote>

<code>Type: object</code>

</blockquote>

<h5>At least one of the items must be:</h5>
<blockquote>

<code>Type: const</code>

<code>Specific value: "eggplant"</code>

</blockquote>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>