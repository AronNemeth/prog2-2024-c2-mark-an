# 2024-07-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.08143  |       1.0761   |   0.090622 |
| solution-pl        |     5.6669   |       0.102119 |   0.167408 |
| solution-aron-mark |     0.499691 |       0.100801 |   0.167592 |
| solution-1-flask   |     0.499205 |       1.00883  |   0.265312 |
| solution-1         |     7.7044   |       1e-06    |   0.610611 |
| solution-2         |     0.499713 |       0.557062 |   0.886102 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.502337 |       1.0091   |   0.221107 |
| solution-pl        |     0.498139 |       0.103532 |   0.284488 |
| solution-aron-mark |     0.49601  |       0.103045 |   0.287169 |
| solution-1-flask   |     0.500937 |       1.00911  |   0.77574  |
| solution-2         |     0.492366 |       0.477708 |   4.88592  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.494593 |       1.00897  |   0.911513 |
| solution-aron-mark |     0.499627 |       0.11123  |   0.99097  |
| solution-pl        |     0.502347 |       0.110231 |   0.994089 |
| solution-1-flask   |     0.503871 |       1.00907  |   5.59078  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496749 |       1.00914  |    4.14061 |
| solution-aron-mark |     0.5003   |       0.145067 |    4.17468 |
| solution-pl        |     0.499568 |       0.147716 |    4.24695 |