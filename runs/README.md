# 2026-09-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.14793  |       1.17663  |   0.127322 |
| solution-pl        |     2.11193  |       0.167485 |   0.245978 |
| solution-aron-mark |     0.426502 |       0.160589 |   0.247788 |
| solution-1-flask   |     0.45039  |       1.00843  |   0.274337 |
| solution-1         |     7.64715  |       1e-06    |   0.650139 |
| solution-2         |     4.40936  |       0.677329 |   0.859842 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.467674 |       0.162591 |   0.381582 |
| solution-aron-mark |     0.436518 |       0.157851 |   0.39657  |
| solution-flask     |     0.429733 |       1.00836  |   0.403955 |
| solution-1-flask   |     0.435674 |       1.00931  |   0.829859 |
| solution-2         |     0.428002 |       0.506566 |   4.20221  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.430894 |       0.162241 |    1.16379 |
| solution-aron-mark |     0.436362 |       0.1619   |    1.17531 |
| solution-flask     |     0.435867 |       1.00885  |    1.68377 |
| solution-1-flask   |     0.440562 |       1.00875  |    5.82859 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.425005 |       0.18437  |    3.6074  |
| solution-pl        |     0.437532 |       0.188085 |    3.64454 |
| solution-flask     |     0.429601 |       1.00879  |    5.44014 |