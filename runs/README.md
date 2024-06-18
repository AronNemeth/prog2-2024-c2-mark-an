# 2024-06-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.669979 |       1.00912  |   0.074292 |
| solution-pl        |     0.685627 |       0.10819  |   0.161527 |
| solution-aron-mark |     5.94019  |       0.102953 |   0.168319 |
| solution-1-flask   |     1.33964  |       1.09475  |   0.263943 |
| solution-1         |     8.89746  |       1e-06    |   0.674802 |
| solution-2         |     0.667166 |       0.699366 |   0.881371 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672744 |       1.00873  |   0.164602 |
| solution-aron-mark |     0.672286 |       0.105366 |   0.256439 |
| solution-pl        |     0.673598 |       0.10466  |   0.270847 |
| solution-1-flask   |     0.68188  |       1.00895  |   0.796347 |
| solution-2         |     0.668654 |       0.47053  |   2.96123  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674983 |       1.00918  |   0.729987 |
| solution-aron-mark |     0.686093 |       0.113548 |   0.815662 |
| solution-pl        |     0.671306 |       0.113899 |   0.821919 |
| solution-1-flask   |     0.683477 |       1.00908  |   5.5076   |
| solution-2         |     0.681945 |       0.525456 | 164.243    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.670253 |       1.00974  |    2.54433 |
| solution-pl        |     0.676597 |       0.152812 |    2.65735 |
| solution-aron-mark |     0.683669 |       0.15501  |    2.67709 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667556 |       1.00928  |    17.3448 |
| solution-aron-mark |     0.67109  |       0.277716 |    23.2148 |
| solution-pl        |     0.674967 |       0.277276 |    24.3249 |