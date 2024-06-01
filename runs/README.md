# 2024-06-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.35441  |       1.0672   |   0.100197 |
| solution-aron-mark |     6.09013  |       0.10713  |   0.171026 |
| solution-pl        |     0.678758 |       0.109321 |   0.172773 |
| solution-1-flask   |     0.710055 |       1.0101   |   0.275896 |
| solution-1         |     8.73263  |       1e-06    |   0.77092  |
| solution-2         |     0.694555 |       0.437922 |   1.55303  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.678418 |       1.0101   |   0.169011 |
| solution-aron-mark |     0.691167 |       0.106955 |   0.261209 |
| solution-pl        |     0.693456 |       0.110115 |   0.267362 |
| solution-1-flask   |     0.700668 |       1.00988  |   0.822722 |
| solution-2         |     0.702099 |       0.443134 |   2.15029  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689154 |       1.01049  |   0.730171 |
| solution-pl        |     0.696139 |       0.124019 |   0.836975 |
| solution-aron-mark |     0.684328 |       0.118631 |   0.84693  |
| solution-1-flask   |     0.692143 |       1.01121  |   5.738    |
| solution-2         |     0.690816 |       0.507028 |  30.1003   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.681171 |       1.01073  |    2.67262 |
| solution-aron-mark |     0.71999  |       0.159441 |    2.77576 |
| solution-pl        |     0.681662 |       0.158294 |    2.79266 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.697679 |       1.01049  |    19.0135 |
| solution-aron-mark |     0.691433 |       0.305003 |    25.1153 |
| solution-pl        |     0.690581 |       0.285086 |    25.795  |