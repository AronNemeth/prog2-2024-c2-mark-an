# 2024-08-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.559614 |       1.00898  |   0.09258  |
| solution-aron-mark |     2.44267  |       0.104546 |   0.16969  |
| solution-pl        |     0.555268 |       0.103857 |   0.192409 |
| solution-1-flask   |     1.69356  |       1.08335  |   0.264202 |
| solution-1         |     8.67207  |       1e-06    |   0.647724 |
| solution-2         |     4.81313  |       0.529958 |   0.817962 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.56253  |       1.00912  |   0.229672 |
| solution-pl        |     0.561151 |       0.106253 |   0.295621 |
| solution-aron-mark |     0.57238  |       0.109166 |   0.322957 |
| solution-1-flask   |     0.57496  |       1.00934  |   0.78929  |
| solution-2         |     0.553043 |       0.478876 |   2.92997  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.57313  |       1.00917  |   0.912746 |
| solution-pl        |     0.602727 |       0.119756 |   1.03052  |
| solution-aron-mark |     0.570471 |       0.113747 |   1.0376   |
| solution-1-flask   |     0.56392  |       1.00902  |   5.53593  |
| solution-2         |     0.556103 |       0.524704 | 169.021    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.561436 |       1.00983  |    4.44207 |
| solution-pl        |     0.568225 |       0.149347 |    4.60705 |
| solution-aron-mark |     0.567864 |       0.148623 |    4.69088 |