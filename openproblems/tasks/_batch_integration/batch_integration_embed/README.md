<!--- TODO: add links --->

# Batch integration graph

This is a sub-task of the overall batch integration task. Batch (or data) integration integrates datasets across batches that arise from various biological and technical sources. Methods that integrate batches typically have three different types of output: a corrected feature matrix, a joint embedding across batches, and/or an integrated cell-cell similarity graph (e.g., a kNN graph). This sub-task focuses on all methods that can output integrated graphs, and includes methods that canonically output the other two data formats with subsequent postprocessing to generate a graph. Other sub-tasks for batch integration can be found for:

* [graphs](../batch_integration_graph/README.md), and
* [corrected features]()

This sub-task was taken from a [benchmarking study of data integration methods](https://www.biorxiv.org/content/10.1101/2020.05.22.111161v2).


## API

Datasets should contain the following attributes:

* `adata.obs["batch"]`
* `adata.obs["label"]`

Methods should assign output to `adata.obsm['X_emb'].

Metrics can compare:
* `adata.obsm['X_emb']` to `adata.obsm['X_uni']`,
* `adata.obsm['X_emb']` to `adata.obs['label']`, and/or
* `adata.obsm['X_emb']` to `adata.obs['batch']`.

To reuse metrics functions from `scIB`, [`metrics._utils._get_split`](metrics/_utils.py) separates the combined anndata into an integrated and an unintegrated anndata object.