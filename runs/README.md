# 2024-04-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661924 |       1.00886  |   0.06672  |
| solution-pl        |     5.65967  |       0.111328 |   0.16966  |
| solution-aron-mark |     0.651981 |       0.109986 |   0.171438 |
| solution-1-flask   |     1.28164  |       1.13382  |   0.264775 |
| solution-1         |     7.86545  |       1e-06    |   0.853004 |
| solution-2         |     0.66085  |       0.413971 |   1.0244   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668535 |       1.00922  |   0.162284 |
| solution-aron-mark |     0.659544 |       0.119049 |   0.266491 |
| solution-pl        |     0.660769 |       0.119724 |   0.266855 |
| solution-1-flask   |     0.665642 |       1.00877  |   0.789645 |
| solution-2         |     0.655915 |       0.427241 |   3.44608  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.652919 |       1.0086   |   0.712467 |
| solution-aron-mark |     0.689775 |       0.12564  |   0.810278 |
| solution-pl        |     0.663251 |       0.127595 |   0.852035 |
| solution-1-flask   |     0.674959 |       1.00892  |   5.59736  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.659755 |       1.00909  |    2.48716 |
| solution-pl        |     0.65689  |       0.161117 |    2.58017 |
| solution-aron-mark |     0.66382  |       0.161152 |    2.61767 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672013 |       1.00935  |    15.3223 |
| solution-pl        |     0.682195 |       0.285804 |    16.0607 |
| solution-aron-mark |     0.65088  |       0.286532 |    16.5725 |