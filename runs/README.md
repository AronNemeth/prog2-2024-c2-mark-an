# 2025-10-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.86558  |       1.05963  |   0.105356 |
| solution-pl        |     0.486131 |       0.156728 |   0.242526 |
| solution-aron-mark |     0.48631  |       0.155905 |   0.242868 |
| solution-1-flask   |     0.489782 |       1.0094   |   0.269176 |
| solution-1         |     8.09795  |       1e-06    |   0.750014 |
| solution-2         |     4.90179  |       0.610474 |   1.01527  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485994 |       0.15808  |   0.372369 |
| solution-pl        |     0.488818 |       0.158416 |   0.378251 |
| solution-flask     |     0.48759  |       1.00851  |   0.391402 |
| solution-1-flask   |     0.489251 |       1.00845  |   0.826472 |
| solution-2         |     0.482708 |       0.510785 |   2.95001  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.488182 |       0.163863 |    1.09882 |
| solution-pl        |     0.500859 |       0.173357 |    1.11973 |
| solution-flask     |     0.489964 |       1.00848  |    1.6205  |
| solution-1-flask   |     0.499382 |       1.00894  |    5.67892 |
| solution-2         |     0.504727 |       0.567057 |   25.3455  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485415 |       0.194789 |    3.29201 |
| solution-pl        |     0.485481 |       0.198661 |    3.31898 |
| solution-flask     |     0.498974 |       1.00885  |    5.16703 |