# 2024-12-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.12029  |       1.10786  |   0.110759 |
| solution-pl        |     5.74058  |       0.111228 |   0.182703 |
| solution-aron-mark |     0.558909 |       0.106362 |   0.189643 |
| solution-1-flask   |     0.57359  |       1.00892  |   0.265011 |
| solution-1         |     7.51934  |       1e-06    |   0.577001 |
| solution-2         |     0.608663 |       0.529316 |   1.63403  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.562161 |       0.109252 |   0.30219  |
| solution-pl        |     0.56143  |       0.109451 |   0.303038 |
| solution-flask     |     0.560406 |       1.00881  |   0.495816 |
| solution-1-flask   |     0.561559 |       1.0094   |   0.772864 |
| solution-2         |     0.554985 |       0.47194  |   3.13963  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.566456 |       0.117816 |    1.0298  |
| solution-pl        |     0.565777 |       0.116768 |    1.03252 |
| solution-flask     |     0.559613 |       1.00903  |    2.20138 |
| solution-1-flask   |     0.562667 |       1.00908  |    5.35236 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.561389 |       0.143796 |    4.25448 |
| solution-aron-mark |     0.555408 |       0.14666  |    4.33401 |
| solution-flask     |     0.555617 |       1.00903  |    8.55802 |