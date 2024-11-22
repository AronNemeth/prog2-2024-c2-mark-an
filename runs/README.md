# 2024-11-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23138  |       1.0766   |   0.107838 |
| solution-pl        |     5.83     |       0.111458 |   0.175985 |
| solution-aron-mark |     0.577821 |       0.10911  |   0.177314 |
| solution-1-flask   |     0.580365 |       1.00912  |   0.258708 |
| solution-1         |     7.71154  |       1e-06    |   0.582443 |
| solution-2         |     0.570684 |       0.536574 |   1.64204  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.576063 |       0.111742 |   0.304267 |
| solution-aron-mark |     0.608001 |       0.112257 |   0.306552 |
| solution-flask     |     0.574825 |       1.00947  |   0.485983 |
| solution-1-flask   |     0.575304 |       1.00899  |   0.781818 |
| solution-2         |     0.569018 |       0.491245 |   5.44182  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.574641 |       0.117562 |    1.02595 |
| solution-aron-mark |     0.588926 |       0.117589 |    1.03058 |
| solution-flask     |     0.568932 |       1.00915  |    2.17632 |
| solution-1-flask   |     0.584848 |       1.00899  |    5.51957 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.578116 |       0.149027 |    4.64921 |
| solution-pl        |     0.569611 |       0.151461 |    4.66867 |
| solution-flask     |     0.573149 |       1.00958  |    8.88288 |