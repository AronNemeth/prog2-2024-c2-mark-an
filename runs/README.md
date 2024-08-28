# 2024-08-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.558138 |       1.00902  |   0.097802 |
| solution-aron-mark |     1.83996  |       0.108531 |   0.175321 |
| solution-pl        |     0.571704 |       0.10659  |   0.189544 |
| solution-1-flask   |     1.19932  |       1.06551  |   0.260373 |
| solution-1         |     7.7963   |       1e-06    |   0.934482 |
| solution-2         |     4.4753   |       0.732156 |   1.08389  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566049 |       1.00942  |   0.225985 |
| solution-pl        |     0.564204 |       0.115242 |   0.305874 |
| solution-aron-mark |     0.575358 |       0.106197 |   0.337728 |
| solution-1-flask   |     0.571401 |       1.00904  |   0.785117 |
| solution-2         |     0.584896 |       0.498162 |   2.5126   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.561782 |       1.00903  |   0.883684 |
| solution-pl        |     0.560399 |       0.113935 |   0.997291 |
| solution-aron-mark |     0.570069 |       0.113444 |   0.998459 |
| solution-1-flask   |     0.56392  |       1.00921  |   5.45658  |
| solution-2         |     0.549325 |       0.550624 |  32.2918   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.582114 |       1.00971  |    4.30428 |
| solution-aron-mark |     0.571374 |       0.145574 |    4.38917 |
| solution-pl        |     0.566106 |       0.144333 |    4.55358 |