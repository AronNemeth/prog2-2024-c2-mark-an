# 2026-01-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.22861  |       1.10042  |   0.101872 |
| solution-pl        |     0.484524 |       0.162724 |   0.247927 |
| solution-aron-mark |     0.497579 |       0.17533  |   0.251893 |
| solution-1-flask   |     0.488329 |       1.00841  |   0.266224 |
| solution-1         |     8.0869   |       1e-06    |   0.742552 |
| solution-2         |     5.65946  |       0.673508 |   0.914792 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473203 |       0.162296 |   0.374102 |
| solution-flask     |     0.478982 |       1.00859  |   0.383345 |
| solution-pl        |     0.495966 |       0.167215 |   0.383559 |
| solution-1-flask   |     0.483998 |       1.00844  |   0.796103 |
| solution-2         |     0.482066 |       0.529558 |   2.27316  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.47385  |       0.16957  |    1.09529 |
| solution-aron-mark |     0.482365 |       0.173128 |    1.09604 |
| solution-flask     |     0.494492 |       1.009    |    1.60573 |
| solution-1-flask   |     0.493728 |       1.00883  |    5.57205 |
| solution-2         |     0.479725 |       0.567457 |   40.7888  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478255 |       0.191482 |    3.69283 |
| solution-pl        |     0.489026 |       0.204781 |    3.69567 |
| solution-flask     |     0.486403 |       1.00865  |    5.23215 |