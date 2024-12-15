# 2024-12-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.95829  |       1.00864  |   0.103931 |
| solution-aron-mark |     0.529437 |       0.106662 |   0.184348 |
| solution-pl        |     0.528    |       0.108272 |   0.185711 |
| solution-1-flask   |     5.47952  |       1.07411  |   0.266488 |
| solution-1         |     7.45165  |       1e-06    |   0.590236 |
| solution-2         |     0.530015 |       0.527792 |   1.52606  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535372 |       0.111789 |   0.318208 |
| solution-aron-mark |     0.531508 |       0.109637 |   0.319774 |
| solution-flask     |     0.533508 |       1.00899  |   0.508744 |
| solution-1-flask   |     0.557554 |       1.00919  |   0.819275 |
| solution-2         |     0.525632 |       0.474696 |   3.66509  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.530366 |       0.116466 |    1.07638 |
| solution-aron-mark |     0.530732 |       0.115854 |    1.10812 |
| solution-flask     |     0.547861 |       1.00958  |    2.2494  |
| solution-1-flask   |     0.534168 |       1.00902  |    5.8175  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53286  |       0.146191 |    4.33447 |
| solution-aron-mark |     0.529423 |       0.144369 |    4.33495 |
| solution-flask     |     0.526942 |       1.00873  |    8.75136 |