# 2026-06-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.67392  |       1.20901  |   0.101743 |
| solution-pl        |     0.427833 |       0.150949 |   0.230498 |
| solution-1-flask   |     0.431847 |       1.0088   |   0.230738 |
| solution-aron-mark |     0.430833 |       0.150052 |   0.232111 |
| solution-1         |     7.46699  |       1e-06    |   0.609881 |
| solution-2         |     4.46469  |       0.660563 |   0.91845  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.428587 |       0.151814 |   0.351483 |
| solution-pl        |     0.424434 |       0.152174 |   0.352872 |
| solution-flask     |     0.431694 |       1.00895  |   0.38773  |
| solution-1-flask   |     0.430533 |       1.00881  |   0.729378 |
| solution-2         |     0.427572 |       0.505643 |   2.86758  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.424777 |       0.157334 |    1.02308 |
| solution-aron-mark |     0.42662  |       0.159064 |    1.0547  |
| solution-flask     |     0.42659  |       1.00893  |    1.63552 |
| solution-1-flask   |     0.432546 |       1.00887  |    5.57214 |
| solution-2         |     0.435506 |       0.561666 |   47.2281  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.425021 |       0.182973 |    3.79928 |
| solution-pl        |     0.430234 |       0.184261 |    3.80504 |
| solution-flask     |     0.427522 |       1.00886  |    5.27539 |