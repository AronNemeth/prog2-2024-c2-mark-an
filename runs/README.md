# 2025-12-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67729  |       1.16639  |   0.09973  |
| solution-aron-mark |     0.49136  |       0.16369  |   0.246757 |
| solution-pl        |     0.486424 |       0.165271 |   0.250412 |
| solution-1-flask   |     0.493432 |       1.0083   |   0.272437 |
| solution-1         |     7.76126  |       1e-06    |   0.694593 |
| solution-2         |     4.6963   |       0.648152 |   1.04532  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48732  |       0.167957 |   0.3646   |
| solution-aron-mark |     0.488501 |       0.167754 |   0.371377 |
| solution-flask     |     0.483784 |       1.00856  |   0.376148 |
| solution-1-flask   |     0.487031 |       1.00843  |   0.798448 |
| solution-2         |     0.483687 |       0.538964 |   3.495    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48765  |       0.171369 |    1.05882 |
| solution-pl        |     0.48652  |       0.172338 |    1.05947 |
| solution-flask     |     0.486776 |       1.00853  |    1.58665 |
| solution-1-flask   |     0.498629 |       1.00853  |    5.64094 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.489807 |       0.196601 |    3.63523 |
| solution-aron-mark |     0.486964 |       0.198571 |    3.64211 |
| solution-flask     |     0.487005 |       1.00831  |    5.24435 |