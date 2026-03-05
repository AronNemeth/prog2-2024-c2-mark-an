# 2026-03-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.98501  |       1.06321  |   0.107387 |
| solution-pl        |     5.23176  |       0.15158  |   0.24201  |
| solution-aron-mark |     0.475547 |       0.154309 |   0.242511 |
| solution-1-flask   |     0.474378 |       1.00864  |   0.270133 |
| solution-1         |     8.37602  |       2e-06    |   0.807796 |
| solution-2         |     0.465351 |       0.700717 |   1.23546  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.451425 |       0.151118 |   0.366694 |
| solution-aron-mark |     0.457628 |       0.147369 |   0.374327 |
| solution-flask     |     0.454855 |       1.00875  |   0.386412 |
| solution-1-flask   |     0.458121 |       1.00902  |   0.80525  |
| solution-2         |     0.44855  |       0.514241 |   3.3988   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.454707 |        0.15399 |    1.12635 |
| solution-pl        |     0.448794 |        0.15387 |    1.13076 |
| solution-flask     |     0.453431 |        1.00918 |    1.64914 |
| solution-1-flask   |     0.45118  |        1.00904 |    5.59119 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447907 |       0.181648 |    3.9524  |
| solution-pl        |     0.449256 |       0.179488 |    3.97086 |
| solution-flask     |     0.445748 |       1.00895  |    5.28608 |