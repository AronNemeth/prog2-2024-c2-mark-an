# 2025-07-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.06345  |       1.03964  |   0.101426 |
| solution-pl        |     0.485346 |       0.150072 |   0.232891 |
| solution-aron-mark |     5.52026  |       0.181985 |   0.233001 |
| solution-1-flask   |     0.499879 |       1.00819  |   0.269317 |
| solution-1         |     7.19942  |       1e-06    |   0.654753 |
| solution-2         |     0.495632 |       0.574965 |   0.961328 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.501107 |       0.151996 |   0.359802 |
| solution-aron-mark |     0.493961 |       0.149788 |   0.362093 |
| solution-flask     |     0.49729  |       1.00802  |   0.37926  |
| solution-1-flask   |     0.500677 |       1.00817  |   0.801871 |
| solution-2         |     0.496223 |       0.496673 |   2.76922  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491808 |       0.156646 |    1.07621 |
| solution-aron-mark |     0.494811 |       0.157313 |    1.08429 |
| solution-flask     |     0.493529 |       1.00827  |    1.58422 |
| solution-1-flask   |     0.5039   |       1.00842  |    5.67691 |
| solution-2         |     0.495793 |       0.54698  |   40.7854  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494645 |       0.190814 |    3.18838 |
| solution-pl        |     0.505656 |       0.190313 |    3.19714 |
| solution-flask     |     0.492249 |       1.00827  |    5.08082 |