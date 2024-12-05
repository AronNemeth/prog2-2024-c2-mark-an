# 2024-12-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.32317  |       1.108    |   0.112465 |
| solution-aron-mark |     0.560718 |       0.109479 |   0.18027  |
| solution-pl        |     5.88011  |       0.112715 |   0.198957 |
| solution-1-flask   |     0.568643 |       1.00919  |   0.262669 |
| solution-1         |     7.74362  |       2e-06    |   0.746267 |
| solution-2         |     0.558465 |       0.644726 |   0.836045 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.563916 |       0.109061 |   0.303126 |
| solution-pl        |     0.56035  |       0.117044 |   0.316073 |
| solution-flask     |     0.56851  |       1.00916  |   0.536751 |
| solution-1-flask   |     0.567974 |       1.00892  |   0.781301 |
| solution-2         |     0.561731 |       0.477482 |   2.25285  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.593972 |       0.117362 |    1.03605 |
| solution-pl        |     0.567492 |       0.117634 |    1.05014 |
| solution-flask     |     0.574141 |       1.00893  |    2.24968 |
| solution-1-flask   |     0.581216 |       1.00929  |    5.50213 |
| solution-2         |     0.570017 |       0.526558 |  422.239   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.591207 |       0.153527 |    4.63815 |
| solution-aron-mark |     0.579124 |       0.152554 |    4.70114 |
| solution-flask     |     0.587684 |       1.00963  |    9.10015 |