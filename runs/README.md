# 2026-07-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.3037   |       1.04611  |   0.108893 |
| solution-pl        |     6.55845  |       0.166722 |   0.214923 |
| solution-aron-mark |     0.400767 |       0.140602 |   0.2203   |
| solution-1-flask   |     0.409595 |       1.00677  |   0.239582 |
| solution-1         |     7.81746  |       1e-06    |   0.626491 |
| solution-2         |     0.393416 |       0.693955 |   1.05872  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.405578 |       0.142618 |   0.334289 |
| solution-pl        |     0.409652 |       0.148323 |   0.33852  |
| solution-flask     |     0.405264 |       1.00705  |   0.428338 |
| solution-1-flask   |     0.419572 |       1.00755  |   0.7268   |
| solution-2         |     0.405249 |       0.503921 |   4.39031  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.397442 |       0.150289 |    1.03718 |
| solution-pl        |     0.401948 |       0.150831 |    1.05542 |
| solution-flask     |     0.404992 |       1.00742  |    1.8424  |
| solution-1-flask   |     0.412256 |       1.00762  |    5.4712  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.400728 |       0.175743 |    4.83522 |
| solution-pl        |     0.401258 |       0.178652 |    4.88634 |
| solution-flask     |     0.392947 |       1.00721  |    5.82759 |