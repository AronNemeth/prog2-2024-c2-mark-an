# 2024-12-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20435  |       1.01231  |   0.112814 |
| solution-aron-mark |     0.569571 |       0.112128 |   0.178969 |
| solution-pl        |     5.83661  |       0.111859 |   0.182734 |
| solution-1-flask   |     0.596789 |       1.00982  |   0.267432 |
| solution-1         |     7.60457  |       1e-06    |   0.698308 |
| solution-2         |     0.572359 |       0.611072 |   0.900689 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.574811 |       0.113575 |   0.306483 |
| solution-pl        |     0.58694  |       0.112043 |   0.34021  |
| solution-flask     |     0.597525 |       1.00935  |   0.527763 |
| solution-1-flask   |     0.619443 |       1.00905  |   0.793472 |
| solution-2         |     0.571629 |       0.489724 |   4.47065  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.583644 |       0.121519 |    1.03364 |
| solution-aron-mark |     0.569883 |       0.118594 |    1.03506 |
| solution-flask     |     0.574046 |       1.00911  |    2.29954 |
| solution-1-flask   |     0.585396 |       1.00941  |    5.51645 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.575181 |       0.149484 |    4.63231 |
| solution-pl        |     0.585474 |       0.1545   |    4.86534 |
| solution-flask     |     0.569444 |       1.00919  |    9.05149 |