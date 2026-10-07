# 2026-10-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.35554  |       1.06395  |   0.099331 |
| solution-aron-mark |    19.7415   |       0.198855 |   0.255929 |
| solution-pl        |     0.43031  |       0.167697 |   0.257693 |
| solution-1-flask   |     0.450848 |       1.00868  |   0.259875 |
| solution-1         |     7.73573  |       1e-06    |   0.728834 |
| solution-2         |     0.532043 |       0.689016 |   1.60427  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.437341 |       1.00861  |   0.24187  |
| solution-aron-mark |     0.434669 |       0.18797  |   0.396985 |
| solution-pl        |     0.428865 |       0.171413 |   0.398661 |
| solution-1-flask   |     0.441    |       1.00879  |   0.800544 |
| solution-2         |     0.43432  |       0.519909 |   3.47733  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.429989 |       1.00879  |    1.06037 |
| solution-aron-mark |     0.444106 |       0.173434 |    1.18626 |
| solution-pl        |     0.437511 |       0.173062 |    1.19525 |
| solution-1-flask   |     0.465419 |       1.00883  |    5.58193 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429092 |       0.211675 |    3.63227 |
| solution-aron-mark |     0.441388 |       0.206202 |    3.72438 |
| solution-flask     |     0.43406  |       1.00872  |    4.42969 |