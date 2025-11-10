# 2025-11-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06119  |       1.08931  |   0.098778 |
| solution-aron-mark |     0.470639 |       0.158643 |   0.240325 |
| solution-pl        |     0.469002 |       0.156578 |   0.242857 |
| solution-1-flask   |     0.479888 |       1.00838  |   0.263374 |
| solution-1         |     7.91099  |       1e-06    |   0.595147 |
| solution-2         |     4.89017  |       0.710696 |   1.11342  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.469879 |       0.157627 |   0.365628 |
| solution-pl        |     0.467975 |       0.165335 |   0.368852 |
| solution-flask     |     0.464236 |       1.00822  |   0.38246  |
| solution-1-flask   |     0.475935 |       1.00845  |   0.778772 |
| solution-2         |     0.478639 |       0.530637 |   4.14315  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.480347 |       0.165292 |    1.06428 |
| solution-aron-mark |     0.46865  |       0.163789 |    1.06566 |
| solution-flask     |     0.463919 |       1.0086   |    1.56486 |
| solution-1-flask   |     0.471582 |       1.00846  |    5.49939 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.466276 |       0.193883 |    3.19188 |
| solution-pl        |     0.468202 |       0.193722 |    3.20757 |
| solution-flask     |     0.469052 |       1.00857  |    5.11785 |