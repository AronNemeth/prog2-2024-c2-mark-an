# 2026-01-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.81204  |       1.04429  |   0.110426 |
| solution-pl        |     0.490423 |       0.175278 |   0.256459 |
| solution-aron-mark |     0.495871 |       0.173414 |   0.256865 |
| solution-1-flask   |     0.494055 |       1.00847  |   0.276277 |
| solution-1         |     8.04815  |       1e-06    |   0.69518  |
| solution-2         |     4.67799  |       0.734181 |   0.995447 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4921   |       0.170019 |   0.379202 |
| solution-aron-mark |     0.49474  |       0.171319 |   0.379677 |
| solution-flask     |     0.492052 |       1.00888  |   0.383134 |
| solution-1-flask   |     0.499243 |       1.00867  |   0.823445 |
| solution-2         |     0.492568 |       0.540668 |   5.06789  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494255 |       0.176761 |    1.08032 |
| solution-pl        |     0.499116 |       0.179493 |    1.09932 |
| solution-flask     |     0.490648 |       1.00851  |    1.63467 |
| solution-1-flask   |     0.499218 |       1.00859  |    5.75514 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490322 |       0.202245 |    3.69393 |
| solution-aron-mark |     0.491601 |       0.200551 |    3.72665 |
| solution-flask     |     0.497284 |       1.0087   |    5.27835 |