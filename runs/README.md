# 2025-03-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.522904 |       1.0092   |   0.080628 |
| solution-aron-mark |     2.05368  |       0.120943 |   0.188639 |
| solution-pl        |     0.527719 |       0.121272 |   0.201922 |
| solution-1-flask   |     5.31474  |       1.05722  |   0.267847 |
| solution-1         |     7.72314  |       1e-06    |   0.599293 |
| solution-2         |     0.525285 |       0.554677 |   1.49667  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525334 |       0.122988 |   0.296364 |
| solution-aron-mark |     0.527334 |       0.123286 |   0.29694  |
| solution-flask     |     0.523071 |       1.00864  |   0.298057 |
| solution-1-flask   |     0.532225 |       1.009    |   0.827332 |
| solution-2         |     0.519387 |       0.527172 |   4.18828  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.531115 |       0.130284 |   0.909699 |
| solution-pl        |     0.529762 |       0.132148 |   0.922079 |
| solution-flask     |     0.516361 |       1.00925  |   1.25968  |
| solution-1-flask   |     0.535153 |       1.00908  |   5.70111  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.526847 |       0.162626 |    2.83606 |
| solution-aron-mark |     0.534675 |       0.16031  |    2.84571 |
| solution-flask     |     0.531291 |       1.00906  |    4.30122 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.519879 |       0.274437 |    16.9307 |
| solution-aron-mark |     0.528006 |       0.273516 |    16.9421 |