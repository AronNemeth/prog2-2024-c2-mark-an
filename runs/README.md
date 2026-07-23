# 2026-07-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.97543  |       1.06365  |   0.105508 |
| solution-pl        |     0.426777 |       0.15517  |   0.240766 |
| solution-aron-mark |     0.431983 |       0.150958 |   0.241141 |
| solution-1-flask   |     0.44443  |       1.00853  |   0.267718 |
| solution-1         |     8.11295  |       1e-06    |   0.633413 |
| solution-2         |     4.91172  |       0.61156  |   0.965453 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434299 |       0.152789 |   0.371545 |
| solution-aron-mark |     0.433723 |       0.154445 |   0.374781 |
| solution-flask     |     0.431763 |       1.00865  |   0.392331 |
| solution-1-flask   |     0.445066 |       1.00871  |   0.815625 |
| solution-2         |     0.426406 |       0.508847 |   3.62814  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432467 |       0.158253 |    1.12133 |
| solution-aron-mark |     0.430564 |       0.158926 |    1.12588 |
| solution-flask     |     0.428263 |       1.00854  |    1.69466 |
| solution-1-flask   |     0.430784 |       1.00879  |    5.77742 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435438 |       0.187271 |    3.60094 |
| solution-pl        |     0.43134  |       0.182827 |    3.63647 |
| solution-flask     |     0.431334 |       1.0086   |    5.36398 |