# 2026-10-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30826  |       1.05158  |   0.101625 |
| solution-pl        |     0.442644 |       0.169331 |   0.257544 |
| solution-aron-mark |     6.46448  |       0.20136  |   0.263407 |
| solution-1-flask   |     0.453907 |       1.0084   |   0.265361 |
| solution-1         |     8.69606  |       1e-06    |   0.787664 |
| solution-2         |     0.441248 |       0.763149 |   1.16794  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.460025 |       1.00866  |   0.244013 |
| solution-aron-mark |     0.453642 |       0.176682 |   0.403694 |
| solution-pl        |     0.452671 |       0.175398 |   0.408933 |
| solution-1-flask   |     0.4603   |       1.00861  |   0.792587 |
| solution-2         |     0.454847 |       0.550268 |   3.47472  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.429282 |       1.00865  |    1.04905 |
| solution-pl        |     0.436688 |       0.174416 |    1.18449 |
| solution-aron-mark |     0.451346 |       0.182943 |    1.19064 |
| solution-1-flask   |     0.437567 |       1.00862  |    5.57495 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.437182 |       0.206796 |    3.71169 |
| solution-pl        |     0.44626  |       0.206587 |    3.71439 |
| solution-flask     |     0.428768 |       1.00921  |    4.51103 |