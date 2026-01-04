# 2026-01-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.60863  |       1.05973  |   0.105329 |
| solution-aron-mark |     0.469259 |       0.158215 |   0.239658 |
| solution-pl        |     0.463147 |       0.160426 |   0.240841 |
| solution-1-flask   |     0.467885 |       1.00814  |   0.269232 |
| solution-1         |     7.41285  |       1e-06    |   0.696549 |
| solution-2         |     4.5521   |       0.641116 |   0.797275 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469201 |       0.160985 |   0.362676 |
| solution-flask     |     0.466456 |       1.00818  |   0.367237 |
| solution-aron-mark |     0.481986 |       0.168268 |   0.37112  |
| solution-1-flask   |     0.494206 |       1.00831  |   0.81034  |
| solution-2         |     0.472846 |       0.510493 |   4.56368  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.46663  |       0.166945 |    1.06773 |
| solution-pl        |     0.467064 |       0.16708  |    1.07334 |
| solution-flask     |     0.463351 |       1.00834  |    1.54394 |
| solution-1-flask   |     0.471014 |       1.00838  |    5.56406 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.467711 |       0.192007 |    3.43498 |
| solution-pl        |     0.466048 |       0.189186 |    3.48903 |
| solution-flask     |     0.468505 |       1.00854  |    5.01631 |