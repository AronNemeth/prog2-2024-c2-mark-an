# 2025-04-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.71662  |       1.07974  |   0.10817  |
| solution-pl        |     6.35178  |       0.129458 |   0.198894 |
| solution-aron-mark |     0.567856 |       0.1311   |   0.199467 |
| solution-1-flask   |     0.561814 |       1.00947  |   0.269652 |
| solution-1         |     8.55255  |       2e-06    |   0.75505  |
| solution-2         |     0.543307 |       0.710173 |   1.07415  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.540968 |       0.126486 |   0.301176 |
| solution-pl        |     0.544601 |       0.131189 |   0.305411 |
| solution-flask     |     0.556108 |       1.00926  |   0.335558 |
| solution-1-flask   |     0.543474 |       1.00889  |   0.792409 |
| solution-2         |     0.561332 |       0.552923 |   5.42016  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.566636 |       0.139047 |   0.944991 |
| solution-pl        |     0.585733 |       0.139692 |   0.955396 |
| solution-flask     |     0.544325 |       1.00966  |   1.27348  |
| solution-1-flask   |     0.569869 |       1.00922  |   5.54822  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.554036 |       0.16748  |    3.16207 |
| solution-aron-mark |     0.551856 |       0.165866 |    3.19813 |
| solution-flask     |     0.53482  |       1.00906  |    4.54154 |