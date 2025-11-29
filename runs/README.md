# 2025-11-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.52556  |       1.03927  |   0.101222 |
| solution-pl        |     0.475506 |       0.157601 |   0.241193 |
| solution-aron-mark |     0.464584 |       0.156326 |   0.243222 |
| solution-1-flask   |     0.478193 |       1.00822  |   0.261297 |
| solution-1         |     7.46201  |       1e-06    |   0.703626 |
| solution-2         |     4.60481  |       0.624423 |   0.893693 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.473028 |       0.158719 |   0.360057 |
| solution-pl        |     0.473743 |       0.157426 |   0.369514 |
| solution-flask     |     0.471826 |       1.0082   |   0.372054 |
| solution-1-flask   |     0.476562 |       1.00838  |   0.7913   |
| solution-2         |     0.46491  |       0.501041 |   2.73459  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.467464 |       0.16477  |    1.07105 |
| solution-aron-mark |     0.470502 |       0.1652   |    1.07282 |
| solution-flask     |     0.468463 |       1.00856  |    1.56513 |
| solution-1-flask   |     0.475816 |       1.00858  |    5.44614 |
| solution-2         |     0.469316 |       0.560564 |   36.0658  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.468589 |       0.19501  |    3.20571 |
| solution-pl        |     0.467287 |       0.194141 |    3.20878 |
| solution-flask     |     0.469986 |       1.00852  |    5.03716 |