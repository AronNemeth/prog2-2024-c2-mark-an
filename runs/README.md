# 2025-01-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.31391  |       1.00904  |   0.106124 |
| solution-aron-mark |     1.03384  |       0.114546 |   0.193632 |
| solution-pl        |     0.977635 |       0.117527 |   0.19453  |
| solution-1-flask   |     5.79253  |       1.10978  |   0.286371 |
| solution-1         |     8.12932  |       1e-06    |   0.858592 |
| solution-2         |     1.01978  |       0.896151 |   1.15787  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.568893 |       0.116366 |   0.329052 |
| solution-pl        |     0.582568 |       0.122845 |   0.343258 |
| solution-flask     |     0.568727 |       1.0092   |   0.485789 |
| solution-1-flask   |     0.573458 |       1.00902  |   0.831874 |
| solution-2         |     0.552851 |       0.51706  |   2.21856  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.548926 |       0.122311 |    1.06925 |
| solution-aron-mark |     0.564553 |       0.125415 |    1.08056 |
| solution-flask     |     0.577967 |       1.00916  |    2.21096 |
| solution-1-flask   |     0.571304 |       1.00913  |    5.93754 |
| solution-2         |     0.535864 |       0.567349 |   39.915   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.564356 |       0.154567 |    5.06184 |
| solution-aron-mark |     0.546367 |       0.153776 |    5.36333 |
| solution-flask     |     0.546453 |       1.00918  |    9.29007 |