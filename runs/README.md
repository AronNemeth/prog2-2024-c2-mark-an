# 2024-09-19

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.8775   |       1.07384  |   0.08347  |
| solution-aron-mark |     1.99042  |       0.102553 |   0.176153 |
| solution-pl        |     0.567258 |       0.10229  |   0.178162 |
| solution-1-flask   |     0.57947  |       1.00811  |   0.264818 |
| solution-1         |     8.43794  |       1e-06    |   0.592678 |
| solution-2         |     5.26072  |       0.577799 |   0.901211 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.573274 |       1.0088   |   0.20563  |
| solution-pl        |     0.569562 |       0.104922 |   0.303529 |
| solution-aron-mark |     0.568679 |       0.105621 |   0.30685  |
| solution-1-flask   |     0.575345 |       1.00862  |   0.786682 |
| solution-2         |     0.577571 |       0.487035 |   2.64687  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.574967 |       1.00828  |   0.924718 |
| solution-pl        |     0.57571  |       0.113317 |   1.04164  |
| solution-aron-mark |     0.569391 |       0.10976  |   1.04546  |
| solution-1-flask   |     0.566665 |       1.0082   |   5.58015  |
| solution-2         |     0.566836 |       0.541164 |  33.1615   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.565365 |       1.00848  |    4.25871 |
| solution-aron-mark |     0.567039 |       0.145323 |    4.48785 |
| solution-pl        |     0.575964 |       0.14096  |    4.6231  |