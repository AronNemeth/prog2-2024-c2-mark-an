# 2025-02-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.17548  |       1.10936  |   0.082445 |
| solution-aron-mark |     0.548952 |       0.147712 |   0.207582 |
| solution-pl        |     4.67422  |       0.144184 |   0.223103 |
| solution-1-flask   |     0.550597 |       1.00907  |   0.264671 |
| solution-1         |     7.52739  |       1e-06    |   0.906498 |
| solution-2         |     0.552152 |       0.737174 |   1.16492  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550813 |       1.00927  |   0.291145 |
| solution-aron-mark |     0.534585 |       0.142746 |   0.306552 |
| solution-pl        |     0.555942 |       0.14647  |   0.312245 |
| solution-1-flask   |     0.540434 |       1.00882  |   0.795862 |
| solution-2         |     0.559104 |       0.527438 |   8.70097  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.542808 |       0.150107 |   0.897359 |
| solution-pl        |     0.552605 |       0.154212 |   0.911848 |
| solution-flask     |     0.543241 |       1.00915  |   1.2517   |
| solution-1-flask   |     0.550361 |       1.00887  |   5.76082  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541686 |       0.181588 |    2.90525 |
| solution-aron-mark |     0.5392   |       0.180356 |    2.94695 |
| solution-flask     |     0.540206 |       1.00901  |    4.22283 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543995 |       0.282513 |    19.0739 |
| solution-aron-mark |     0.553642 |       0.284326 |    19.5398 |