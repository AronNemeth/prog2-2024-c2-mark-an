# 2024-10-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.31391  |       1.12554  |   0.094797 |
| solution-pl        |     0.571565 |       0.105357 |   0.17868  |
| solution-aron-mark |     1.94266  |       0.103779 |   0.182733 |
| solution-1-flask   |     0.58355  |       1.00806  |   0.258487 |
| solution-1         |     7.96094  |       1e-06    |   0.649958 |
| solution-2         |     4.56015  |       0.566537 |   1.54124  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.595878 |       1.0081   |   0.213957 |
| solution-aron-mark |     0.587976 |       0.107389 |   0.312635 |
| solution-pl        |     0.593153 |       0.105166 |   0.314126 |
| solution-1-flask   |     0.593158 |       1.00846  |   0.796567 |
| solution-2         |     0.585575 |       0.505785 |   2.56549  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.598174 |       1.0083   |   0.952887 |
| solution-aron-mark |     0.614074 |       0.116724 |   1.05478  |
| solution-pl        |     0.602807 |       0.116077 |   1.06169  |
| solution-1-flask   |     0.605844 |       1.0086   |   5.86435  |
| solution-2         |     0.589257 |       0.554753 | 170.898    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.613601 |       1.00861  |    5.25723 |
| solution-pl        |     0.594545 |       0.145269 |    5.34877 |
| solution-aron-mark |     0.606755 |       0.149848 |    5.57565 |