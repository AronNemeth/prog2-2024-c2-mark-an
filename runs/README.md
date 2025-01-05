# 2025-01-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.12055  |       1.00867  |   0.101346 |
| solution-aron-mark |     0.53485  |       0.108171 |   0.18452  |
| solution-pl        |     0.525089 |       0.108966 |   0.187335 |
| solution-1-flask   |     5.3876   |       1.06149  |   0.269338 |
| solution-1         |     7.68399  |       1e-06    |   0.792476 |
| solution-2         |     0.536644 |       0.651795 |   1.28654  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.532829 |       0.111624 |   0.314818 |
| solution-aron-mark |     0.531832 |       0.110894 |   0.318649 |
| solution-flask     |     0.532631 |       1.00901  |   0.482994 |
| solution-1-flask   |     0.533739 |       1.01     |   0.806373 |
| solution-2         |     0.528375 |       0.481736 |   2.29982  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.531584 |       0.120054 |    1.06407 |
| solution-aron-mark |     0.53214  |       0.118811 |    1.07157 |
| solution-flask     |     0.527178 |       1.00892  |    2.16237 |
| solution-1-flask   |     0.53336  |       1.00884  |    5.81351 |
| solution-2         |     0.536153 |       0.532922 |   62.6021  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.54341  |       0.146252 |    4.35732 |
| solution-pl        |     0.530321 |       0.14649  |    4.3768  |
| solution-flask     |     0.543741 |       1.0089   |    8.62034 |