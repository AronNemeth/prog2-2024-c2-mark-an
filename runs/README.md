# 2026-05-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.14834  |       1.09931  |   0.106575 |
| solution-1-flask   |     0.444806 |       1.00883  |   0.22287  |
| solution-pl        |     0.453981 |       0.155049 |   0.235548 |
| solution-aron-mark |     6.80921  |       0.286604 |   0.249315 |
| solution-1         |     7.83244  |       1e-06    |   0.64149  |
| solution-2         |     0.450881 |       0.788566 |   1.32096  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.443852 |       0.155623 |   0.361666 |
| solution-aron-mark |     0.453155 |       0.162945 |   0.364913 |
| solution-flask     |     0.446115 |       1.00899  |   0.410241 |
| solution-1-flask   |     0.450333 |       1.00899  |   0.724353 |
| solution-2         |     0.44722  |       0.548759 |   1.75771  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.445186 |       0.162192 |    1.05551 |
| solution-pl        |     0.43925  |       0.161994 |    1.06907 |
| solution-flask     |     0.446399 |       1.00902  |    1.71586 |
| solution-1-flask   |     0.448965 |       1.00898  |    5.57777 |
| solution-2         |     0.450553 |       0.596432 |  307.817   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.442431 |       0.188409 |    3.98377 |
| solution-pl        |     0.449308 |       0.188282 |    3.99054 |
| solution-flask     |     0.436942 |       1.00915  |    5.59119 |