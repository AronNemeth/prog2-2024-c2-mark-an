# 2025-10-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.48776  |       1.13194  |   0.103477 |
| solution-aron-mark |     0.491486 |       0.156778 |   0.242126 |
| solution-pl        |     0.497897 |       0.156641 |   0.242856 |
| solution-1-flask   |     0.494046 |       1.00823  |   0.264582 |
| solution-1         |     7.77465  |       1e-06    |   0.712629 |
| solution-2         |     4.74699  |       0.809981 |   1.5072   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504936 |       0.164157 |   0.367832 |
| solution-aron-mark |     0.490393 |       0.164456 |   0.372581 |
| solution-flask     |     0.491421 |       1.00957  |   0.379253 |
| solution-1-flask   |     0.502919 |       1.00848  |   0.809979 |
| solution-2         |     0.488303 |       0.510877 |   4.03855  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.495451 |       0.166703 |    1.08026 |
| solution-aron-mark |     0.49054  |       0.166055 |    1.09882 |
| solution-flask     |     0.49019  |       1.0085   |    1.57956 |
| solution-1-flask   |     0.495708 |       1.00848  |    5.64164 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48782  |       0.198605 |    3.26735 |
| solution-pl        |     0.487743 |       0.203433 |    3.32954 |
| solution-flask     |     0.496765 |       1.0086   |    5.12336 |