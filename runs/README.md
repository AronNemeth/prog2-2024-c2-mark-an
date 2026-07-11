# 2026-07-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11867  |       1.06591  |   0.109903 |
| solution-aron-mark |     0.425105 |       0.149735 |   0.233418 |
| solution-1-flask   |     0.426369 |       1.00824  |   0.268632 |
| solution-pl        |     5.63113  |       0.177751 |   0.294968 |
| solution-1         |     7.15073  |       1e-06    |   0.697208 |
| solution-2         |     0.413277 |       0.725509 |   1.14299  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420506 |       0.149997 |   0.362916 |
| solution-aron-mark |     0.421922 |       0.151018 |   0.36682  |
| solution-flask     |     0.422088 |       1.00838  |   0.393589 |
| solution-1-flask   |     0.424676 |       1.00855  |   0.794386 |
| solution-2         |     0.421234 |       0.50105  |   6.35472  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.425428 |       0.161904 |    1.10223 |
| solution-pl        |     0.424427 |       0.155309 |    1.10537 |
| solution-flask     |     0.42796  |       1.00854  |    1.67115 |
| solution-1-flask   |     0.428561 |       1.00854  |    5.76885 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.424515 |       0.182008 |    3.88836 |
| solution-aron-mark |     0.429949 |       0.185756 |    3.91284 |
| solution-flask     |     0.428834 |       1.00918  |    5.37369 |