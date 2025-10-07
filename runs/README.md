# 2025-10-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.52811  |       1.07572  |   0.106801 |
| solution-aron-mark |     0.499619 |       0.16274  |   0.247642 |
| solution-pl        |     0.525374 |       0.163933 |   0.251985 |
| solution-1-flask   |     0.500494 |       1.00833  |   0.270319 |
| solution-1         |     7.63788  |       1e-06    |   0.766597 |
| solution-2         |     4.6038   |       0.909086 |   1.03843  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.498705 |       0.164747 |   0.376262 |
| solution-flask     |     0.503656 |       1.00882  |   0.377879 |
| solution-pl        |     0.505858 |       0.163607 |   0.396209 |
| solution-1-flask   |     0.503829 |       1.00852  |   0.813988 |
| solution-2         |     0.496145 |       0.519056 |   5.33933  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506799 |       0.168999 |    1.10282 |
| solution-aron-mark |     0.509254 |       0.165759 |    1.14048 |
| solution-flask     |     0.501253 |       1.00868  |    1.61499 |
| solution-1-flask   |     0.491523 |       1.00919  |    5.70527 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.493994 |       0.204943 |    3.39208 |
| solution-aron-mark |     0.504786 |       0.199782 |    3.39596 |
| solution-flask     |     0.499721 |       1.00863  |    5.24737 |