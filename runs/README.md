# 2024-04-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.681913 |       1.00912  |   0.065782 |
| solution-aron-mark |     0.678846 |       0.112029 |   0.16835  |
| solution-pl        |     5.9945   |       0.115599 |   0.172128 |
| solution-1-flask   |     1.47075  |       1.06276  |   0.288798 |
| solution-1         |     9.03074  |       1e-06    |   0.719883 |
| solution-2         |     0.671343 |       0.431639 |   0.754224 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672514 |       1.00876  |   0.171973 |
| solution-aron-mark |     0.680375 |       0.116535 |   0.261928 |
| solution-pl        |     0.682847 |       0.119484 |   0.262446 |
| solution-1-flask   |     0.676535 |       1.0089   |   0.798362 |
| solution-2         |     0.679671 |       0.431789 |   4.4129   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.666239 |       0.132208 |   0.81281  |
| solution-pl        |     0.668112 |       0.122897 |   0.817847 |
| solution-flask     |     0.665964 |       1.00915  |   0.906705 |
| solution-1-flask   |     0.689853 |       1.00906  |   5.56732  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.669392 |       0.154914 |    3.22025 |
| solution-aron-mark |     0.665036 |       0.15516  |    3.2575  |
| solution-flask     |     0.667438 |       1.00938  |    5.1628  |