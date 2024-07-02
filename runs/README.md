# 2024-07-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.512549 |       1.00913  |   0.094661 |
| solution-pl        |     0.49215  |       0.100783 |   0.165852 |
| solution-aron-mark |     5.86281  |       0.100034 |   0.166564 |
| solution-1-flask   |     1.25711  |       1.05937  |   0.261066 |
| solution-1         |     8.02569  |       1e-06    |   0.586046 |
| solution-2         |     0.491727 |       0.513859 |   0.780975 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.508009 |       1.00896  |   0.222965 |
| solution-aron-mark |     0.497613 |       0.101322 |   0.283991 |
| solution-pl        |     0.495429 |       0.102341 |   0.285784 |
| solution-1-flask   |     0.509316 |       1.0091   |   0.77673  |
| solution-2         |     0.497634 |       0.469207 |   3.52558  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.493498 |       1.00879  |   0.890828 |
| solution-aron-mark |     0.493427 |       0.109509 |   0.992061 |
| solution-pl        |     0.498939 |       0.109395 |   1.02649  |
| solution-1-flask   |     0.503157 |       1.00921  |   5.60638  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.49156  |       1.00923  |    4.10547 |
| solution-aron-mark |     0.506937 |       0.145456 |    4.13894 |
| solution-pl        |     0.498267 |       0.145936 |    4.14519 |