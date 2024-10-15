# 2024-10-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.530215 |       1.00874  |   0.086943 |
| solution-pl        |     0.539018 |       0.107582 |   0.181246 |
| solution-aron-mark |     1.96677  |       0.105767 |   0.181687 |
| solution-1-flask   |     5.2814   |       1.08702  |   0.267967 |
| solution-1         |     7.85462  |       1e-06    |   0.616706 |
| solution-2         |     0.536693 |       0.5811   |   1.25145  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.524754 |       1.009    |   0.206867 |
| solution-aron-mark |     0.537136 |       0.105295 |   0.308952 |
| solution-pl        |     0.536199 |       0.105711 |   0.309022 |
| solution-1-flask   |     0.547735 |       1.0089   |   0.805234 |
| solution-2         |     0.537779 |       0.502788 |  14.7541   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.538529 |       1.00873  |   0.931886 |
| solution-pl        |     0.54058  |       0.114116 |   1.04986  |
| solution-aron-mark |     0.540644 |       0.113353 |   1.05261  |
| solution-1-flask   |     0.542147 |       1.00923  |   6.06596  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.519661 |       1.00992  |    4.37627 |
| solution-pl        |     0.526806 |       0.142829 |    4.72957 |
| solution-aron-mark |     0.526877 |       0.142227 |    4.73739 |