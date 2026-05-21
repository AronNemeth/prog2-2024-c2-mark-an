# 2026-05-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.20544  |       1.05528  |   0.115718 |
| solution-aron-mark |     6.41002  |       0.174578 |   0.245229 |
| solution-pl        |     0.472299 |       0.157483 |   0.245582 |
| solution-1-flask   |     0.454928 |       1.00829  |   0.269444 |
| solution-1         |     7.90054  |       1e-06    |   0.685135 |
| solution-2         |     0.448723 |       0.758658 |   1.53858  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.463948 |       0.156937 |   0.392008 |
| solution-aron-mark |     0.467882 |       0.156661 |   0.39547  |
| solution-flask     |     0.458836 |       1.00867  |   0.427736 |
| solution-1-flask   |     0.455531 |       1.00859  |   0.819895 |
| solution-2         |     0.450799 |       0.52526  |   2.32912  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.450307 |       0.159458 |    1.18225 |
| solution-pl        |     0.479406 |       0.164634 |    1.19094 |
| solution-flask     |     0.45569  |       1.00896  |    1.75634 |
| solution-1-flask   |     0.461969 |       1.00907  |    6.03284 |
| solution-2         |     0.446142 |       0.585169 |   37.524   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.472187 |       0.186941 |    4.27232 |
| solution-pl        |     0.469929 |       0.183518 |    4.35289 |
| solution-flask     |     0.465209 |       1.00874  |    5.72554 |