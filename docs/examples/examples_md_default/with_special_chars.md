# Personne

- [1. Property `Personne > prénom`](#pr_nom)
- [2. Property `Personne > nomDeFamille`](#nomDeFamille)
- [3. Property `Personne > âge`](#a_ge)
- [4. Property `Personne > 0 de quoi d'autre`](#a0_de_quoi_d_autre)

**Title:** Personne

|                           |                                                                           |
| ------------------------- | ------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                  |
| **Required**              | No                                                                        |
| **Additional properties** | [[Any type: allowed]](# "Additional Properties of any type are allowed.") |

| Property                                    | Pattern | Type    | Deprecated | Definition | Title/Description                                     |
| ------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------------------------------------------- |
| - [prénom](#pr_nom )                        | No      | string  | No         | -          | Le prénom de la personne.                             |
| - [nomDeFamille](#nomDeFamille )            | No      | string  | No         | -          | Le nom de famille de la personne.                     |
| - [âge](#a_ge )                             | No      | integer | No         | -          | L'âge en années qui doit être plus grand ou égal à 0. |
| - [0 de quoi d'autre](#a0_de_quoi_d_autre ) | No      | string  | No         | -          | -                                                     |

## <a name="pr_nom"></a>1. Property `Personne > prénom`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Le prénom de la personne.

## <a name="nomDeFamille"></a>2. Property `Personne > nomDeFamille`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Le nom de famille de la personne.

## <a name="a_ge"></a>3. Property `Personne > âge`

|              |           |
| ------------ | --------- |
| **Type**     | `integer` |
| **Required** | No        |

**Description:** L'âge en années qui doit être plus grand ou égal à 0.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="a0_de_quoi_d_autre"></a>4. Property `Personne > 0 de quoi d'autre`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Examples:** 

```json
"🖖"
```

```json
"صباح الخير"
```

```json
"你好"
```

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
