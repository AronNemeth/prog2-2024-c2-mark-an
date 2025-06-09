# 2025-06-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.86273  |       1.00848  |   0.103697 |
| solution-pl        |     0.540025 |       0.161195 |   0.241942 |
| solution-aron-mark |     0.518233 |       0.155257 |   0.243044 |
| solution-1-flask   |     5.42661  |       1.05209  |   0.266522 |
| solution-1         |     8.22819  |       2e-06    |   0.811754 |
| solution-2         |     0.520952 |       0.753829 |   1.23115  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.525417 |       0.155211 |   0.367476 |
| solution-pl        |     0.531337 |       0.158583 |   0.37129  |
| solution-flask     |     0.536894 |       1.00908  |   0.376911 |
| solution-1-flask   |     0.533055 |       1.00884  |   0.791755 |
| solution-2         |     0.522194 |       0.545169 |   7.56259  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.539615 |       0.163456 |    1.07655 |
| solution-aron-mark |     0.531126 |       0.163096 |    1.09973 |
| solution-flask     |     0.522953 |       1.00895  |    1.58759 |
| solution-1-flask   |     0.527822 |       1.00897  |    5.46751 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.539365 |       0.196403 |    3.40102 |
| solution-pl        |     0.529138 |       0.19259  |    3.43274 |
| solution-flask     |     0.522738 |       1.00966  |    5.26347 |