# 2026-08-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.92577  |       1.09826  |   0.146262 |
| solution-1-flask   |     0.44606  |       1.00984  |   0.228932 |
| solution-aron-mark |     4.66089  |       0.156087 |   0.236789 |
| solution-pl        |     0.439993 |       0.1613   |   0.239085 |
| solution-1         |     8.04964  |       1e-06    |   0.614898 |
| solution-2         |     0.450557 |       0.584239 |   1.15813  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451805 |       0.15957  |   0.360602 |
| solution-aron-mark |     0.449079 |       0.160921 |   0.362959 |
| solution-flask     |     0.446178 |       1.00916  |   0.385177 |
| solution-1-flask   |     0.448155 |       1.00906  |   0.730459 |
| solution-2         |     0.431019 |       0.527197 |   6.06241  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.434135 |       0.162948 |    1.03305 |
| solution-pl        |     0.440864 |       0.261437 |    1.05375 |
| solution-flask     |     0.442727 |       1.0094   |    1.62464 |
| solution-1-flask   |     0.447362 |       1.00952  |    5.62457 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.443417 |       0.189962 |    3.52349 |
| solution-aron-mark |     0.448616 |       0.193751 |    3.55731 |
| solution-flask     |     0.449381 |       1.00934  |    5.35448 |