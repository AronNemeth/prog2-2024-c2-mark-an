# 2026-01-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.08808  |       1.15072  |   0.101592 |
| solution-pl        |     0.484628 |       0.162954 |   0.246484 |
| solution-aron-mark |     0.476148 |       0.158798 |   0.247134 |
| solution-1-flask   |     0.476428 |       1.00839  |   0.270017 |
| solution-1         |     9.01126  |       1e-06    |   0.736316 |
| solution-2         |     4.87996  |       0.721155 |   0.99196  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.473624 |       1.00848  |   0.370816 |
| solution-aron-mark |     0.473894 |       0.164483 |   0.374182 |
| solution-pl        |     0.479538 |       0.164989 |   0.380437 |
| solution-1-flask   |     0.482011 |       1.00847  |   0.793786 |
| solution-2         |     0.478454 |       0.532424 |   3.0305   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469165 |       0.167845 |    1.0937  |
| solution-aron-mark |     0.473309 |       0.167427 |    1.10057 |
| solution-flask     |     0.474227 |       1.00854  |    1.59848 |
| solution-1-flask   |     0.474389 |       1.00841  |    5.55208 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.470474 |       0.196156 |    3.48723 |
| solution-pl        |     0.471481 |       0.19394  |    3.53194 |
| solution-flask     |     0.469316 |       1.00865  |    5.08946 |