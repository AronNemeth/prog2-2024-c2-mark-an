# 2026-06-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15055  |       1.105    |   0.112329 |
| solution-pl        |     6.30326  |       0.176133 |   0.241296 |
| solution-aron-mark |     0.433017 |       0.152739 |   0.243053 |
| solution-1-flask   |     0.45003  |       1.00846  |   0.273734 |
| solution-1         |     7.55026  |       1e-06    |   0.682886 |
| solution-2         |     0.434872 |       0.730063 |   1.39181  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.437607 |       0.151572 |   0.37572  |
| solution-pl        |     0.443823 |       0.156309 |   0.377489 |
| solution-flask     |     0.436415 |       1.00874  |   0.40116  |
| solution-1-flask   |     0.43859  |       1.00851  |   0.816389 |
| solution-2         |     0.438077 |       0.521197 |   3.33992  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435716 |       0.158325 |    1.14046 |
| solution-pl        |     0.43554  |       0.158582 |    1.14508 |
| solution-flask     |     0.433043 |       1.00862  |    1.69593 |
| solution-1-flask   |     0.449681 |       1.00864  |    5.75664 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.443706 |       0.182853 |    4.11754 |
| solution-pl        |     0.436484 |       0.185788 |    4.12701 |
| solution-flask     |     0.429812 |       1.00854  |    5.49713 |