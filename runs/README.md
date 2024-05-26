# 2024-05-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.49253  |       1.09322  |   0.068435 |
| solution-pl        |     0.65638  |       0.100613 |   0.1588   |
| solution-aron-mark |     6.04399  |       0.103634 |   0.16092  |
| solution-1-flask   |     0.688558 |       1.00917  |   0.264875 |
| solution-1         |     8.4623   |       2e-06    |   0.802049 |
| solution-2         |     0.67026  |       0.414109 |   1.15457  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66528  |        1.00917 |   0.158119 |
| solution-aron-mark |     0.685898 |        0.10532 |   0.257896 |
| solution-pl        |     0.661997 |        0.1024  |   0.261098 |
| solution-1-flask   |     0.69129  |        1.00912 |   0.796281 |
| solution-2         |     0.654247 |        0.43023 |   2.95608  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.716187 |       1.00893  |   0.681287 |
| solution-pl        |     0.667072 |       0.111202 |   0.79608  |
| solution-aron-mark |     0.683377 |       0.113005 |   0.798769 |
| solution-1-flask   |     0.686215 |       1.00919  |   5.58884  |
| solution-2         |     0.687059 |       0.508044 | 169.833    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.683193 |       1.00914  |    2.60627 |
| solution-aron-mark |     0.668377 |       0.152543 |    2.65438 |
| solution-pl        |     0.664869 |       0.152274 |    2.76625 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.673481 |       1.00923  |    16.9457 |
| solution-pl        |     0.662109 |       0.282146 |    22.3    |
| solution-aron-mark |     0.672725 |       0.282073 |    22.619  |