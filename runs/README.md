# 2024-11-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.09205  |       1.11956  |   0.109464 |
| solution-aron-mark |     0.565892 |       0.107612 |   0.17752  |
| solution-pl        |     5.68769  |       0.114512 |   0.182382 |
| solution-1-flask   |     0.59175  |       1.00964  |   0.259877 |
| solution-1         |     7.53926  |       1e-06    |   0.657667 |
| solution-2         |     0.561078 |       0.592537 |   0.931602 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.560776 |       0.109842 |   0.300729 |
| solution-pl        |     0.558976 |       0.11103  |   0.331217 |
| solution-flask     |     0.553287 |       1.00898  |   0.483402 |
| solution-1-flask   |     0.560013 |       1.009    |   0.765768 |
| solution-2         |     0.55846  |       0.476479 |   4.83708  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.563336 |       0.116104 |    1.02533 |
| solution-aron-mark |     0.551648 |       0.115851 |    1.02874 |
| solution-flask     |     0.552037 |       1.00913  |    2.15088 |
| solution-1-flask   |     0.559818 |       1.00904  |    5.48975 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.587946 |       0.147856 |    4.17486 |
| solution-pl        |     0.558111 |       0.149803 |    4.38516 |
| solution-flask     |     0.553202 |       1.00925  |    8.56369 |