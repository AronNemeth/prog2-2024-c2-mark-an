# 2025-10-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.06872  |       1.06161  |   0.104889 |
| solution-pl        |     0.49798  |       0.156295 |   0.241496 |
| solution-aron-mark |     0.498764 |       0.159318 |   0.244371 |
| solution-1-flask   |     0.504706 |       1.00848  |   0.26993  |
| solution-1         |     8.39098  |       1e-06    |   0.753533 |
| solution-2         |     4.95548  |       0.747373 |   0.859502 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496793 |       0.156939 |   0.37054  |
| solution-pl        |     0.504743 |       0.159564 |   0.373084 |
| solution-flask     |     0.504406 |       1.00883  |   0.38514  |
| solution-1-flask   |     0.508093 |       1.00867  |   0.816481 |
| solution-2         |     0.517956 |       0.55381  |   2.56616  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.497398 |       0.164238 |    1.07702 |
| solution-pl        |     0.491972 |       0.161721 |    1.08358 |
| solution-flask     |     0.496682 |       1.0086   |    1.6054  |
| solution-1-flask   |     0.511025 |       1.00864  |    5.70036 |
| solution-2         |     0.502862 |       0.596933 |  299.727   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.490824 |       0.193659 |    3.32949 |
| solution-aron-mark |     0.494503 |       0.196079 |    3.33178 |
| solution-flask     |     0.49036  |       1.00903  |    5.24878 |