# 2025-11-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06351  |       1.04724  |   0.099431 |
| solution-pl        |     0.467738 |       0.157738 |   0.243072 |
| solution-aron-mark |     0.46242  |       0.156301 |   0.243356 |
| solution-1-flask   |     0.477322 |       1.00847  |   0.261984 |
| solution-1         |     7.78408  |       1e-06    |   0.738129 |
| solution-2         |     4.78173  |       0.674025 |   1.29008  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4692   |       0.15758  |   0.371467 |
| solution-aron-mark |     0.471043 |       0.159233 |   0.37172  |
| solution-flask     |     0.479835 |       1.00862  |   0.376148 |
| solution-1-flask   |     0.47246  |       1.00839  |   0.795979 |
| solution-2         |     0.467979 |       0.501626 |   2.74403  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.46486  |       0.164101 |    1.09088 |
| solution-pl        |     0.485321 |       0.169425 |    1.09204 |
| solution-flask     |     0.466025 |       1.00862  |    1.58538 |
| solution-1-flask   |     0.477011 |       1.00842  |    5.55854 |
| solution-2         |     0.467808 |       0.558884 |   39.2978  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476647 |       0.194133 |    3.21577 |
| solution-pl        |     0.473217 |       0.193042 |    3.21758 |
| solution-flask     |     0.473404 |       1.00856  |    5.12442 |