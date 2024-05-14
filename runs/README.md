# 2024-05-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671424 |       1.00914  |   0.076281 |
| solution-pl        |     6.23608  |       0.12963  |   0.177191 |
| solution-aron-mark |     0.681861 |       0.124081 |   0.184277 |
| solution-1-flask   |     1.45988  |       1.04545  |   0.265432 |
| solution-1         |     8.28495  |       1e-06    |   0.612718 |
| solution-2         |     0.670906 |       0.425601 |   0.773888 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.692268 |       1.009    |   0.162784 |
| solution-pl        |     0.675899 |       0.127475 |   0.274022 |
| solution-aron-mark |     0.677822 |       0.127991 |   0.281736 |
| solution-1-flask   |     0.68017  |       1.00897  |   0.793057 |
| solution-2         |     0.671839 |       0.448133 |   5.53716  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.673376 |       1.00907  |   0.700943 |
| solution-aron-mark |     0.672427 |       0.132555 |   0.810275 |
| solution-pl        |     0.676731 |       0.1323   |   0.821429 |
| solution-1-flask   |     0.676677 |       1.00942  |   5.68276  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659154 |       1.00929  |    2.53038 |
| solution-pl        |     0.666821 |       0.168563 |    2.6527  |
| solution-aron-mark |     0.683366 |       0.165931 |    2.66441 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.666106 |       0.291599 |    16.2205 |
| solution-flask     |     0.669609 |       1.00926  |    16.3209 |
| solution-pl        |     0.67048  |       0.287652 |    16.7325 |