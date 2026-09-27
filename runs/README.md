# 2026-09-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.67266  |       1.12704  |   0.116069 |
| solution-pl        |     0.469176 |       0.164284 |   0.252196 |
| solution-aron-mark |     6.71161  |       0.190121 |   0.25729  |
| solution-1-flask   |     0.458725 |       1.00865  |   0.276737 |
| solution-1         |     8.20983  |       1e-06    |   0.678498 |
| solution-2         |     0.44457  |       0.589803 |   0.865565 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.470839 |       0.165823 |   0.396908 |
| solution-aron-mark |     0.463197 |       0.167708 |   0.404228 |
| solution-flask     |     0.474383 |       1.00909  |   0.41086  |
| solution-1-flask   |     0.465655 |       1.00905  |   0.849919 |
| solution-2         |     0.455643 |       0.565466 |   2.63877  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.46344  |       0.170515 |    1.15325 |
| solution-pl        |     0.469596 |       0.170397 |    1.16946 |
| solution-flask     |     0.465589 |       1.00903  |    1.72923 |
| solution-1-flask   |     0.467034 |       1.00879  |    5.92207 |
| solution-2         |     0.470778 |       0.614362 |   27.5627  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.449721 |       0.194108 |    3.74938 |
| solution-pl        |     0.432318 |       0.189271 |    3.81199 |
| solution-flask     |     0.458595 |       1.0086   |    5.62388 |