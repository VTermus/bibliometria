# Bibliometria
A package for bibliometric analysis of journals.

This package provides tools for retrieving journal information and comparing metrics,  
combining the data from SCImago Journal Rank and Web of Science. 

## Installation
```bash
pip install pycauctile
```

## Usage
```python
import bibliometria

```

## Data
Built-in Datasets
```
import bibliometria as bm

sjr = bm.get_sjr()   # pandas.DataFrame
wos = bm.get_wos()   # pandas.DataFrame
```
## Main functions

The package exposes four main functions for working with journal data.
---
### `title_matches(title_query, limit=10, score_cutoff=60) -> pd.DataFrame`

Fuzzy-search a journal by its **title** across both SCImago Journal Rank (SJR) and Web of Science (WoS).  
Returns a DataFrame with the top candidate matches, their similarity scores, data source, and basic journal metadata  
(e.g. title, ISSN/eISSN, SJR, quartiles).

Typical use case: quickly see a list of possible matches when you are not sure about the exact journal title.

---
### `title_best_match(title_query) -> pd.Series | None`

Find the **single best fuzzy match** for a journal title across SJR and WoS.  
Returns a pandas Series with the matched title, similarity score, data source, and core metadata,  
or `None` if no reasonable match is found.

Typical use case: you want one “best guess” journal record for a given title string.

---
### `journal_metrics(query, query_type="title") -> pd.Series`

Retrieve **core bibliometric indicators** for a journal, using either:

- `query_type="title"` – fuzzy match by journal title, or  
- `query_type="issn"` – exact match by ISSN / eISSN.

The returned Series contains a small set of harmonised metrics such as:

- `sjr`, `sjr_best_quartile`, `h_index` (from SJR)  
- `wos_quartile`, `wos_jif`, `wos_jif_5_year` (from WoS, if available)

If the journal is not found, an “empty” Series with all fields set to `None` is returned, and a warning is emitted.

---
### `journal_info(query, query_type="title") -> pd.DataFrame`

Return a **single-row DataFrame** with all available fields for a journal from both SJR and WoS,  
merged into one record. Supports the same lookup modes as `journal_metrics`:

- `query_type="title"` – fuzzy title match  
- `query_type="issn"` – exact ISSN / eISSN match

The result also includes a few metadata columns describing the lookup:

- `query`, `query_type`, `source_primary`, `matched_title`, `match_score`

## Interactive examples

You can explore example outputs in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://github.com/VTermus/bibliometria/blob/main/bibliometria_demo.ipynb
)

## Contribution
This package is in the testing status.
To report a bug or suggest an improvement, you can open an issue or contact us directly.

Authors: Vladislava Termus, Alexandra Pogozheva
