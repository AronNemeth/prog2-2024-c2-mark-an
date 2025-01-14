# 2025-01-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.87142  |       1.00917  |   0.104028 |
| solution-pl        |     0.537919 |       0.112178 |   0.189548 |
| solution-aron-mark |     0.543901 |       0.111753 |   0.193114 |
| solution-1-flask   |     5.45865  |       1.12648  |   0.268095 |
| solution-1         |     7.86444  |       1e-06    |   0.727502 |
| solution-2         |     0.544209 |       0.726975 |   1.08016  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534824 |       0.113204 |   0.316473 |
| solution-pl        |     0.533185 |       0.116487 |   0.320578 |
| solution-flask     |     0.550473 |       1.00903  |   0.516239 |
| solution-1-flask   |     0.538655 |       1.0091   |   0.799828 |
| solution-2         |     0.532992 |       0.491181 |   3.96117  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.533193 |       0.119767 |    1.07671 |
| solution-pl        |     0.530519 |       0.119712 |    1.08506 |
| solution-flask     |     0.536232 |       1.00898  |    2.16684 |
| solution-1-flask   |     0.548319 |       1.00896  |    5.75177 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.528835 |       0.151445 |    4.72084 |
| solution-pl        |     0.553988 |       0.148564 |    4.98328 |
| solution-flask     |     0.531695 |       1.00909  |    8.70569 |