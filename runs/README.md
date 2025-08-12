# 2025-08-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.73356  |       1.11209  |   0.099624 |
| solution-pl        |     0.475679 |       0.156495 |   0.236144 |
| solution-aron-mark |     4.70152  |       0.148724 |   0.24185  |
| solution-1-flask   |     0.480335 |       1.00817  |   0.26563  |
| solution-1         |     7.65516  |       1e-06    |   0.677077 |
| solution-2         |     0.47509  |       0.615172 |   0.736813 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476387 |       0.152468 |   0.361241 |
| solution-aron-mark |     0.474284 |       0.152043 |   0.363317 |
| solution-flask     |     0.473832 |       1.00829  |   0.375641 |
| solution-1-flask   |     0.478034 |       1.00822  |   0.800221 |
| solution-2         |     0.473151 |       0.497338 |   4.56708  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473604 |       0.159553 |    1.07211 |
| solution-aron-mark |     0.475969 |       0.158144 |    1.07456 |
| solution-flask     |     0.477623 |       1.00834  |    1.56531 |
| solution-1-flask   |     0.478684 |       1.0081   |    5.60996 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472087 |       0.190611 |    3.1626  |
| solution-aron-mark |     0.473096 |       0.188923 |    3.16461 |
| solution-flask     |     0.473504 |       1.00821  |    5.06496 |