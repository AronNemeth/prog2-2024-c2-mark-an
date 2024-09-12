# 2024-09-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.15732  |       1.08703  |   0.088615 |
| solution-pl        |     0.556543 |       0.104621 |   0.184355 |
| solution-aron-mark |     5.64948  |       0.105696 |   0.190117 |
| solution-1-flask   |     0.558687 |       1.00923  |   0.256537 |
| solution-1         |     7.5631   |       1e-06    |   0.574913 |
| solution-2         |     0.55439  |       0.486686 |   1.58054  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554811 |       1.00913  |   0.225191 |
| solution-pl        |     0.549638 |       0.105538 |   0.302836 |
| solution-aron-mark |     0.568333 |       0.105354 |   0.3175   |
| solution-1-flask   |     0.565965 |       1.00901  |   0.773296 |
| solution-2         |     0.558375 |       0.473983 |   2.46905  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55136  |       1.00917  |   0.914598 |
| solution-aron-mark |     0.552608 |       0.114025 |   0.995116 |
| solution-pl        |     0.55583  |       0.111892 |   0.998149 |
| solution-1-flask   |     0.565743 |       1.00893  |   5.55346  |
| solution-2         |     0.551948 |       0.528366 | 173.169    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.557075 |       1.00961  |    4.1466  |
| solution-aron-mark |     0.55217  |       0.146538 |    4.1666  |
| solution-pl        |     0.555058 |       0.145471 |    4.18737 |