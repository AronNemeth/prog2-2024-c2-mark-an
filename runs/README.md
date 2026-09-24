# 2026-09-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.27534  |       1.09572  |   0.111146 |
| solution-aron-mark |     6.35067  |       0.160362 |   0.244862 |
| solution-pl        |     0.444163 |       0.16125  |   0.250904 |
| solution-1-flask   |     0.440831 |       1.00838  |   0.280395 |
| solution-1         |     7.89345  |       1e-06    |   0.674414 |
| solution-2         |     0.429691 |       0.621346 |   1.18002  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438725 |       0.163428 |   0.389914 |
| solution-pl        |     0.44781  |       0.160346 |   0.396192 |
| solution-flask     |     0.449921 |       1.00867  |   0.401044 |
| solution-1-flask   |     0.448143 |       1.00871  |   0.832506 |
| solution-2         |     0.45289  |       0.529594 |   3.41493  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.43909  |       0.162585 |    1.1647  |
| solution-aron-mark |     0.444089 |       0.163099 |    1.20417 |
| solution-flask     |     0.436212 |       1.00882  |    1.70289 |
| solution-1-flask   |     0.442732 |       1.00862  |    5.83789 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429384 |       0.186644 |    3.64565 |
| solution-aron-mark |     0.444036 |       0.184381 |    3.65089 |
| solution-flask     |     0.435582 |       1.00862  |    5.43743 |