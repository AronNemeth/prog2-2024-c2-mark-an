# 2026-04-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.40779  |       1.09041  |   0.092965 |
| solution-aron-mark |     4.44542  |       0.146946 |   0.217319 |
| solution-pl        |     0.406212 |       0.146235 |   0.220769 |
| solution-1-flask   |     0.408789 |       1.00857  |   0.22789  |
| solution-1         |     7.95261  |       1e-06    |   0.56073  |
| solution-2         |     0.40677  |       0.525793 |   0.790138 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.408872 |       0.14739  |   0.335765 |
| solution-aron-mark |     0.41372  |       0.148652 |   0.337534 |
| solution-flask     |     0.407311 |       1.00864  |   0.382018 |
| solution-1-flask   |     0.41581  |       1.00862  |   0.715243 |
| solution-2         |     0.403522 |       0.493082 |   3.18555  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.405893 |       0.154111 |   0.979712 |
| solution-aron-mark |     0.408566 |       0.152883 |   0.983144 |
| solution-flask     |     0.405484 |       1.00889  |   1.52521  |
| solution-1-flask   |     0.415745 |       1.00884  |   5.52145  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420497 |       0.179314 |    3.4902  |
| solution-pl        |     0.404312 |       0.178975 |    3.49864 |
| solution-flask     |     0.411209 |       1.0088   |    4.82729 |