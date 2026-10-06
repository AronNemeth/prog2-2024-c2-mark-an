# 2026-10-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.97016  |       1.11553  |   0.091125 |
| solution-1-flask   |     0.451976 |       1.00902  |   0.230284 |
| solution-aron-mark |     7.00011  |       0.230478 |   0.247635 |
| solution-pl        |     0.94369  |       0.167135 |   0.256565 |
| solution-1         |     9.13263  |       1e-06    |   0.764217 |
| solution-2         |     0.927267 |       0.744858 |   1.51293  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.445082 |       1.0091   |   0.21764  |
| solution-aron-mark |     0.449967 |       0.171912 |   0.385413 |
| solution-pl        |     0.458804 |       0.181094 |   0.394493 |
| solution-1-flask   |     0.479896 |       1.00922  |   0.75117  |
| solution-2         |     0.469085 |       0.555392 |   2.75201  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.488161 |       1.00946  |   0.976503 |
| solution-aron-mark |     0.492845 |       0.185847 |   1.11453  |
| solution-pl        |     0.473394 |       0.187081 |   1.1174   |
| solution-1-flask   |     0.482096 |       1.00954  |   6.04618  |
| solution-2         |     0.487775 |       0.631994 |  40.9812   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.465175 |       0.216302 |    3.85771 |
| solution-pl        |     0.47179  |       0.218537 |    3.91572 |
| solution-flask     |     0.488812 |       1.00937  |    4.53994 |