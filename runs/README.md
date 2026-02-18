# 2026-02-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.32185  |       1.05593  |   0.098669 |
| solution-aron-mark |     0.401908 |       0.131449 |   0.20442  |
| solution-pl        |     5.29734  |       0.129589 |   0.205771 |
| solution-1-flask   |     0.401106 |       1.00631  |   0.233564 |
| solution-1         |     9.35125  |       2e-06    |   0.623888 |
| solution-2         |     0.396407 |       0.572347 |   0.788527 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.408149 |       0.134179 |   0.312012 |
| solution-pl        |     0.404067 |       0.132645 |   0.317778 |
| solution-flask     |     0.404527 |       1.00663  |   0.403577 |
| solution-1-flask   |     0.431581 |       1.00689  |   0.699212 |
| solution-2         |     0.401851 |       0.484284 |  13.0679   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.401016 |       0.140693 |   0.983298 |
| solution-aron-mark |     0.399567 |       0.138299 |   1.0073   |
| solution-flask     |     0.401183 |       1.00646  |   1.76041  |
| solution-1-flask   |     0.410518 |       1.00688  |   5.25166  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.401499 |       0.167395 |    4.37322 |
| solution-pl        |     0.396509 |       0.167872 |    4.52721 |
| solution-flask     |     0.401709 |       1.00659  |    5.54369 |