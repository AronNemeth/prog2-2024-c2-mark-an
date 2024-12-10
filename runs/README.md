# 2024-12-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.41186  |       1.18885  |   0.115754 |
| solution-aron-mark |     0.587571 |       0.111114 |   0.181442 |
| solution-pl        |     6.01434  |       0.112757 |   0.186601 |
| solution-1-flask   |     0.615477 |       1.00928  |   0.264188 |
| solution-1         |     8.17939  |       1e-06    |   0.612936 |
| solution-2         |     0.593601 |       0.560724 |   1.4062   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.593675 |       0.112224 |   0.308333 |
| solution-aron-mark |     0.600399 |       0.114721 |   0.313608 |
| solution-flask     |     0.571367 |       1.00922  |   0.50167  |
| solution-1-flask   |     0.57901  |       1.00954  |   0.778728 |
| solution-2         |     0.592556 |       0.514316 |   2.89869  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.582557 |       0.121285 |    1.04218 |
| solution-pl        |     0.59526  |       0.120848 |    1.07144 |
| solution-flask     |     0.585934 |       1.00912  |    2.23768 |
| solution-1-flask   |     0.605871 |       1.0092   |    5.53599 |
| solution-2         |     0.589977 |       0.537495 |   42.9007  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.577085 |       0.157444 |    4.52438 |
| solution-aron-mark |     0.567717 |       0.147146 |    4.58709 |
| solution-flask     |     0.566538 |       1.00904  |    9.07973 |