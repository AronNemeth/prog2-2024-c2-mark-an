# 2024-05-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657334 |       1.00903  |   0.074865 |
| solution-pl        |     6.24351  |       0.139061 |   0.176078 |
| solution-aron-mark |     0.66472  |       0.115138 |   0.181389 |
| solution-1-flask   |     1.50287  |       1.09006  |   0.262049 |
| solution-1         |     8.22281  |       1e-06    |   0.859694 |
| solution-2         |     0.665658 |       0.41315  |   1.14026  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66734  |       1.00874  |   0.165967 |
| solution-aron-mark |     0.669353 |       0.125306 |   0.273572 |
| solution-pl        |     0.664773 |       0.123433 |   0.274509 |
| solution-1-flask   |     0.679292 |       1.00885  |   0.780055 |
| solution-2         |     0.661964 |       0.430788 |   4.8524   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.669672 |       1.00912  |   0.700691 |
| solution-aron-mark |     0.673149 |       0.130695 |   0.833353 |
| solution-pl        |     0.668156 |       0.132282 |   0.835689 |
| solution-1-flask   |     0.677253 |       1.00918  |   5.63013  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659076 |       1.00921  |    2.54019 |
| solution-pl        |     0.661306 |       0.170014 |    2.63451 |
| solution-aron-mark |     0.679479 |       0.172014 |    2.72395 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.66057  |       0.298268 |    15.6158 |
| solution-aron-mark |     0.659628 |       0.298506 |    15.809  |
| solution-flask     |     0.653817 |       1.00919  |    16.1734 |