# 2025-12-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.54863  |       1.07118  |   0.101874 |
| solution-pl        |     0.51202  |       0.166822 |   0.253149 |
| solution-aron-mark |     0.498689 |       0.162621 |   0.258443 |
| solution-1-flask   |     0.523342 |       1.00832  |   0.263811 |
| solution-1         |     7.89866  |       1e-06    |   0.755477 |
| solution-2         |     4.73144  |       0.725323 |   0.98105  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496412 |       0.191317 |   0.376289 |
| solution-pl        |     0.519129 |       0.172197 |   0.378432 |
| solution-flask     |     0.511622 |       1.00867  |   0.382906 |
| solution-1-flask   |     0.516149 |       1.00904  |   0.810669 |
| solution-2         |     0.496475 |       0.572489 |   3.06258  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.5125   |       0.176418 |    1.08448 |
| solution-pl        |     0.518903 |       0.183166 |    1.10521 |
| solution-flask     |     0.509808 |       1.00907  |    1.618   |
| solution-1-flask   |     0.514091 |       1.0089   |    5.90671 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.516153 |       0.211642 |    3.64164 |
| solution-aron-mark |     0.526129 |       0.210361 |    3.64318 |
| solution-flask     |     0.516244 |       1.00878  |    5.476   |