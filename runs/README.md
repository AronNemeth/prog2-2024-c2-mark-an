# 2026-01-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.88175  |       1.04325  |   0.100719 |
| solution-aron-mark |     0.476264 |       0.165592 |   0.245877 |
| solution-pl        |     0.473307 |       0.16289  |   0.248161 |
| solution-1-flask   |     0.481532 |       1.00823  |   0.267537 |
| solution-1         |     7.96879  |       1e-06    |   0.646747 |
| solution-2         |     4.83927  |       0.597547 |   1.02022  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473156 |       0.163045 |   0.362488 |
| solution-aron-mark |     0.474561 |       0.170621 |   0.362735 |
| solution-flask     |     0.466233 |       1.00827  |   0.371902 |
| solution-1-flask   |     0.483695 |       1.00834  |   0.787391 |
| solution-2         |     0.477386 |       0.534837 |   9.97463  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.46809  |       0.167902 |    1.05921 |
| solution-aron-mark |     0.467051 |       0.165668 |    1.06153 |
| solution-flask     |     0.468033 |       1.00852  |    1.57256 |
| solution-1-flask   |     0.470647 |       1.00842  |    5.4385  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.468811 |       0.191566 |    3.52592 |
| solution-aron-mark |     0.473487 |       0.194767 |    3.54708 |
| solution-flask     |     0.465369 |       1.00818  |    5.08341 |