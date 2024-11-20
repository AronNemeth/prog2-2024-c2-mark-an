# 2024-11-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.2222   |       1.1143   |   0.130505 |
| solution-pl        |     6.08368  |       0.11478  |   0.196929 |
| solution-aron-mark |     0.618435 |       0.114302 |   0.210597 |
| solution-1-flask   |     0.640818 |       1.01014  |   0.267825 |
| solution-1         |     8.21274  |       2e-06    |   0.83281  |
| solution-2         |     0.623123 |       0.578088 |   1.3539   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.636149 |       0.118753 |   0.315573 |
| solution-aron-mark |     0.595196 |       0.12373  |   0.356578 |
| solution-flask     |     0.625813 |       1.01007  |   0.512667 |
| solution-1-flask   |     0.620665 |       1.00939  |   0.826449 |
| solution-2         |     0.602816 |       0.540239 |   3.3632   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.597394 |       0.121429 |    1.05446 |
| solution-pl        |     0.608531 |       0.125538 |    1.09374 |
| solution-flask     |     0.656127 |       1.01063  |    2.33821 |
| solution-1-flask   |     0.606691 |       1.00935  |    5.74207 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.610403 |       0.157386 |    5.56635 |
| solution-aron-mark |     0.595544 |       0.154667 |    5.77897 |
| solution-flask     |     0.638294 |       1.0097   |   10.2202  |