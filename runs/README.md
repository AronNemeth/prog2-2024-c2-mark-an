# 2026-09-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.28875  |       1.05342  |   0.112489 |
| solution-aron-mark |     6.11749  |       0.196371 |   0.251089 |
| solution-pl        |     0.436917 |       0.166343 |   0.255941 |
| solution-1-flask   |     0.449668 |       1.00837  |   0.278152 |
| solution-1         |     8.45512  |       1e-06    |   0.685052 |
| solution-2         |     0.436082 |       0.698516 |   0.77861  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434048 |       0.159039 |   0.383935 |
| solution-aron-mark |     0.433457 |       0.159467 |   0.388615 |
| solution-flask     |     0.449143 |       1.00904  |   0.407582 |
| solution-1-flask   |     0.43962  |       1.00901  |   0.844841 |
| solution-2         |     0.439169 |       0.527849 |   2.49322  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461812 |       0.180557 |    1.17186 |
| solution-aron-mark |     0.453394 |       0.166771 |    1.17796 |
| solution-flask     |     0.447978 |       1.00916  |    1.7152  |
| solution-1-flask   |     0.435324 |       1.00843  |    5.9281  |
| solution-2         |     0.467869 |       0.62703  |   53.4532  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.446571 |       0.187266 |    3.67913 |
| solution-aron-mark |     0.447055 |       0.190827 |    3.70804 |
| solution-flask     |     0.43378  |       1.00872  |    5.65105 |