# 2024-03-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.5441   |       1.13507  |   0.066595 |
| solution-pl        |     0.63188  |       0.109681 |   0.1634   |
| solution-aron-mark |     0.631883 |       0.10764  |   0.163793 |
| solution-1-flask   |     0.64739  |       1.00889  |   0.270092 |
| solution-1         |     8.04858  |       1e-06    |   0.758255 |
| solution-2         |     4.50324  |       0.561971 |   0.898395 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.632021 |       1.00865  |   0.173155 |
| solution-pl        |     0.639717 |       0.1152   |   0.25502  |
| solution-aron-mark |     0.634596 |       0.114408 |   0.256974 |
| solution-1-flask   |     0.639826 |       1.00869  |   0.788543 |
| solution-2         |     0.632051 |       0.441599 |   4.63484  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.638807 |       0.119482 |   0.808827 |
| solution-pl        |     0.631154 |       0.120512 |   0.80973  |
| solution-flask     |     0.635643 |       1.00875  |   0.941022 |
| solution-1-flask   |     0.642879 |       1.00927  |   5.5786   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.64007  |        0.1537  |    3.17798 |
| solution-pl        |     0.631783 |        0.1527  |    3.18956 |
| solution-flask     |     0.635161 |        1.00923 |    5.27399 |