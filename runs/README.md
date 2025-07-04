# 2025-07-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15359  |       1.10965  |   0.099685 |
| solution-aron-mark |     5.48518  |       0.150837 |   0.232618 |
| solution-pl        |     0.480725 |       0.146121 |   0.232854 |
| solution-1-flask   |     0.502066 |       1.00819  |   0.269411 |
| solution-1         |     7.25843  |       1e-06    |   0.620877 |
| solution-2         |     0.497069 |       0.582364 |   1.10933  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492848 |       0.149201 |   0.360011 |
| solution-aron-mark |     0.510621 |       0.1484   |   0.361192 |
| solution-flask     |     0.491005 |       1.00834  |   0.376899 |
| solution-1-flask   |     0.496923 |       1.00849  |   0.799593 |
| solution-2         |     0.489251 |       0.497864 |   1.94     |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.498157 |       0.157895 |    1.06583 |
| solution-pl        |     0.492094 |       0.157518 |    1.09657 |
| solution-flask     |     0.493602 |       1.00815  |    1.5717  |
| solution-1-flask   |     0.501099 |       1.00833  |    5.63578 |
| solution-2         |     0.494838 |       0.550861 |   45.6704  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492144 |       0.189498 |    3.17728 |
| solution-aron-mark |     0.498204 |       0.186687 |    3.20922 |
| solution-flask     |     0.494325 |       1.00828  |    5.01942 |