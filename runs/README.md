# 2024-10-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.51923  |       1.05991  |   0.112542 |
| solution-aron-mark |     0.575736 |       0.111569 |   0.181453 |
| solution-pl        |     6.24775  |       0.115209 |   0.19829  |
| solution-1-flask   |     0.593235 |       1.00949  |   0.264624 |
| solution-1         |     8.41235  |       1e-06    |   0.728292 |
| solution-2         |     0.585556 |       0.598762 |   0.836688 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.584089 |       0.113967 |   0.304644 |
| solution-pl        |     0.585775 |       0.111392 |   0.306811 |
| solution-flask     |     0.585576 |       1.00922  |   0.486855 |
| solution-1-flask   |     0.586319 |       1.00917  |   0.786079 |
| solution-2         |     0.583802 |       0.502095 |   2.49899  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.5861   |       0.119098 |    1.00762 |
| solution-pl        |     0.58254  |       0.119744 |    1.03749 |
| solution-flask     |     0.58105  |       1.00936  |    2.1261  |
| solution-1-flask   |     0.588164 |       1.00943  |    5.42844 |
| solution-2         |     0.582055 |       0.548553 |  164.014   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.586093 |       0.155433 |    4.82118 |
| solution-aron-mark |     0.58101  |       0.150436 |    4.82955 |
| solution-flask     |     0.590049 |       1.00915  |    9.31801 |