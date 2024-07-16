# 2024-07-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.22783  |       1.04042  |   0.088867 |
| solution-aron-mark |     0.493995 |       0.100491 |   0.166838 |
| solution-pl        |     5.89858  |       0.102068 |   0.169275 |
| solution-1-flask   |     0.500511 |       1.00956  |   0.262692 |
| solution-1         |     7.85262  |       1e-06    |   0.575191 |
| solution-2         |     0.489387 |       0.495359 |   0.907235 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492256 |       1.00908  |   0.224063 |
| solution-pl        |     0.498896 |       0.102421 |   0.282892 |
| solution-aron-mark |     0.491629 |       0.103469 |   0.283401 |
| solution-1-flask   |     0.502659 |       1.00918  |   0.786344 |
| solution-2         |     0.493057 |       0.467544 |   3.80401  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.518378 |       1.00881  |   0.900553 |
| solution-aron-mark |     0.495923 |       0.111527 |   0.986537 |
| solution-pl        |     0.498117 |       0.111552 |   1.00719  |
| solution-1-flask   |     0.498104 |       1.00867  |   5.59263  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.493469 |       1.00908  |    4.1517  |
| solution-aron-mark |     0.491502 |       0.14721  |    4.23667 |
| solution-pl        |     0.494963 |       0.144624 |    4.25901 |