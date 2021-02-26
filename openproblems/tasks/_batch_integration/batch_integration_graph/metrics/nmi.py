from .....tools.decorators import metric
from scIB.clustering import opt_louvain
from scIB.metrics import nmi

import numpy as np


@metric(
    metric_name="NMI",
    maximize=True,
    # image="openproblems-template-image" # only if required
)
def nmi(adata):
    res_max, nmi_max, nmi_all = opt_louvain(
        adata,
        label_key="labels",
        cluster_key="cluster",
        function=nmi,
        plot=False,
        verbose=verbose,
        inplace=True,
        force=True,
    )
    return nmi(adata, group1="cluster", group2="labels")
