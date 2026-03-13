# 2026-03-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.52938  |       1.05245  |   0.104829 |
| solution-aron-mark |     0.460644 |       0.154819 |   0.23609  |
| solution-pl        |     4.72931  |       0.151294 |   0.238086 |
| solution-1-flask   |     0.45439  |       1.00889  |   0.260519 |
| solution-1         |     7.5685   |       1e-06    |   0.63985  |
| solution-2         |     0.447036 |       0.615717 |   1.70026  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.452477 |       0.152586 |   0.369789 |
| solution-aron-mark |     0.450562 |       0.150067 |   0.373613 |
| solution-flask     |     0.452583 |       1.00892  |   0.394003 |
| solution-1-flask   |     0.454496 |       1.00862  |   0.795237 |
| solution-2         |     0.445928 |       0.515751 |  14.2893   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.464496 |       0.161797 |    1.15205 |
| solution-aron-mark |     0.474983 |       0.159859 |    1.16143 |
| solution-flask     |     0.448321 |       1.00896  |    1.66472 |
| solution-1-flask   |     0.482795 |       1.00941  |    5.62006 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472688 |       0.185634 |    4.09788 |
| solution-aron-mark |     0.450652 |       0.190059 |    4.09839 |
| solution-flask     |     0.46822  |       1.00907  |    5.40546 |