# 2026-04-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4511   |       1.04717  |   0.101522 |
| solution-pl        |     4.34642  |       0.151813 |   0.231179 |
| solution-aron-mark |     0.434452 |       0.153006 |   0.233985 |
| solution-1-flask   |     0.42072  |       1.00822  |   0.258059 |
| solution-1         |     7.30034  |       1e-06    |   0.750453 |
| solution-2         |     0.412356 |       0.704391 |   1.35757  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.419139 |       0.148967 |   0.359867 |
| solution-pl        |     0.427972 |       0.150046 |   0.362477 |
| solution-flask     |     0.42309  |       1.00812  |   0.385016 |
| solution-1-flask   |     0.421589 |       1.00821  |   0.799349 |
| solution-2         |     0.414082 |       0.571119 |   3.03728  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424104 |       0.153539 |    1.09527 |
| solution-pl        |     0.415072 |       0.157734 |    1.11541 |
| solution-flask     |     0.421176 |       1.00821  |    1.57699 |
| solution-1-flask   |     0.422983 |       1.00811  |    5.64601 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429251 |       0.177107 |    3.8972  |
| solution-aron-mark |     0.439078 |       0.180947 |    3.9166  |
| solution-flask     |     0.431592 |       1.00846  |    5.19984 |