# 2026-09-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08771  |       1.14016  |   0.097483 |
| solution-1-flask   |     0.426033 |       1.00888  |   0.221446 |
| solution-pl        |     2.11096  |       0.165839 |   0.227266 |
| solution-aron-mark |     0.41688  |       0.157487 |   0.230145 |
| solution-1         |     7.35522  |       1e-06    |   0.610792 |
| solution-2         |     4.64073  |       0.858971 |   1.51319  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419947 |       0.157216 |   0.353702 |
| solution-aron-mark |     0.419744 |       0.155022 |   0.354455 |
| solution-flask     |     0.419432 |       1.00901  |   0.385612 |
| solution-1-flask   |     0.428647 |       1.00886  |   0.728088 |
| solution-2         |     0.422315 |       0.495248 |   2.53582  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420004 |       0.159511 |    1.02602 |
| solution-pl        |     0.421268 |       0.160512 |    1.04164 |
| solution-flask     |     0.42323  |       1.01009  |    1.66786 |
| solution-1-flask   |     0.425523 |       1.00914  |    5.65389 |
| solution-2         |     0.42106  |       0.548268 |  454.984   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.421421 |       0.187878 |    3.40565 |
| solution-aron-mark |     0.420974 |       0.186497 |    3.43038 |
| solution-flask     |     0.420436 |       1.00914  |    5.15934 |