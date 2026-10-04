# 2026-10-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.26102  |       1.04207  |   0.108506 |
| solution-aron-mark |     5.67853  |       0.160097 |   0.240737 |
| solution-pl        |     0.418141 |       0.154983 |   0.251694 |
| solution-1-flask   |     0.432525 |       1.00868  |   0.26769  |
| solution-1         |     7.64802  |       1e-06    |   0.605415 |
| solution-2         |     0.41666  |       0.54834  |   0.859665 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.425966 |       0.156121 |   0.375011 |
| solution-aron-mark |     0.429389 |       0.154268 |   0.376337 |
| solution-flask     |     0.421572 |       1.00828  |   0.514073 |
| solution-1-flask   |     0.448343 |       1.00856  |   0.811215 |
| solution-2         |     0.421242 |       0.498665 |   3.35371  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.423002 |       0.161994 |    1.13703 |
| solution-aron-mark |     0.42837  |       0.161327 |    1.14784 |
| solution-flask     |     0.425393 |       1.00825  |    1.7141  |
| solution-1-flask   |     0.428914 |       1.00859  |    5.75181 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.425419 |       0.187392 |    3.52897 |
| solution-aron-mark |     0.426945 |       0.182635 |    3.53308 |
| solution-flask     |     0.423974 |       1.00902  |    5.4537  |