# 2025-05-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.478482 |       1.00869  |   0.083637 |
| solution-aron-mark |     1.89863  |       0.132636 |   0.200932 |
| solution-pl        |     0.497048 |       0.123431 |   0.201108 |
| solution-1-flask   |     1.15058  |       1.05506  |   0.274735 |
| solution-1         |     8.90823  |       1e-06    |   0.753576 |
| solution-2         |     5.24041  |       0.741125 |   0.957437 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.512005 |       1.00928  |   0.301013 |
| solution-pl        |     0.526685 |       0.140586 |   0.305044 |
| solution-aron-mark |     0.556393 |       0.135323 |   0.313429 |
| solution-1-flask   |     0.505181 |       1.00905  |   0.811277 |
| solution-2         |     0.483157 |       0.543    |   1.91419  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.541369 |       0.143968 |   0.920717 |
| solution-pl        |     0.52351  |       0.149126 |   0.935405 |
| solution-flask     |     0.512882 |       1.009    |   1.28732  |
| solution-1-flask   |     0.529084 |       1.01016  |   5.85692  |
| solution-2         |     0.528832 |       0.599713 |  36.775    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.524053 |       0.170391 |    3.23487 |
| solution-aron-mark |     0.500166 |       0.172993 |    3.27976 |
| solution-flask     |     0.516994 |       1.00911  |    4.67241 |