# 2026-01-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.69374  |       1.06698  |   0.105572 |
| solution-aron-mark |     0.471896 |       0.165531 |   0.25007  |
| solution-pl        |     0.477352 |       0.163341 |   0.253815 |
| solution-1-flask   |     0.479229 |       1.0084   |   0.267761 |
| solution-1         |     7.48775  |       1e-06    |   0.687639 |
| solution-2         |     4.46942  |       0.612231 |   1.28497  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.475655 |       0.163269 |   0.376913 |
| solution-aron-mark |     0.478464 |       0.166916 |   0.385161 |
| solution-flask     |     0.480658 |       1.00856  |   0.394019 |
| solution-1-flask   |     0.481847 |       1.0086   |   0.798229 |
| solution-2         |     0.521838 |       0.503248 |   2.92332  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472115 |       0.173747 |    1.08969 |
| solution-aron-mark |     0.473598 |       0.171221 |    1.09684 |
| solution-flask     |     0.471322 |       1.00977  |    1.60819 |
| solution-1-flask   |     0.47816  |       1.00903  |    5.60563 |
| solution-2         |     0.468608 |       0.573994 |   32.961   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477217 |       0.19393  |    3.58876 |
| solution-aron-mark |     0.47334  |       0.192754 |    3.61019 |
| solution-flask     |     0.476108 |       1.00873  |    5.13488 |