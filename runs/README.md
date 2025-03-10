# 2025-03-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.606523 |       1.00965  |   0.085025 |
| solution-aron-mark |     2.04256  |       0.156657 |   0.214232 |
| solution-pl        |     0.584374 |       0.158602 |   0.265481 |
| solution-1-flask   |     5.23827  |       1.06395  |   0.273043 |
| solution-1         |     7.76844  |       2e-06    |   0.607909 |
| solution-2         |     0.56975  |       0.578345 |   1.33463  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.570772 |       1.00927  |   0.291293 |
| solution-aron-mark |     0.617235 |       0.147422 |   0.317718 |
| solution-pl        |     0.591222 |       0.154604 |   0.321662 |
| solution-1-flask   |     0.555066 |       1.00927  |   0.820743 |
| solution-2         |     0.551985 |       0.521973 |  14.1974   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543364 |       0.152777 |   0.896106 |
| solution-aron-mark |     0.547535 |       0.154276 |   0.910648 |
| solution-flask     |     0.563822 |       1.00909  |   1.2604   |
| solution-1-flask   |     0.591842 |       1.00898  |   5.9195   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.549976 |       0.178599 |    2.78995 |
| solution-pl        |     0.540828 |       0.184724 |    2.82782 |
| solution-flask     |     0.531699 |       1.00851  |    4.14009 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.532566 |       0.289995 |    17.0982 |
| solution-pl        |     0.539827 |       0.278241 |    18.0316 |