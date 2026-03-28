# 2026-03-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.64269  |       1.03286  |   0.092557 |
| solution-pl        |     4.58444  |       0.141341 |   0.213711 |
| solution-aron-mark |     0.399396 |       0.139525 |   0.213916 |
| solution-1-flask   |     0.393506 |       1.00641  |   0.242754 |
| solution-1         |     7.39238  |       1e-06    |   0.700588 |
| solution-2         |     0.392803 |       0.65902  |   0.816648 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.39625  |       0.140391 |   0.324416 |
| solution-pl        |     0.406261 |       0.144551 |   0.326973 |
| solution-flask     |     0.398178 |       1.00704  |   0.404141 |
| solution-1-flask   |     0.400009 |       1.00656  |   0.755608 |
| solution-2         |     0.397403 |       0.540997 |   4.31988  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.387986 |       0.144026 |   0.982739 |
| solution-aron-mark |     0.397758 |       0.148055 |   0.992298 |
| solution-flask     |     0.397414 |       1.00697  |   1.7058   |
| solution-1-flask   |     0.402644 |       1.00686  |   5.80394  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.392754 |       0.177602 |    5.10933 |
| solution-aron-mark |     0.387053 |       0.176215 |    5.14663 |
| solution-flask     |     0.393895 |       1.00707  |    5.96962 |