# 2025-10-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.54198  |       1.07095  |   0.103343 |
| solution-aron-mark |     0.487036 |       0.154113 |   0.239197 |
| solution-pl        |     0.486098 |       0.15514  |   0.239372 |
| solution-1-flask   |     0.486826 |       1.00804  |   0.266183 |
| solution-1         |     7.37615  |       1e-06    |   0.694913 |
| solution-2         |     4.49176  |       0.734612 |   0.732664 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.495425 |       0.159465 |   0.366694 |
| solution-pl        |     0.480953 |       0.156842 |   0.369139 |
| solution-flask     |     0.482985 |       1.0082   |   0.375097 |
| solution-1-flask   |     0.484244 |       1.00829  |   0.806697 |
| solution-2         |     0.491965 |       0.501087 |   2.86614  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.48123  |       0.163862 |    1.07996 |
| solution-pl        |     0.482362 |       0.164281 |    1.08182 |
| solution-flask     |     0.48069  |       1.00842  |    1.58981 |
| solution-1-flask   |     0.486933 |       1.00818  |    5.63007 |
| solution-2         |     0.48161  |       0.557277 |   23.4465  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482605 |       0.196948 |    3.21908 |
| solution-aron-mark |     0.486033 |       0.193452 |    3.22864 |
| solution-flask     |     0.483534 |       1.0081   |    5.029   |