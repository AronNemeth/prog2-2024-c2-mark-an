# 2026-06-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.36324  |       1.02974  |   0.077817 |
| solution-1-flask   |     0.339001 |       1.00706  |   0.175398 |
| solution-aron-mark |     0.333014 |       0.116043 |   0.178913 |
| solution-pl        |     5.70091  |       0.138397 |   0.18207  |
| solution-1         |     7.02503  |       1e-06    |   0.490702 |
| solution-2         |     0.330243 |       0.507299 |   0.83121  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.330503 |       0.117612 |   0.272207 |
| solution-aron-mark |     0.330331 |       0.118664 |   0.272212 |
| solution-flask     |     0.338999 |       1.00725  |   0.310788 |
| solution-1-flask   |     0.333925 |       1.00717  |   0.543868 |
| solution-2         |     0.331043 |       0.397296 |   8.30928  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.331468 |       0.124661 |   0.801822 |
| solution-aron-mark |     0.333005 |       0.137424 |   0.810644 |
| solution-flask     |     0.333963 |       1.00761  |   1.28435  |
| solution-1-flask   |     0.337106 |       1.0072   |   4.29804  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.331315 |       0.146948 |    2.97781 |
| solution-aron-mark |     0.33808  |       0.145668 |    2.99686 |
| solution-flask     |     0.337357 |       1.00758  |    4.1127  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.336566 |       0.207615 |    15.3561 |
| solution-aron-mark |     0.330053 |       0.205    |    15.4767 |