# 2024-05-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.49403  |       1.08132  |   0.075372 |
| solution-pl        |     0.646697 |       0.100844 |   0.157803 |
| solution-aron-mark |    14.2689   |       0.100751 |   0.160863 |
| solution-1-flask   |     0.671833 |       1.00899  |   0.261321 |
| solution-2         |     0.648423 |       0.412875 |   0.674193 |
| solution-1         |    14.6303   |       1e-06    |   0.721349 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661103 |       1.00921  |   0.155992 |
| solution-aron-mark |     0.656002 |       0.102228 |   0.259071 |
| solution-pl        |     0.685624 |       0.103899 |   0.260583 |
| solution-1-flask   |     0.671167 |       1.00925  |   0.775342 |
| solution-2         |     0.662035 |       0.431916 |  12.2606   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662192 |       1.00871  |   0.686868 |
| solution-pl        |     0.663709 |       0.111214 |   0.783221 |
| solution-aron-mark |     0.671796 |       0.111899 |   0.831192 |
| solution-1-flask   |     0.692587 |       1.00896  |   5.57587  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663522 |       1.00926  |    2.44775 |
| solution-aron-mark |     0.661704 |       0.148578 |    2.56239 |
| solution-pl        |     0.675131 |       0.145217 |    2.57514 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.652318 |       1.0089   |    15.6186 |
| solution-aron-mark |     0.674153 |       0.272458 |    22.4399 |
| solution-pl        |     0.655387 |       0.274564 |    22.5751 |