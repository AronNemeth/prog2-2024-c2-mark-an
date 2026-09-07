# 2026-09-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.23164  |       1.05439  |   0.112082 |
| solution-1-flask   |     0.429167 |       1.00896  |   0.225226 |
| solution-aron-mark |     0.429942 |       0.153919 |   0.232632 |
| solution-pl        |     2.54795  |       0.164705 |   0.233204 |
| solution-1         |     8.20286  |       1e-06    |   0.59731  |
| solution-2         |     4.80507  |       0.597327 |   1.18853  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.45692  |       0.160631 |   0.359187 |
| solution-pl        |     0.427343 |       0.154735 |   0.364963 |
| solution-flask     |     0.423604 |       1.00896  |   0.399072 |
| solution-1-flask   |     0.431108 |       1.00893  |   0.727977 |
| solution-2         |     0.426032 |       0.50579  |   2.45805  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.42777  |       0.166466 |    1.05279 |
| solution-aron-mark |     0.423085 |       0.161897 |    1.06706 |
| solution-flask     |     0.427386 |       1.00907  |    1.63321 |
| solution-1-flask   |     0.434282 |       1.009    |    5.66681 |
| solution-2         |     0.42179  |       0.55619  |   30.4903  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42176  |       0.18588  |    3.46121 |
| solution-pl        |     0.424345 |       0.186655 |    3.46798 |
| solution-flask     |     0.422277 |       1.00927  |    5.18197 |