# 2026-05-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.57678  |       1.06367  |   0.131431 |
| solution-aron-mark |     4.33054  |       0.146173 |   0.235567 |
| solution-pl        |     0.412595 |       0.14449  |   0.238172 |
| solution-1-flask   |     0.418537 |       1.00818  |   0.266843 |
| solution-1         |     7.31819  |       1e-06    |   0.593    |
| solution-2         |     0.409073 |       0.564058 |   0.748687 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.413677 |       0.146071 |   0.362166 |
| solution-aron-mark |     0.412334 |       0.147055 |   0.365407 |
| solution-flask     |     0.409198 |       1.00822  |   0.393576 |
| solution-1-flask   |     0.417335 |       1.00829  |   0.795221 |
| solution-2         |     0.409337 |       0.507911 |   2.62377  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.411489 |       0.15275  |    1.09849 |
| solution-pl        |     0.415337 |       0.151885 |    1.10893 |
| solution-flask     |     0.409104 |       1.00835  |    1.64058 |
| solution-1-flask   |     0.415808 |       1.00827  |    5.58826 |
| solution-2         |     0.412085 |       0.562696 |  179.741   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.41122  |       0.177379 |    3.7434  |
| solution-aron-mark |     0.408735 |       0.175114 |    3.75447 |
| solution-flask     |     0.414833 |       1.00855  |    5.21712 |