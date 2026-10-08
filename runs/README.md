# 2026-10-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.58032  |       1.15303  |   0.108234 |
| solution-pl        |     0.438097 |       0.168067 |   0.257476 |
| solution-aron-mark |     6.72863  |       0.286938 |   0.263953 |
| solution-1-flask   |     0.440628 |       1.0086   |   0.276783 |
| solution-1         |     8.18398  |       1e-06    |   0.670291 |
| solution-2         |     0.44608  |       0.694593 |   0.926619 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.441824 |       1.00895  |   0.245117 |
| solution-aron-mark |     0.436956 |       0.167805 |   0.401876 |
| solution-pl        |     0.446756 |       0.169802 |   0.405208 |
| solution-1-flask   |     0.449008 |       1.00873  |   0.82124  |
| solution-2         |     0.450004 |       0.594215 |   6.63042  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.442263 |       1.00896  |    1.03306 |
| solution-aron-mark |     0.447903 |       0.179219 |    1.19829 |
| solution-pl        |     0.454333 |       0.178315 |    1.21206 |
| solution-1-flask   |     0.472502 |       1.00883  |    5.65033 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.443503 |       0.204765 |     3.7618 |
| solution-pl        |     0.434155 |       0.203914 |     3.8539 |
| solution-flask     |     0.452251 |       1.00862  |     4.4424 |