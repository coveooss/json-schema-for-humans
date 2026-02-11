<h1>Schema Docs</h1>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="objectA"></a>objectA</strong></summary>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="objectA_signature"></a>signature</strong></summary>

<h4>Signature</h4>

<code>Type: object</code>

<h4>One of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0"></a>Option 1</h5>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers"></a>signers</strong></summary>

<h4>Signature</h4>

<code>Type: array</code>

<p>Unique top level property for Multiple Signatures. (multisignature)</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature</h5>
<blockquote>

<h4>Signature</h4>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_algorithm"></a>algorithm</strong> <code>Required</code></summary>

<h4>One of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i0"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: enum (of string)</code>

<p>Signature algorithm. The currently recognized JWA [RFC7518] and RFC8037 [RFC8037] asymmetric key algorithms. Note: Unlike RFC8037 [RFC8037] JSF requires explicit Ed* algorithm names instead of "EdDSA".</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"RS256"</code></li>
<li><code>"RS384"</code></li>
<li><code>"RS512"</code></li>
<li><code>"PS256"</code></li>
<li><code>"PS384"</code></li>
<li><code>"PS512"</code></li>
<li><code>"ES256"</code></li>
<li><code>"ES384"</code></li>
<li><code>"ES512"</code></li>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
<li><code>"HS256"</code></li>
<li><code>"HS384"</code></li>
<li><code>"HS512"</code></li>
</ul>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i1"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: string</code>
<code>Format: uri</code>

<p>Signature algorithm. Note: If proprietary signature algorithms are added, they must be expressed as URIs.</p>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_keyId"></a>keyId</strong></summary>

<h4>Key ID</h4>

<code>Type: string</code>

<p>Optional. Application specific string identifying the signature key.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey"></a>publicKey</strong></summary>

<h4>Public key</h4>

<code>Type: object</code>

<p>Optional. Public key object.</p>

<h4>All of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0"></a>Requirement 1</h5>

<code>Type: object</code>

