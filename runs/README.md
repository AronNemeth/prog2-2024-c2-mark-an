# 2026-10-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.01291  |       1.06192  |   0.077033 |
| solution-1-flask   |     0.338057 |       1.00726  |   0.175943 |
| solution-aron-mark |     5.43918  |       0.14483  |   0.19161  |
| solution-pl        |     0.336783 |       0.130767 |   0.198421 |
| solution-2         |     0.325436 |       0.700545 |   0.72426  |
| solution-1         |     6.97058  |       1e-06    |   0.846477 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.334815 |       1.00744  |   0.168043 |
| solution-pl        |     0.329854 |       0.131766 |   0.287361 |
| solution-aron-mark |     0.333744 |       0.130513 |   0.290029 |
| solution-1-flask   |     0.340874 |       1.00742  |   0.527515 |
| solution-2         |     0.332533 |       0.402519 |   8.60368  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.331012 |       1.00742  |   0.733735 |
| solution-aron-mark |     0.329498 |       0.136394 |   0.837707 |
| solution-pl        |     0.330032 |       0.134176 |   0.901726 |
| solution-1-flask   |     0.331846 |       1.00742  |   4.18743  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.333538 |       0.157404 |    2.70726 |
| solution-pl        |     0.328127 |       0.156848 |    2.73132 |
| solution-flask     |     0.341229 |       1.00824  |    3.24641 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.333972 |       0.283141 |    15.8666 |
| solution-pl        |     0.331654 |       0.221892 |    16.1868 |