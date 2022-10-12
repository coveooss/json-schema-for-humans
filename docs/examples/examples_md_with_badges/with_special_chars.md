# Personne

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > prénom`](#pr_nom)
- [2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > nomDeFamille`](#nomDeFamille)
- [3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > âge`](#a_ge)
- [4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 0 de quoi d'autre`](#a0_de_quoi_d_autre)

**Title:** Personne

|                           |                                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                                          |
| **Additional properties** | [![Any type: allowed](https://img.shields.io/badge/Any%20type-allowed-green)](# "Additional Properties of any type are allowed.") |

| Property                                    | Pattern | Type    | Deprecated | Definition | Title/Description                                     |
| ------------------------------------------- | ------- | ------- | ---------- | ---------- | ----------------------------------------------------- |
| - [prénom](#pr_nom )                        | No      | string  | No         | -          | Le prénom de la personne.                             |
| - [nomDeFamille](#nomDeFamille )            | No      | string  | No         | -          | Le nom de famille de la personne.                     |
| - [âge](#a_ge )                             | No      | integer | No         | -          | L'âge en années qui doit être plus grand ou égal à 0. |
| - [0 de quoi d'autre](#a0_de_quoi_d_autre ) | No      | string  | No         | -          | -                                                     |

## <a name="pr_nom"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > prénom`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Le prénom de la personne.

## <a name="nomDeFamille"></a>2. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > nomDeFamille`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Le nom de famille de la personne.

## <a name="a_ge"></a>3. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > âge`

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** L'âge en années qui doit être plus grand ou égal à 0.

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

## <a name="a0_de_quoi_d_autre"></a>4. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `Personne > 0 de quoi d'autre`

|          |          |
| -------- | -------- |
| **Type** | `string` |

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
