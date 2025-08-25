# 2025-08-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.38858  |       1.04999  |   0.099657 |
| solution-pl        |     0.483612 |       0.15395  |   0.241389 |
| solution-aron-mark |     4.40619  |       0.150577 |   0.242755 |
| solution-1-flask   |     0.495053 |       1.00821  |   0.260559 |
| solution-1         |     7.58388  |       1e-06    |   0.608218 |
| solution-2         |     0.486602 |       0.640553 |   1.3356   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488756 |       0.157479 |   0.365827 |
| solution-aron-mark |     0.483776 |       0.153504 |   0.375059 |
| solution-flask     |     0.495241 |       1.00861  |   0.378549 |
| solution-1-flask   |     0.490136 |       1.00844  |   0.810648 |
| solution-2         |     0.48872  |       0.51333  |   2.98753  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.498075 |       0.162329 |    1.08589 |
| solution-aron-mark |     0.505145 |       0.172668 |    1.09986 |
| solution-flask     |     0.505515 |       1.00899  |    1.58034 |
| solution-1-flask   |     0.492459 |       1.00844  |    5.64721 |
| solution-2         |     0.513506 |       0.587943 |   40.3991  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48191  |       0.190643 |    3.20525 |
| solution-pl        |     0.485313 |       0.194123 |    3.31011 |
| solution-flask     |     0.484188 |       1.00864  |    5.03005 |