# 2024-07-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.492743 |       1.00864  |   0.072209 |
| solution-aron-mark |     5.68323  |       0.099494 |   0.162274 |
| solution-pl        |     0.494833 |       0.098386 |   0.166747 |
| solution-1-flask   |     1.04827  |       1.10964  |   0.258192 |
| solution-1         |     7.64053  |       1e-06    |   0.570387 |
| solution-2         |     0.488854 |       0.484154 |   0.97372  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.485546 |       1.00906  |   0.184032 |
| solution-aron-mark |     0.496174 |       0.101072 |   0.279155 |
| solution-pl        |     0.493153 |       0.101451 |   0.283206 |
| solution-1-flask   |     0.500883 |       1.00975  |   0.761134 |
| solution-2         |     0.480078 |       0.470612 |  13.0876   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.490952 |       1.00883  |   0.870209 |
| solution-aron-mark |     0.5051   |       0.110086 |   0.972125 |
| solution-pl        |     0.496697 |       0.108065 |   1.0158   |
| solution-1-flask   |     0.498098 |       1.00883  |   5.48214  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.493696 |       1.00866  |    3.91198 |
| solution-aron-mark |     0.512711 |       0.143766 |    4.01703 |
| solution-pl        |     0.494569 |       0.145392 |    4.05457 |