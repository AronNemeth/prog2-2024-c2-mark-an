# 2024-08-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.01436 |       1.00893  |   0.091232 |
| solution-aron-mark |      2.27612 |       0.102815 |   0.168229 |
| solution-pl        |      1.02034 |       0.108571 |   0.170307 |
| solution-1-flask   |      1.52701 |       1.05516  |   0.348662 |
| solution-2         |      4.90204 |       0.884703 |   1.03183  |
| solution-1         |      8.29675 |       1e-06    |   1.34223  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.01625 |       1.00914  |   0.220437 |
| solution-aron-mark |      1.02114 |       0.102949 |   0.287488 |
| solution-pl        |      1.02301 |       0.104395 |   0.291912 |
| solution-1-flask   |      1.04893 |       1.00895  |   0.788069 |
| solution-2         |      1.01594 |       0.471616 |   4.97174  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.0133  |       1.00923  |   0.880323 |
| solution-pl        |      1.02026 |       0.111356 |   0.983154 |
| solution-aron-mark |      1.02726 |       0.111116 |   0.992294 |
| solution-1-flask   |      1.05912 |       1.00907  |   5.56326  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.583572 |       0.142476 |    4.24421 |
| solution-aron-mark |     0.732553 |       0.148822 |    4.32322 |
| solution-flask     |     0.564021 |       1.00927  |    4.55602 |