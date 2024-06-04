# 2024-06-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.32003  |       1.244    |   0.07674  |
| solution-aron-mark |     5.86644  |       0.102601 |   0.159328 |
| solution-pl        |     0.657241 |       0.103015 |   0.162742 |
| solution-1-flask   |     0.68033  |       1.00899  |   0.266112 |
| solution-1         |     7.84036  |       1e-06    |   0.590708 |
| solution-2         |     0.662044 |       0.424628 |   0.964983 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.686345 |       1.00883  |   0.162038 |
| solution-pl        |     0.671997 |       0.105641 |   0.259268 |
| solution-aron-mark |     0.671797 |       0.105232 |   0.270895 |
| solution-1-flask   |     0.670108 |       1.00924  |   0.793879 |
| solution-2         |     0.671461 |       0.442569 |   3.10949  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661449 |       1.00919  |   0.722092 |
| solution-aron-mark |     0.670372 |       0.114151 |   0.807128 |
| solution-pl        |     0.68747  |       0.113375 |   0.816931 |
| solution-1-flask   |     0.679954 |       1.00925  |   5.63184  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66976  |       1.00917  |    2.48599 |
| solution-aron-mark |     0.677202 |       0.150781 |    2.63048 |
| solution-pl        |     0.677584 |       0.148124 |    2.64314 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.677527 |       1.00917  |    15.9038 |
| solution-aron-mark |     0.669762 |       0.275037 |    21.3031 |
| solution-pl        |     0.675096 |       0.281229 |    22.4439 |