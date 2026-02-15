# 2026-02-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.3575   |       1.06365  |   0.098323 |
| solution-aron-mark |     0.393391 |       0.131056 |   0.203455 |
| solution-pl        |     3.9424   |       0.129889 |   0.208515 |
| solution-1-flask   |     0.393854 |       1.00632  |   0.234296 |
| solution-1         |     6.70599  |       1e-06    |   0.53818  |
| solution-2         |     0.392145 |       0.598346 |   1.30027  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.395095 |       0.131489 |   0.318271 |
| solution-aron-mark |     0.396381 |       0.131468 |   0.321952 |
| solution-flask     |     0.401416 |       1.00657  |   0.411485 |
| solution-1-flask   |     0.401582 |       1.00629  |   0.721252 |
| solution-2         |     0.393445 |       0.477027 |   3.10606  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.395933 |       0.138525 |    1.04053 |
| solution-pl        |     0.397833 |       0.14367  |    1.06128 |
| solution-flask     |     0.413518 |       1.00717  |    1.7435  |
| solution-1-flask   |     0.412218 |       1.0065   |    5.35347 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.401587 |       0.168614 |    4.72665 |
| solution-pl        |     0.396374 |       0.166288 |    4.73617 |
| solution-flask     |     0.39589  |       1.00654  |    5.53513 |