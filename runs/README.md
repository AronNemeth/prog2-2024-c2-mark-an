# 2026-11-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.81291  |       1.05313  |   0.071823 |
| solution-1-flask   |     0.325411 |       1.00929  |   0.176224 |
| solution-pl        |     0.325001 |       0.129052 |   0.188979 |
| solution-aron-mark |     6.76383  |       0.129206 |   0.197847 |
| solution-1         |     6.68673  |       1e-06    |   0.468238 |
| solution-2         |     0.364697 |       0.433079 |   0.680725 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.331696 |       1.00991  |   0.167234 |
| solution-aron-mark |     0.327292 |       0.130817 |   0.289167 |
| solution-pl        |     0.335234 |       0.133786 |   0.290468 |
| solution-1-flask   |     0.338209 |       1.00951  |   0.533061 |
| solution-2         |     0.324735 |       0.417458 |   8.55946  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.336239 |       1.00952  |   0.721709 |
| solution-aron-mark |     0.330864 |       0.139675 |   0.820511 |
| solution-pl        |     0.331494 |       0.139463 |   0.821515 |
| solution-1-flask   |     0.328687 |       1.00942  |   4.03034  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.328215 |       0.165175 |    2.67798 |
| solution-aron-mark |     0.323166 |       0.165377 |    2.7602  |
| solution-flask     |     0.335847 |       1.00954  |    3.29376 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.334024 |       0.24158  |    15.922  |
| solution-aron-mark |     0.334611 |       0.242479 |    15.9275 |