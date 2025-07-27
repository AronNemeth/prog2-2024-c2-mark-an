# 2025-07-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.88383  |       1.11921  |   0.10241  |
| solution-pl        |     0.49648  |       0.148855 |   0.232914 |
| solution-aron-mark |     5.04622  |       0.146972 |   0.235299 |
| solution-1-flask   |     0.501227 |       1.00945  |   0.268265 |
| solution-1         |     8.13174  |       1e-06    |   0.704512 |
| solution-2         |     0.485786 |       0.754508 |   0.859202 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494946 |       0.150202 |   0.364136 |
| solution-aron-mark |     0.496571 |       0.151686 |   0.364765 |
| solution-flask     |     0.499739 |       1.00833  |   0.378694 |
| solution-1-flask   |     0.504038 |       1.00838  |   0.805309 |
| solution-2         |     0.49268  |       0.497759 |   5.84856  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49637  |       0.157351 |    1.08746 |
| solution-aron-mark |     0.492343 |       0.156512 |    1.09808 |
| solution-flask     |     0.493455 |       1.00834  |    1.58427 |
| solution-1-flask   |     0.499864 |       1.00822  |    5.59465 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495006 |       0.188698 |    3.19774 |
| solution-pl        |     0.493031 |       0.185744 |    3.20046 |
| solution-flask     |     0.493568 |       1.0082   |    5.06691 |