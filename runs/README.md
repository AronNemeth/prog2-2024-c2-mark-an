# 2025-12-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.79552  |       1.06487  |   0.103303 |
| solution-pl        |     0.478438 |       0.166205 |   0.250725 |
| solution-aron-mark |     0.479508 |       0.162763 |   0.250883 |
| solution-1-flask   |     0.490903 |       1.00843  |   0.293929 |
| solution-1         |     7.74764  |       1e-06    |   0.693728 |
| solution-2         |     5.19813  |       0.631441 |   1.30064  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480407 |       0.165454 |   0.379277 |
| solution-aron-mark |     0.477002 |       0.165483 |   0.380697 |
| solution-flask     |     0.479709 |       1.0087   |   0.386974 |
| solution-1-flask   |     0.482434 |       1.00865  |   0.803084 |
| solution-2         |     0.482913 |       0.527505 |   2.01365  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.485311 |       0.176209 |    1.08975 |
| solution-aron-mark |     0.488298 |       0.174692 |    1.08985 |
| solution-flask     |     0.490425 |       1.00855  |    1.59409 |
| solution-1-flask   |     0.49216  |       1.0086   |    5.49545 |
| solution-2         |     0.478656 |       0.578277 |  298.879   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481894 |       0.19653  |    3.73822 |
| solution-aron-mark |     0.491486 |       0.199479 |    3.79357 |
| solution-flask     |     0.489284 |       1.00863  |    5.16869 |