# 2025-04-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.31351  |       1.18052  |   0.084974 |
| solution-pl        |     5.84534  |       0.125134 |   0.192252 |
| solution-aron-mark |     0.47065  |       0.130301 |   0.203333 |
| solution-1-flask   |     0.470213 |       1.00838  |   0.265794 |
| solution-2         |     0.459441 |       0.723935 |   0.757085 |
| solution-1         |     7.87147  |       1e-06    |   0.793976 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.46937  |       0.123526 |   0.295692 |
| solution-flask     |     0.458273 |       1.00903  |   0.295945 |
| solution-aron-mark |     0.472752 |       0.122687 |   0.296262 |
| solution-1-flask   |     0.466855 |       1.00883  |   0.786759 |
| solution-2         |     0.468901 |       0.497694 |   4.15061  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465431 |       0.129905 |   0.902861 |
| solution-pl        |     0.466385 |       0.129203 |   0.918839 |
| solution-flask     |     0.457759 |       1.0087   |   1.24617  |
| solution-1-flask   |     0.468064 |       1.00856  |   5.37209  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.461749 |       0.159038 |    2.834   |
| solution-pl        |     0.470852 |       0.159008 |    2.84112 |
| solution-flask     |     0.459108 |       1.00888  |    4.21882 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469186 |       0.275308 |    15.8643 |
| solution-pl        |     0.462487 |       0.265707 |    16.0162 |