# 2025-01-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.2408   |       1.05862  |   0.082057 |
| solution-pl        |     4.84061  |       0.151833 |   0.218528 |
| solution-aron-mark |     0.58805  |       0.159895 |   0.221542 |
| solution-1-flask   |     0.579547 |       1.00886  |   0.270215 |
| solution-1         |     7.77105  |       1e-06    |   0.735459 |
| solution-2         |     0.598984 |       0.638881 |   1.2735   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.597394 |       1.00907  |   0.311726 |
| solution-pl        |     0.578089 |       0.151401 |   0.317547 |
| solution-aron-mark |     0.567339 |       0.15257  |   0.320703 |
| solution-1-flask   |     0.591621 |       1.0103   |   0.808447 |
| solution-2         |     0.578903 |       0.539992 |   3.88146  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.588711 |       0.156691 |   0.911878 |
| solution-aron-mark |     0.588278 |       0.153374 |   0.921422 |
| solution-flask     |     0.598128 |       1.00968  |   1.28     |
| solution-1-flask   |     0.5877   |       1.00928  |   6.05381  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.571492 |       0.18919  |    3.03805 |
| solution-pl        |     0.579914 |       0.184749 |    3.05466 |
| solution-flask     |     0.579667 |       1.00955  |    4.56131 |