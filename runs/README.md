# 2025-12-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.78878  |       1.11049  |   0.102222 |
| solution-pl        |     0.469355 |       0.163837 |   0.243433 |
| solution-aron-mark |     0.469622 |       0.160352 |   0.247259 |
| solution-1-flask   |     0.475596 |       1.00823  |   0.270678 |
| solution-2         |     5.78477  |       0.76504  |   0.811632 |
| solution-1         |     8.65616  |       1e-06    |   0.890065 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.471827 |       0.162849 |   0.366138 |
| solution-flask     |     0.464965 |       1.00838  |   0.371541 |
| solution-pl        |     0.471997 |       0.163573 |   0.374959 |
| solution-1-flask   |     0.494225 |       1.00836  |   0.778266 |
| solution-2         |     0.46841  |       0.501662 |  13.2115   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.474081 |       0.168652 |    1.07954 |
| solution-pl        |     0.47344  |       0.167225 |    1.09387 |
| solution-flask     |     0.464931 |       1.00845  |    1.57595 |
| solution-1-flask   |     0.471833 |       1.00861  |    5.53565 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465523 |       0.191744 |    3.56387 |
| solution-aron-mark |     0.472111 |       0.191473 |    3.58642 |
| solution-flask     |     0.469144 |       1.0086   |    5.13992 |