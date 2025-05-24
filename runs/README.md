# 2025-05-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.76748  |       1.00817  |   0.098098 |
| solution-aron-mark |     0.495912 |       0.146428 |   0.227597 |
| solution-pl        |     0.500244 |       0.147045 |   0.227769 |
| solution-1-flask   |     4.86765  |       1.061    |   0.292974 |
| solution-1         |     7.17846  |       1e-06    |   0.593721 |
| solution-2         |     0.497055 |       0.553811 |   0.917053 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496293 |       0.147351 |   0.350143 |
| solution-pl        |     0.492648 |       0.147252 |   0.350256 |
| solution-flask     |     0.501924 |       1.00859  |   0.368178 |
| solution-1-flask   |     0.513728 |       1.01133  |   0.775991 |
| solution-2         |     0.494269 |       0.499019 |  11.9839   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494492 |       0.156814 |    1.06313 |
| solution-pl        |     0.493745 |       0.156886 |    1.07021 |
| solution-flask     |     0.4965   |       1.00812  |    1.55377 |
| solution-1-flask   |     0.502124 |       1.00859  |    5.44247 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.514798 |       0.186322 |    3.17118 |
| solution-pl        |     0.494852 |       0.185391 |    3.17299 |
| solution-flask     |     0.495705 |       1.00857  |    4.97977 |