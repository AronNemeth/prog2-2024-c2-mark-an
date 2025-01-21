# 2025-01-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.85756  |       1.00879  |   0.080092 |
| solution-aron-mark |     0.537469 |       0.111475 |   0.177881 |
| solution-pl        |     0.544044 |       0.114638 |   0.181461 |
| solution-1-flask   |     5.08667  |       1.05484  |   0.267218 |
| solution-1         |     7.50818  |       1e-06    |   0.602196 |
| solution-2         |     0.548765 |       0.641545 |   0.976295 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543386 |       0.114913 |   0.28232  |
| solution-aron-mark |     0.567934 |       0.122117 |   0.286353 |
| solution-flask     |     0.558474 |       1.0091   |   0.297386 |
| solution-1-flask   |     0.560229 |       1.00887  |   0.800781 |
| solution-2         |     0.562168 |       0.521469 |   3.36854  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.5526   |       0.122587 |   0.885229 |
| solution-aron-mark |     0.567138 |       0.122743 |   0.897939 |
| solution-flask     |     0.545726 |       1.00898  |   1.2564   |
| solution-1-flask   |     0.551542 |       1.0094   |   5.69008  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.551009 |       0.150862 |    2.90656 |
| solution-aron-mark |     0.550121 |       0.148993 |    2.92333 |
| solution-flask     |     0.537125 |       1.00914  |    4.36221 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.538579 |       0.255339 |    17.4386 |
| solution-aron-mark |     0.534533 |       0.254085 |    17.7666 |