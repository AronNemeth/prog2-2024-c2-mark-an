# 2025-05-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.66256  |       1.15435  |   0.121652 |
| solution-pl        |     6.32067  |       0.120244 |   0.19049  |
| solution-aron-mark |     0.951559 |       0.119193 |   0.191272 |
| solution-1-flask   |     0.968261 |       1.00825  |   0.271444 |
| solution-1         |     8.20471  |       1e-06    |   0.985629 |
| solution-2         |     0.950738 |       0.875622 |   1.34388  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.949969 |       1.00826  |   0.286126 |
| solution-pl        |     0.950619 |       0.121021 |   0.286183 |
| solution-aron-mark |     0.948384 |       0.121029 |   0.297115 |
| solution-1-flask   |     0.795513 |       1.00826  |   0.81527  |
| solution-2         |     0.946928 |       0.493952 |  11.6998   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.463086 |       0.12791  |   0.879564 |
| solution-aron-mark |     0.467044 |       0.131304 |   0.887861 |
| solution-flask     |     0.463677 |       1.0082   |   1.23746  |
| solution-1-flask   |     0.46755  |       1.00803  |   5.35436  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464952 |       0.159144 |    2.82066 |
| solution-aron-mark |     0.475788 |       0.163617 |    2.85258 |
| solution-flask     |     0.469222 |       1.00863  |    4.23536 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475922 |       0.270056 |    15.6459 |
| solution-pl        |     0.473147 |       0.271736 |    16.1596 |