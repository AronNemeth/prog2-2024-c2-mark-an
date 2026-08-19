# 2026-08-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.9509   |       1.10208  |   0.105207 |
| solution-aron-mark |     4.59877  |       0.149405 |   0.240224 |
| solution-1-flask   |     0.429169 |       1.00862  |   0.264786 |
| solution-pl        |     0.424481 |       0.152319 |   0.274883 |
| solution-1         |     8.00259  |       1e-06    |   0.658449 |
| solution-2         |     0.424082 |       0.644698 |   1.19046  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428626 |       0.153465 |   0.370738 |
| solution-aron-mark |     0.431144 |       0.152261 |   0.374925 |
| solution-flask     |     0.427072 |       1.0084   |   0.393995 |
| solution-1-flask   |     0.426655 |       1.00825  |   0.823548 |
| solution-2         |     0.421281 |       0.506225 |   4.31997  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.426046 |       0.15991  |    1.11322 |
| solution-pl        |     0.430041 |       0.158985 |    1.11883 |
| solution-flask     |     0.425875 |       1.00831  |    1.63013 |
| solution-1-flask   |     0.428839 |       1.00843  |    5.6824  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431665 |       0.18256  |    3.53159 |
| solution-pl        |     0.421982 |       0.181009 |    3.58362 |
| solution-flask     |     0.421234 |       1.00849  |    5.2806  |