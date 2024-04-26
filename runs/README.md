# 2024-04-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.678497 |       1.00883  |   0.081061 |
| solution-aron-mark |     0.689639 |       0.11495  |   0.177059 |
| solution-pl        |     7.68156  |       0.114732 |   0.178139 |
| solution-1-flask   |     1.94257  |       1.06401  |   0.26611  |
| solution-1         |     9.09034  |       2e-06    |   0.633231 |
| solution-2         |     0.691142 |       0.436433 |   1.06344  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.691863 |       1.00919  |   0.165142 |
| solution-aron-mark |     0.70543  |       0.12406  |   0.279782 |
| solution-pl        |     0.692667 |       0.124383 |   0.283441 |
| solution-1-flask   |     0.687968 |       1.0091   |   0.785589 |
| solution-2         |     0.679088 |       0.449978 |   3.22148  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.678697 |       1.0096   |   0.69887  |
| solution-pl        |     0.711078 |       0.128093 |   0.824323 |
| solution-aron-mark |     0.685783 |       0.126298 |   0.827525 |
| solution-1-flask   |     0.698259 |       1.0094   |   5.6661   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.687033 |        1.00924 |    2.67726 |
| solution-aron-mark |     0.676677 |        0.1643  |    2.69476 |
| solution-pl        |     0.703848 |        0.16394 |    2.70014 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.687964 |       0.292564 |    16.8878 |
| solution-flask     |     0.676761 |       1.00911  |    17.2242 |
| solution-pl        |     0.688375 |       0.294209 |    18.508  |