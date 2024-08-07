# 2024-08-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.570198 |       1.00905  |   0.091599 |
| solution-pl        |     0.569157 |       0.103111 |   0.170335 |
| solution-aron-mark |     1.83712  |       0.105204 |   0.183887 |
| solution-1-flask   |     1.07042  |       1.11972  |   0.263406 |
| solution-1         |     7.81561  |       1e-06    |   0.78203  |
| solution-2         |     4.47503  |       0.72053  |   0.892025 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552944 |       1.00938  |   0.225074 |
| solution-pl        |     0.550943 |       0.103513 |   0.287341 |
| solution-aron-mark |     0.549968 |       0.105133 |   0.290255 |
| solution-1-flask   |     0.558292 |       1.00903  |   0.763328 |
| solution-2         |     0.562126 |       0.473625 |  13.781    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551427 |       1.00886  |   0.917333 |
| solution-pl        |     0.554365 |       0.110653 |   1.00096  |
| solution-aron-mark |     0.565582 |       0.109591 |   1.00342  |
| solution-1-flask   |     0.559694 |       1.00899  |   5.5304   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.549555 |       1.00947  |    4.15811 |
| solution-pl        |     0.552948 |       0.142922 |    4.1977  |
| solution-aron-mark |     0.55357  |       0.142299 |    4.22417 |