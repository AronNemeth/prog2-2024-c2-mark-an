# 2024-05-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.38231  |       1.06079  |   0.083957 |
| solution-aron-mark |     5.70671  |       0.120377 |   0.176471 |
| solution-pl        |     0.66193  |       0.120689 |   0.176673 |
| solution-1-flask   |     0.69663  |       1.00941  |   0.265215 |
| solution-1         |     7.8241   |       1e-06    |   0.591315 |
| solution-2         |     0.654177 |       0.427938 |   1.21569  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658678 |       1.00904  |   0.160652 |
| solution-pl        |     0.660231 |       0.125271 |   0.268168 |
| solution-aron-mark |     0.666571 |       0.124353 |   0.278165 |
| solution-1-flask   |     0.66618  |       1.00891  |   0.793082 |
| solution-2         |     0.662717 |       0.423965 |   2.73407  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689258 |       1.00916  |   0.675689 |
| solution-aron-mark |     0.659897 |       0.131116 |   0.811325 |
| solution-pl        |     0.696568 |       0.136615 |   0.812712 |
| solution-1-flask   |     0.692469 |       1.00935  |   5.63418  |
| solution-2         |     0.680739 |       0.48051  | 292.444    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.658969 |       1.00875  |    2.42004 |
| solution-aron-mark |     0.662661 |       0.168223 |    2.56365 |
| solution-pl        |     0.661032 |       0.167505 |    2.5792  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.665255 |       0.291894 |    15.4791 |
| solution-pl        |     0.655173 |       0.292537 |    15.6611 |
| solution-flask     |     0.658509 |       1.0088   |    15.8552 |