<h5>If (<code>kty = "EC"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EC curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"P-256"</code></li>
<li><code>"P-384"</code></li>
<li><code>"P-521"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-521", the decoded argument must be 66 bytes.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_y"></a>y</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point Y. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-256", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1"></a>Requirement 2</h5>

<code>Type: object</code>

<h5>If (<code>kty = "OKP"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EdDSA curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EdDSA curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "Ed25519", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2"></a>Requirement 3</h5>

<code>Type: object</code>

<h5>If (<code>kty = "RSA"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_n"></a>n</strong> <code>Required</code></summary>

<h4>Modulus</h4>

<code>Type: string</code>

<p>RSA modulus.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_e"></a>e</strong> <code>Required</code></summary>

<h4>Exponent</h4>

<code>Type: string</code>

<p>RSA exponent.</p>

</details>

</blockquote>

</blockquote>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"EC"</code></li>
<li><code>"OKP"</code></li>
<li><code>"RSA"</code></li>
</ul>

</details>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_certificatePath"></a>certificatePath</strong></summary>

<h4>Certificate path</h4>

<code>Type: array of string</code>

<p>Optional. Sorted array of X.509 [RFC5280] certificates, where the first element must contain the signature certificate. The certificate path must be contiguous but is not required to be complete.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > certificatePath > certificatePath items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_excludes"></a>excludes</strong></summary>

<h4>Excludes</h4>

<code>Type: array of string</code>

<p>Optional. Array holding the names of one or more application level properties that must be excluded from the signature process. Note that the "excludes" property itself, must also be excluded from the signature process. Since both the "excludes" property and the associated data it points to are unsigned, a conforming JSF implementation must provide options for specifying which properties to accept.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > excludes > excludes items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_value"></a>value</strong> <code>Required</code></summary>

<h4>Signature</h4>

<code>Type: string</code>

<p>The signature data. Note that the binary representation must follow the JWA [RFC7518] specifications.</p>

</details>

</blockquote>

</details>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i1"></a>Option 2</h5>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i1_chain"></a>chain</strong></summary>

<h4>Signature</h4>

<code>Type: array</code>

<p>Unique top level property for Signature Chains. (signaturechain)</p>

<h5>Array items: root > objectA > signature > oneOf > item 1 > chain > Signature</h5>
<blockquote>

<h4>Signature</h4>

<code>Type: object</code>

<a href="#objectA_signature_oneOf_i0_signers_items">Same definition as Signature</a>
</blockquote>

</details>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i2"></a>Signature</h5>

<h4>Signature</h4>

<code>Type: object</code>

<p>Unique top level property for simple signatures. (signaturecore)</p>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_algorithm"></a>algorithm</strong> <code>Required</code></summary>

<h4>One of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i0"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: enum (of string)</code>

<p>Signature algorithm. The currently recognized JWA [RFC7518] and RFC8037 [RFC8037] asymmetric key algorithms. Note: Unlike RFC8037 [RFC8037] JSF requires explicit Ed* algorithm names instead of "EdDSA".</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"RS256"</code></li>
<li><code>"RS384"</code></li>
<li><code>"RS512"</code></li>
<li><code>"PS256"</code></li>
<li><code>"PS384"</code></li>
<li><code>"PS512"</code></li>
<li><code>"ES256"</code></li>
<li><code>"ES384"</code></li>
<li><code>"ES512"</code></li>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
<li><code>"HS256"</code></li>
<li><code>"HS384"</code></li>
<li><code>"HS512"</code></li>
</ul>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i1"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: string</code>
<code>Format: uri</code>

<p>Signature algorithm. Note: If proprietary signature algorithms are added, they must be expressed as URIs.</p>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_keyId"></a>keyId</strong></summary>

<h4>Key ID</h4>

<code>Type: string</code>

<p>Optional. Application specific string identifying the signature key.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey"></a>publicKey</strong></summary>

<h4>Public key</h4>

<code>Type: object</code>

<p>Optional. Public key object.</p>

<h4>All of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0"></a>Requirement 1</h5>

<code>Type: object</code>

<h5>If (<code>kty = "EC"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EC curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"P-256"</code></li>
<li><code>"P-384"</code></li>
<li><code>"P-521"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-521", the decoded argument must be 66 bytes.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_y"></a>y</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point Y. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-256", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1"></a>Requirement 2</h5>

<code>Type: object</code>

<h5>If (<code>kty = "OKP"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EdDSA curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EdDSA curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "Ed25519", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2"></a>Requirement 3</h5>

<code>Type: object</code>

<h5>If (<code>kty = "RSA"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_n"></a>n</strong> <code>Required</code></summary>

<h4>Modulus</h4>

<code>Type: string</code>

<p>RSA modulus.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_e"></a>e</strong> <code>Required</code></summary>

<h4>Exponent</h4>

<code>Type: string</code>

<p>RSA exponent.</p>

</details>

</blockquote>

</blockquote>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"EC"</code></li>
<li><code>"OKP"</code></li>
<li><code>"RSA"</code></li>
</ul>

</details>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_certificatePath"></a>certificatePath</strong></summary>

<h4>Certificate path</h4>

<code>Type: array of string</code>

<p>Optional. Sorted array of X.509 [RFC5280] certificates, where the first element must contain the signature certificate. The certificate path must be contiguous but is not required to be complete.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > certificatePath > certificatePath items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_excludes"></a>excludes</strong></summary>

<h4>Excludes</h4>

<code>Type: array of string</code>

<p>Optional. Array holding the names of one or more application level properties that must be excluded from the signature process. Note that the "excludes" property itself, must also be excluded from the signature process. Since both the "excludes" property and the associated data it points to are unsigned, a conforming JSF implementation must provide options for specifying which properties to accept.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > excludes > excludes items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_value"></a>value</strong> <code>Required</code></summary>

<h4>Signature</h4>

<code>Type: string</code>

<p>The signature data. Note that the binary representation must follow the JWA [RFC7518] specifications.</p>

</details>

</blockquote>

</details>

</details>

<details>
<summary>
  <strong><a name="objectB"></a>objectB</strong></summary>

<code>Type: object</code>

<details>
<summary>
  <strong><a name="objectB_signature"></a>signature</strong></summary>

<h4>Signature</h4>

<code>Type: object</code>

<h4>One of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0"></a>Option 1</h5>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers"></a>signers</strong></summary>

<h4>Signature</h4>

<code>Type: array</code>

<p>Unique top level property for Multiple Signatures. (multisignature)</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature</h5>
<blockquote>

<h4>Signature</h4>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_algorithm"></a>algorithm</strong> <code>Required</code></summary>

<h4>One of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i0"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: enum (of string)</code>

<p>Signature algorithm. The currently recognized JWA [RFC7518] and RFC8037 [RFC8037] asymmetric key algorithms. Note: Unlike RFC8037 [RFC8037] JSF requires explicit Ed* algorithm names instead of "EdDSA".</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"RS256"</code></li>
<li><code>"RS384"</code></li>
<li><code>"RS512"</code></li>
<li><code>"PS256"</code></li>
<li><code>"PS384"</code></li>
<li><code>"PS512"</code></li>
<li><code>"ES256"</code></li>
<li><code>"ES384"</code></li>
<li><code>"ES512"</code></li>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
<li><code>"HS256"</code></li>
<li><code>"HS384"</code></li>
<li><code>"HS512"</code></li>
</ul>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i1"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: string</code>
<code>Format: uri</code>

<p>Signature algorithm. Note: If proprietary signature algorithms are added, they must be expressed as URIs.</p>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_keyId"></a>keyId</strong></summary>

<h4>Key ID</h4>

<code>Type: string</code>

<p>Optional. Application specific string identifying the signature key.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey"></a>publicKey</strong></summary>

<h4>Public key</h4>

<code>Type: object</code>

<p>Optional. Public key object.</p>

<h4>All of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0"></a>Requirement 1</h5>

<code>Type: object</code>

<h5>If (<code>kty = "EC"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EC curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"P-256"</code></li>
<li><code>"P-384"</code></li>
<li><code>"P-521"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-521", the decoded argument must be 66 bytes.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_y"></a>y</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point Y. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-256", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1"></a>Requirement 2</h5>

<code>Type: object</code>

<h5>If (<code>kty = "OKP"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EdDSA curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EdDSA curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "Ed25519", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2"></a>Requirement 3</h5>

<code>Type: object</code>

<h5>If (<code>kty = "RSA"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_n"></a>n</strong> <code>Required</code></summary>

<h4>Modulus</h4>

<code>Type: string</code>

<p>RSA modulus.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_e"></a>e</strong> <code>Required</code></summary>

<h4>Exponent</h4>

<code>Type: string</code>

<p>RSA exponent.</p>

</details>

</blockquote>

</blockquote>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"EC"</code></li>
<li><code>"OKP"</code></li>
<li><code>"RSA"</code></li>
</ul>

</details>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_certificatePath"></a>certificatePath</strong></summary>

<h4>Certificate path</h4>

<code>Type: array of string</code>

<p>Optional. Sorted array of X.509 [RFC5280] certificates, where the first element must contain the signature certificate. The certificate path must be contiguous but is not required to be complete.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > certificatePath > certificatePath items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_excludes"></a>excludes</strong></summary>

<h4>Excludes</h4>

<code>Type: array of string</code>

<p>Optional. Array holding the names of one or more application level properties that must be excluded from the signature process. Note that the "excludes" property itself, must also be excluded from the signature process. Since both the "excludes" property and the associated data it points to are unsigned, a conforming JSF implementation must provide options for specifying which properties to accept.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > excludes > excludes items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_value"></a>value</strong> <code>Required</code></summary>

<h4>Signature</h4>

<code>Type: string</code>

<p>The signature data. Note that the binary representation must follow the JWA [RFC7518] specifications.</p>

</details>

</blockquote>

</details>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i1"></a>Option 2</h5>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i1_chain"></a>chain</strong></summary>

<h4>Signature</h4>

<code>Type: array</code>

<p>Unique top level property for Signature Chains. (signaturechain)</p>

<h5>Array items: root > objectA > signature > oneOf > item 1 > chain > Signature</h5>
<blockquote>

<h4>Signature</h4>

<code>Type: object</code>

<a href="#objectA_signature_oneOf_i0_signers_items">Same definition as Signature</a>
</blockquote>

</details>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i2"></a>Signature</h5>

<h4>Signature</h4>

<code>Type: object</code>

<p>Unique top level property for simple signatures. (signaturecore)</p>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_algorithm"></a>algorithm</strong> <code>Required</code></summary>

<h4>One of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i0"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: enum (of string)</code>

<p>Signature algorithm. The currently recognized JWA [RFC7518] and RFC8037 [RFC8037] asymmetric key algorithms. Note: Unlike RFC8037 [RFC8037] JSF requires explicit Ed* algorithm names instead of "EdDSA".</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"RS256"</code></li>
<li><code>"RS384"</code></li>
<li><code>"RS512"</code></li>
<li><code>"PS256"</code></li>
<li><code>"PS384"</code></li>
<li><code>"PS512"</code></li>
<li><code>"ES256"</code></li>
<li><code>"ES384"</code></li>
<li><code>"ES512"</code></li>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
<li><code>"HS256"</code></li>
<li><code>"HS384"</code></li>
<li><code>"HS512"</code></li>
</ul>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_algorithm_oneOf_i1"></a>Algorithm</h5>

<h4>Algorithm</h4>

<code>Type: string</code>
<code>Format: uri</code>

<p>Signature algorithm. Note: If proprietary signature algorithms are added, they must be expressed as URIs.</p>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_keyId"></a>keyId</strong></summary>

<h4>Key ID</h4>

<code>Type: string</code>

<p>Optional. Application specific string identifying the signature key.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey"></a>publicKey</strong></summary>

<h4>Public key</h4>

<code>Type: object</code>

<p>Optional. Public key object.</p>

<h4>All of</h4>

<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0"></a>Requirement 1</h5>

<code>Type: object</code>

<h5>If (<code>kty = "EC"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EC curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"P-256"</code></li>
<li><code>"P-384"</code></li>
<li><code>"P-521"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-521", the decoded argument must be 66 bytes.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i0_then_y"></a>y</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EC curve point Y. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "P-256", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1"></a>Requirement 2</h5>

<code>Type: object</code>

<h5>If (<code>kty = "OKP"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_crv"></a>crv</strong> <code>Required</code></summary>

<h4>Curve name</h4>

<code>Type: enum (of string)</code>

<p>EdDSA curve name.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"Ed25519"</code></li>
<li><code>"Ed448"</code></li>
</ul>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i1_then_x"></a>x</strong> <code>Required</code></summary>

<h4>Coordinate</h4>

<code>Type: string</code>

<p>EdDSA curve point X. The length of this field must be the full size of a coordinate for the curve specified in the "crv" parameter. For example, if the value of "crv" is "Ed25519", the decoded argument must be 32 bytes.</p>

</details>

</blockquote>

</blockquote>
<blockquote>
<h5><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2"></a>Requirement 3</h5>

<code>Type: object</code>

<h5>If (<code>kty = "RSA"</code>)</h5>
<blockquote>

<code>Type: object</code>

<code>No Additional Properties</code>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<a href="#objectA_signature_oneOf_i0_signers_items_publicKey_kty">Same definition as kty</a>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_n"></a>n</strong> <code>Required</code></summary>

<h4>Modulus</h4>

<code>Type: string</code>

<p>RSA modulus.</p>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_allOf_i2_then_e"></a>e</strong> <code>Required</code></summary>

<h4>Exponent</h4>

<code>Type: string</code>

<p>RSA exponent.</p>

</details>

</blockquote>

</blockquote>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_publicKey_kty"></a>kty</strong> <code>Required</code></summary>

<h4>Key type</h4>

<code>Type: enum (of string)</code>

<p>Key type indicator.</p>

<h4>Must be one of:</h4>
<ul>
<li><code>"EC"</code></li>
<li><code>"OKP"</code></li>
<li><code>"RSA"</code></li>
</ul>

</details>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_certificatePath"></a>certificatePath</strong></summary>

<h4>Certificate path</h4>

<code>Type: array of string</code>

<p>Optional. Sorted array of X.509 [RFC5280] certificates, where the first element must contain the signature certificate. The certificate path must be contiguous but is not required to be complete.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > certificatePath > certificatePath items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_excludes"></a>excludes</strong></summary>

<h4>Excludes</h4>

<code>Type: array of string</code>

<p>Optional. Array holding the names of one or more application level properties that must be excluded from the signature process. Note that the "excludes" property itself, must also be excluded from the signature process. Since both the "excludes" property and the associated data it points to are unsigned, a conforming JSF implementation must provide options for specifying which properties to accept.</p>

<h5>Array items: root > objectA > signature > oneOf > item 0 > signers > Signature > excludes > excludes items</h5>
<blockquote>

<code>Type: string</code>

</blockquote>

</details>

<details>
<summary>
  <strong><a name="objectA_signature_oneOf_i0_signers_items_value"></a>value</strong> <code>Required</code></summary>

<h4>Signature</h4>

<code>Type: string</code>

<p>The signature data. Note that the binary representation must follow the JWA [RFC7518] specifications.</p>

</details>

</blockquote>

</details>

</details>

<hr/>
<footer>
<p>Generated using <a href="https://github.com/coveooss/json-schema-for-humans">json-schema-for-humans</a></p>
</footer>