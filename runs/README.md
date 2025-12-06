# 2025-12-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.75519  |       1.09019  |   0.099019 |
| solution-aron-mark |     0.47063  |       0.156109 |   0.243542 |
| solution-pl        |     0.472115 |       0.157916 |   0.244495 |
| solution-1-flask   |     0.481624 |       1.0082   |   0.268519 |
| solution-1         |     8.35704  |       1e-06    |   0.758636 |
| solution-2         |     4.99571  |       0.731503 |   1.19745  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488267 |       0.161531 |   0.368868 |
| solution-aron-mark |     0.473365 |       0.160192 |   0.371084 |
| solution-flask     |     0.471626 |       1.0083   |   0.37948  |
| solution-1-flask   |     0.473596 |       1.0082   |   0.798519 |
| solution-2         |     0.471905 |       0.511517 |   3.39628  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.473409 |       0.168154 |    1.06619 |
| solution-aron-mark |     0.477051 |       0.165498 |    1.06866 |
| solution-flask     |     0.475298 |       1.00842  |    1.6017  |
| solution-1-flask   |     0.478737 |       1.00851  |    5.52412 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472812 |       0.19718  |    3.21786 |
| solution-aron-mark |     0.473058 |       0.193784 |    3.22986 |
| solution-flask     |     0.470115 |       1.00835  |    5.09752 |