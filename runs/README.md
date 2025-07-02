# 2025-07-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20818  |       1.04979  |   0.104613 |
| solution-aron-mark |     5.93939  |       0.170364 |   0.236652 |
| solution-pl        |     0.493142 |       0.151527 |   0.239296 |
| solution-1-flask   |     0.517561 |       1.00808  |   0.268617 |
| solution-1         |     7.69019  |       1e-06    |   0.720971 |
| solution-2         |     0.504128 |       0.646923 |   1.17056  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.506903 |       0.153971 |   0.36044  |
| solution-aron-mark |     0.514299 |       0.152788 |   0.366107 |
| solution-flask     |     0.50548  |       1.00825  |   0.376023 |
| solution-1-flask   |     0.51481  |       1.00825  |   0.795757 |
| solution-2         |     0.514356 |       0.514466 |   7.91668  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.504176 |       0.160255 |    1.07696 |
| solution-aron-mark |     0.505366 |       0.158361 |    1.07851 |
| solution-flask     |     0.499925 |       1.00839  |    1.63081 |
| solution-1-flask   |     0.524862 |       1.00879  |    5.65777 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.512438 |       0.188991 |    3.2551  |
| solution-aron-mark |     0.514021 |       0.188706 |    3.31954 |
| solution-flask     |     0.501586 |       1.00847  |    5.17939 |