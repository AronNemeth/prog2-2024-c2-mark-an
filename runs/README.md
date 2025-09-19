# 2025-09-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.487915 |       1.00812  |   0.099923 |
| solution-pl        |     5.66575  |       0.279556 |   0.236184 |
| solution-aron-mark |     0.492823 |       0.151187 |   0.239628 |
| solution-1-flask   |     1.35718  |       1.04184  |   0.263915 |
| solution-1         |     7.50119  |       1e-06    |   0.68012  |
| solution-2         |     0.479134 |       0.645663 |   0.872265 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47595  |       0.159708 |   0.362749 |
| solution-pl        |     0.480737 |       0.153777 |   0.364319 |
| solution-flask     |     0.47847  |       1.00839  |   0.378506 |
| solution-1-flask   |     0.486135 |       1.00822  |   0.805819 |
| solution-2         |     0.478417 |       0.503377 |   2.86621  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475881 |       0.160118 |    1.05851 |
| solution-pl        |     0.483233 |       0.160655 |    1.08217 |
| solution-flask     |     0.48158  |       1.00858  |    1.57116 |
| solution-1-flask   |     0.494648 |       1.00843  |    5.66677 |
| solution-2         |     0.480281 |       0.550534 |  175.37    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482845 |       0.191211 |    3.23877 |
| solution-aron-mark |     0.479153 |       0.192095 |    3.2493  |
| solution-flask     |     0.47728  |       1.00854  |    5.10657 |