# 2026-05-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67566  |       1.05993  |   0.105882 |
| solution-aron-mark |     4.32513  |       0.150262 |   0.234848 |
| solution-pl        |     0.427875 |       0.150967 |   0.237717 |
| solution-1-flask   |     0.429691 |       1.00847  |   0.260634 |
| solution-1         |     7.5054   |       1e-06    |   0.622265 |
| solution-2         |     0.421322 |       0.580148 |   1.50819  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42605  |       0.151264 |   0.363097 |
| solution-pl        |     0.426024 |       0.151576 |   0.366904 |
| solution-flask     |     0.426124 |       1.0085   |   0.39597  |
| solution-1-flask   |     0.42549  |       1.0085   |   0.802676 |
| solution-2         |     0.421421 |       0.523568 |  13.9436   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432757 |       0.157863 |    1.10492 |
| solution-aron-mark |     0.426567 |       0.156325 |    1.12164 |
| solution-flask     |     0.418632 |       1.00857  |    1.6614  |
| solution-1-flask   |     0.425518 |       1.00888  |    5.76557 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422405 |       0.180787 |    3.87488 |
| solution-pl        |     0.421544 |       0.181113 |    3.88424 |
| solution-flask     |     0.442515 |       1.00856  |    5.34152 |