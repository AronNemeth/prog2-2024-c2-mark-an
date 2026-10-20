# 2026-10-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.14188  |       1.11555  |   0.093166 |
| solution-1-flask   |     0.442095 |       1.0089   |   0.225448 |
| solution-aron-mark |     6.72126  |       0.192226 |   0.247791 |
| solution-pl        |     0.42342  |       0.163788 |   0.248368 |
| solution-1         |     7.75033  |       1e-06    |   0.655801 |
| solution-2         |     0.42861  |       0.694183 |   0.965916 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.437575 |       1.00899  |   0.215461 |
| solution-aron-mark |     0.428996 |       0.16645  |   0.378765 |
| solution-pl        |     0.435691 |       0.198812 |   0.380943 |
| solution-1-flask   |     0.458085 |       1.00922  |   0.726603 |
| solution-2         |     0.430127 |       0.512082 |   2.09901  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.423598 |       1.00905  |   0.950626 |
| solution-aron-mark |     0.437698 |       0.176929 |   1.07962  |
| solution-pl        |     0.435028 |       0.174178 |   1.09755  |
| solution-1-flask   |     0.440595 |       1.00947  |   5.59041  |
| solution-2         |     0.434865 |       0.561334 | 164.902    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434522 |       0.207117 |    3.57139 |
| solution-aron-mark |     0.458976 |       0.206487 |    3.57301 |
| solution-flask     |     0.444435 |       1.00924  |    4.2995  |