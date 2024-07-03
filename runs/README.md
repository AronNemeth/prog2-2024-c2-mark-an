# 2024-07-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.513536 |       1.00901  |   0.08991  |
| solution-pl        |     0.500182 |       0.101734 |   0.167302 |
| solution-aron-mark |     5.83612  |       0.100394 |   0.167692 |
| solution-1-flask   |     1.20173  |       1.17968  |   0.256613 |
| solution-1         |     7.86456  |       1e-06    |   0.583645 |
| solution-2         |     0.497125 |       0.510423 |   0.807278 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.519123 |       1.00888  |   0.224982 |
| solution-pl        |     0.50513  |       0.102138 |   0.286572 |
| solution-aron-mark |     0.504675 |       0.105407 |   0.292276 |
| solution-1-flask   |     0.511358 |       1.00908  |   0.779887 |
| solution-2         |     0.503883 |       0.475377 |   2.42202  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.498975 |       1.00886  |   0.913512 |
| solution-aron-mark |     0.502779 |       0.109575 |   0.985785 |
| solution-pl        |     0.504505 |       0.111289 |   0.988085 |
| solution-1-flask   |     0.511434 |       1.00902  |   5.48035  |
| solution-2         |     0.513442 |       0.528288 |  40.1437   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500828 |       1.00927  |    4.28299 |
| solution-pl        |     0.504309 |       0.145584 |    4.42092 |
| solution-aron-mark |     0.504493 |       0.145571 |    4.47713 |