# 2024-11-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11053  |       1.0542   |   0.114146 |
| solution-aron-mark |     0.560052 |       0.111553 |   0.178093 |
| solution-pl        |     5.75601  |       0.112175 |   0.182635 |
| solution-1-flask   |     0.587045 |       1.00929  |   0.262057 |
| solution-1         |     7.6261   |       1e-06    |   0.592878 |
| solution-2         |     0.574288 |       0.543921 |   0.965859 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.561469 |       0.110143 |   0.301715 |
| solution-aron-mark |     0.564795 |       0.109472 |   0.340338 |
| solution-flask     |     0.565261 |       1.00906  |   0.48041  |
| solution-1-flask   |     0.570966 |       1.00915  |   0.804897 |
| solution-2         |     0.571528 |       0.472956 |   1.73133  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.576763 |       0.11876  |    1.01982 |
| solution-aron-mark |     0.569457 |       0.117426 |    1.0297  |
| solution-flask     |     0.567342 |       1.00915  |    2.12821 |
| solution-1-flask   |     0.592314 |       1.00955  |    5.49409 |
| solution-2         |     0.578058 |       0.549401 |   44.1582  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.574414 |       0.151383 |    4.40927 |
| solution-pl        |     0.580127 |       0.147898 |    4.56618 |
| solution-flask     |     0.567753 |       1.00944  |    8.69274 |