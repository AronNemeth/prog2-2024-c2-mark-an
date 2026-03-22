# 2026-03-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.71405  |       1.07436  |   0.108017 |
| solution-pl        |     4.58567  |       0.155044 |   0.248679 |
| solution-aron-mark |     0.477112 |       0.158103 |   0.250241 |
| solution-1-flask   |     0.480468 |       1.00893  |   0.269041 |
| solution-1         |     7.77542  |       2e-06    |   0.776046 |
| solution-2         |     0.476146 |       0.744927 |   1.0631   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48634  |       0.159488 |   0.38253  |
| solution-aron-mark |     0.477743 |       0.169448 |   0.383619 |
| solution-flask     |     0.481365 |       1.00989  |   0.402481 |
| solution-1-flask   |     0.485116 |       1.00916  |   0.829244 |
| solution-2         |     0.478082 |       0.555084 |   2.38753  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.49496  |       0.165742 |    1.13577 |
| solution-pl        |     0.495622 |       0.167116 |    1.13633 |
| solution-flask     |     0.477212 |       1.00914  |    1.66077 |
| solution-1-flask   |     0.490487 |       1.00896  |    5.86881 |
| solution-2         |     0.477243 |       0.610795 |   39.7672  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476455 |       0.189594 |    4.14614 |
| solution-aron-mark |     0.489835 |       0.190808 |    4.16569 |
| solution-flask     |     0.4735   |       1.00929  |    5.48988 |