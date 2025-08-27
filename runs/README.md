# 2025-08-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.485109 |       1.00843  |   0.097153 |
| solution-pl        |     5.80852  |       0.205174 |   0.238339 |
| solution-aron-mark |     0.478402 |       0.161622 |   0.239508 |
| solution-1-flask   |     1.15655  |       1.14034  |   0.270167 |
| solution-1         |     7.61169  |       1e-06    |   0.906128 |
| solution-2         |     0.482124 |       0.726122 |   1.25376  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48001  |       0.156244 |   0.365037 |
| solution-pl        |     0.483613 |       0.159391 |   0.366374 |
| solution-flask     |     0.483675 |       1.00847  |   0.374203 |
| solution-1-flask   |     0.490145 |       1.00832  |   0.812873 |
| solution-2         |     0.48584  |       0.526311 |   4.04662  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481703 |       0.162346 |    1.0849  |
| solution-aron-mark |     0.486377 |       0.160753 |    1.09639 |
| solution-flask     |     0.482227 |       1.00849  |    1.57386 |
| solution-1-flask   |     0.490215 |       1.00801  |    5.79693 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.484037 |       0.194354 |    3.26343 |
| solution-aron-mark |     0.47917  |       0.192256 |    3.27106 |
| solution-flask     |     0.494465 |       1.00833  |    5.16221 |