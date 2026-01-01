# 2026-01-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.65919  |       1.09528  |   0.097711 |
| solution-aron-mark |     0.471335 |       0.166179 |   0.24222  |
| solution-pl        |     0.47245  |       0.161111 |   0.24345  |
| solution-1-flask   |     0.473007 |       1.00823  |   0.262266 |
| solution-1         |     8.09822  |       1e-06    |   0.696901 |
| solution-2         |     4.98843  |       0.728014 |   1.22084  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481007 |       0.162117 |   0.368473 |
| solution-flask     |     0.470335 |       1.00831  |   0.372213 |
| solution-aron-mark |     0.479269 |       0.169233 |   0.374511 |
| solution-1-flask   |     0.474575 |       1.00845  |   0.800051 |
| solution-2         |     0.46718  |       0.508745 |   2.93731  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.472528 |       0.167401 |    1.05926 |
| solution-aron-mark |     0.474879 |       0.169233 |    1.06399 |
| solution-flask     |     0.469626 |       1.0085   |    1.55445 |
| solution-1-flask   |     0.480257 |       1.00875  |    5.56065 |
| solution-2         |     0.464196 |       0.561762 |  165.898   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.469582 |       0.193193 |    3.53966 |
| solution-aron-mark |     0.471036 |       0.195513 |    3.55886 |
| solution-flask     |     0.467665 |       1.00853  |    5.02834 |