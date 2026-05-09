# 2026-05-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.03493  |       1.07216  |   0.102903 |
| solution-pl        |     0.414384 |       0.147802 |   0.236264 |
| solution-aron-mark |     4.39147  |       0.154686 |   0.256261 |
| solution-1-flask   |     0.428988 |       1.00809  |   0.273323 |
| solution-1         |     7.91683  |       1e-06    |   0.669034 |
| solution-2         |     0.415732 |       0.607358 |   1.28372  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415905 |       0.147718 |   0.365055 |
| solution-aron-mark |     0.413882 |       0.147813 |   0.366336 |
| solution-flask     |     0.413414 |       1.0082   |   0.405131 |
| solution-1-flask   |     0.416639 |       1.00854  |   0.802907 |
| solution-2         |     0.408961 |       0.508473 |   2.87156  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.421215 |       0.153643 |    1.10308 |
| solution-pl        |     0.427124 |       0.155485 |    1.11194 |
| solution-flask     |     0.413718 |       1.00843  |    1.68466 |
| solution-1-flask   |     0.421344 |       1.00835  |    5.75607 |
| solution-2         |     0.420429 |       0.577828 |   31.1329  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415024 |       0.180367 |    3.73594 |
| solution-aron-mark |     0.417863 |       0.178913 |    3.77961 |
| solution-flask     |     0.418129 |       1.0085   |    5.32596 |