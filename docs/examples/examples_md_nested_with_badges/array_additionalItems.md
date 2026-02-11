<h1>Schema Docs</h1>

<code>Type: object</code>

<p>A little food fun</p>

<details>
<summary>
  <strong><a name="address"></a>address</strong></summary>

<code>Type: array</code>

<h5>Item 1: root > address > a number</h5>
<blockquote>

<h4>a number</h4>

<code>Type: number</code>

</blockquote>
<h5>Item 2: root > address > address item 1</h5>
<blockquote>

<code>Type: string</code>

<p>followed by a string</p>

</blockquote>
<h5>Item 3: root > address > again a string</h5>
<blockquote>

<h4>again a string</h4>

<code>Type: enum (of string)</code>

<h4>Must be one of:</h4>
<ul>
<li><code>"Street"</code></li>
<li><code>"Avenue"</code></li>
<li><code>"Boulevard"</code></li>
</ul>

</blockquote>
<h5>Item 4: root > address > finally an enum</h5>
<blockquote>

<h4>finally an enum</h4>

<code>Type: enum (of string)</code>

<h4>Must be one of:</h4>
<ul>
<li><code>"NW"</code></li>
<li><code>"NE"</code></li>
<li><code>"SW"</code></li>
<li><code>"SE"</code></li>
</ul>

</blockquote>

<strong>Example:</strong>

<pre><code class="language-json">[
    1600,
    "Pennsylvania",
    "Avenue",
    "NW",
    "Washington"
]</code></pre>

</details>

<details>
<summary>
  <strong><a name="addressLines"></a>addressLines</strong></summary>

<code>Type: array</code>

<p>list of address lines</p>

<h5>Item 1: root > addressLines > addressLines item 0</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="arrayEmpty"></a>arrayEmpty</strong></summary>

<code>Type: array</code>

<p>This is not a valid JSON Schema, but let's do it anyway.</p>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>