# 2026-10-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.02633  |       1.12116  |   0.053768 |
| solution-1-flask   |     0.321453 |       1.00756  |   0.133822 |
| solution-pl        |     0.274894 |       0.109474 |   0.154004 |
| solution-aron-mark |     4.3973   |       0.123909 |   0.154261 |
| solution-1         |     5.30361  |       0        |   0.398908 |
| solution-2         |     0.299067 |       0.42833  |   0.668029 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.298855 |       1.00752  |   0.108433 |
| solution-aron-mark |     0.315647 |       0.147602 |   0.214594 |
| solution-pl        |     0.313964 |       0.116939 |   0.222794 |
| solution-1-flask   |     0.301375 |       1.01072  |   0.391423 |
| solution-2         |     0.309264 |       0.384491 |   3.76652  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.314367 |       1.01246  |   0.544138 |
| solution-aron-mark |     0.303282 |       0.146766 |   0.591264 |
| solution-pl        |     0.33605  |       0.125607 |   0.59321  |
| solution-1-flask   |     0.308207 |       1.00751  |   2.95851  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.302521 |       0.143327 |    2.05556 |
| solution-aron-mark |     0.301522 |       0.158971 |    2.06704 |
| solution-flask     |     0.303587 |       1.00762  |    2.5359  |
| solution-1-flask   |     0.311688 |       1.00762  |   27.8086  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.30268  |       0.19383  |    14.0021 |
| solution-aron-mark |     0.307702 |       0.199947 |    14.7001 |
| solution-flask     |     0.282552 |       1.00775  |    17.7967 |