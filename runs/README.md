# 2025-10-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.85311  |       1.06084  |   0.105455 |
| solution-aron-mark |     0.524033 |       0.171221 |   0.252159 |
| solution-pl        |     0.534531 |       0.18744  |   0.271381 |
| solution-1-flask   |     0.519024 |       1.0086   |   0.277097 |
| solution-1         |     7.90306  |       1e-06    |   0.778943 |
| solution-2         |     4.56992  |       0.844781 |   0.885339 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506737 |       0.161654 |   0.375805 |
| solution-flask     |     0.507805 |       1.00845  |   0.37968  |
| solution-pl        |     0.500784 |       0.163445 |   0.388166 |
| solution-1-flask   |     0.501042 |       1.00867  |   0.817126 |
| solution-2         |     0.57262  |       0.546399 |   5.13552  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505182 |       0.169056 |    1.08334 |
| solution-pl        |     0.505372 |       0.170496 |    1.09225 |
| solution-flask     |     0.520689 |       1.00878  |    1.63731 |
| solution-1-flask   |     0.497061 |       1.00859  |    5.77676 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.505445 |       0.20898  |    3.38688 |
| solution-aron-mark |     0.514752 |       0.203719 |    3.40505 |
| solution-flask     |     0.508113 |       1.00865  |    5.33142 |