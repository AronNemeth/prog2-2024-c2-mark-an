# 2026-08-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.45845  |       1.04658  |   0.129121 |
| solution-pl        |     0.414385 |       0.144547 |   0.20952  |
| solution-1-flask   |     0.407861 |       1.0087   |   0.214389 |
| solution-aron-mark |     4.78643  |       0.144616 |   0.262236 |
| solution-1         |     7.66731  |       1e-06    |   0.57585  |
| solution-2         |     0.412853 |       0.661735 |   0.832708 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.392871 |       0.148191 |   0.323547 |
| solution-pl        |     0.41732  |       0.147521 |   0.340359 |
| solution-flask     |     0.418102 |       1.00887  |   0.363256 |
| solution-1-flask   |     0.400131 |       1.00882  |   0.679204 |
| solution-2         |     0.399303 |       0.498158 |   5.11693  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.411999 |       0.149611 |   0.955866 |
| solution-pl        |     0.402285 |       0.152124 |   0.965939 |
| solution-flask     |     0.395397 |       1.00858  |   1.48086  |
| solution-1-flask   |     0.408279 |       1.00899  |   5.23264  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.402339 |       0.171822 |    3.26304 |
| solution-aron-mark |     0.409624 |       0.173705 |    3.34976 |
| solution-flask     |     0.407196 |       1.009    |    4.91125 |