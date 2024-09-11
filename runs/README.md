# 2024-09-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.29749  |       1.04823  |   0.099027 |
| solution-pl        |     0.5905   |       0.10905  |   0.179445 |
| solution-aron-mark |     5.90248  |       0.109109 |   0.180111 |
| solution-1-flask   |     0.602911 |       1.0092   |   0.264016 |
| solution-1         |     7.94681  |       1e-06    |   0.791089 |
| solution-2         |     0.585775 |       0.625841 |   0.899851 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.599395 |       1.00942  |   0.224173 |
| solution-pl        |     0.5971   |       0.109862 |   0.297022 |
| solution-aron-mark |     0.589729 |       0.11016  |   0.307274 |
| solution-1-flask   |     0.593926 |       1.0096   |   0.798879 |
| solution-2         |     0.59697  |       0.517729 |  11.7657   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.58411  |       1.00945  |   0.888704 |
| solution-pl        |     0.585991 |       0.116572 |   0.992109 |
| solution-aron-mark |     0.595896 |       0.117905 |   1.03735  |
| solution-1-flask   |     0.595211 |       1.00934  |   5.69284  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.584784 |       1.00967  |    4.52563 |
| solution-aron-mark |     0.570103 |       0.144627 |    4.66983 |
| solution-pl        |     0.577022 |       0.148966 |    4.73313 |