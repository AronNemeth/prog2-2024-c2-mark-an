# 2024-09-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.42759  |       1.11314  |   0.093732 |
| solution-pl        |     0.621218 |       0.110807 |   0.182555 |
| solution-aron-mark |    19.9948   |       0.113947 |   0.201869 |
| solution-1-flask   |     0.606844 |       1.00928  |   0.26646  |
| solution-1         |     8.6944   |       1e-06    |   0.62691  |
| solution-2         |     0.616318 |       0.598971 |   1.03477  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.611749 |       1.00912  |   0.197985 |
| solution-aron-mark |     0.602985 |       0.114797 |   0.302707 |
| solution-pl        |     0.598519 |       0.110017 |   0.303879 |
| solution-1-flask   |     0.602789 |       1.00897  |   0.788461 |
| solution-2         |     0.619451 |       0.52265  |   3.3388   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.630648 |       1.00939  |   0.915519 |
| solution-aron-mark |     0.612075 |       0.129652 |   1.00981  |
| solution-pl        |     0.666801 |       0.118452 |   1.01897  |
| solution-1-flask   |     0.609797 |       1.00936  |   5.75651  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.581359 |       0.149185 |    4.77969 |
| solution-flask     |     0.622235 |       1.00955  |    4.94347 |
| solution-pl        |     0.612346 |       0.155538 |    5.00043 |