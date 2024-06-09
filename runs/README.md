# 2024-06-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.66337  |       1.07142  |   0.078231 |
| solution-aron-mark |     6.68834  |       0.10805  |   0.166841 |
| solution-pl        |     0.688898 |       0.107281 |   0.168006 |
| solution-1-flask   |     0.704748 |       1.00943  |   0.272598 |
| solution-1         |     8.6092   |       2e-06    |   0.618847 |
| solution-2         |     0.684733 |       0.442439 |   0.956401 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.698276 |       1.00949  |   0.161153 |
| solution-pl        |     0.692224 |       0.111067 |   0.263826 |
| solution-aron-mark |     0.701188 |       0.109271 |   0.271422 |
| solution-1-flask   |     0.715583 |       1.00918  |   0.794928 |
| solution-2         |     0.698978 |       0.452934 |   2.60861  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.686981 |       1.00937  |   0.713672 |
| solution-aron-mark |     0.716388 |       0.119273 |   0.813101 |
| solution-pl        |     0.69519  |       0.116185 |   0.818181 |
| solution-1-flask   |     0.705579 |       1.00919  |   5.60585  |
| solution-2         |     0.708762 |       0.529355 |  45.2969   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.691825 |       1.00941  |    2.66892 |
| solution-pl        |     0.693029 |       0.15195  |    2.71915 |
| solution-aron-mark |     0.706623 |       0.151883 |    2.75945 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.692454 |       1.00949  |    19.3012 |
| solution-pl        |     0.696802 |       0.286489 |    24.6672 |
| solution-aron-mark |     0.692616 |       0.281348 |    24.852  |