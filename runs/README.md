# 2025-09-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.480025 |       1.00817  |   0.1005   |
| solution-pl        |     6.00024  |       0.164062 |   0.236333 |
| solution-aron-mark |     0.480809 |       0.150944 |   0.237052 |
| solution-1-flask   |     1.22197  |       1.04875  |   0.268862 |
| solution-1         |     7.60239  |       1e-06    |   0.634478 |
| solution-2         |     0.485159 |       0.643288 |   1.08517  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.486906 |       0.154459 |   0.360907 |
| solution-pl        |     0.48926  |       0.156629 |   0.362191 |
| solution-flask     |     0.484519 |       1.00816  |   0.382405 |
| solution-1-flask   |     0.490535 |       1.0081   |   0.784852 |
| solution-2         |     0.483181 |       0.506727 |  14.3763   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.484869 |       0.15973  |    1.09169 |
| solution-pl        |     0.491756 |       0.165283 |    1.10175 |
| solution-flask     |     0.484326 |       1.00848  |    1.56517 |
| solution-1-flask   |     0.491421 |       1.00838  |    5.73308 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482075 |       0.194118 |    3.25224 |
| solution-aron-mark |     0.483632 |       0.195722 |    3.26267 |
| solution-flask     |     0.483216 |       1.0084   |    5.16118 |