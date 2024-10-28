# 2024-10-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.27524  |       1.05673  |   0.108276 |
| solution-pl        |     5.75465  |       0.109522 |   0.193347 |
| solution-aron-mark |     0.552506 |       0.10675  |   0.193503 |
| solution-1-flask   |     0.564667 |       1.00903  |   0.271824 |
| solution-1         |     7.56191  |       1e-06    |   0.611421 |
| solution-2         |     0.550876 |       0.507815 |   1.20737  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.554487 |       0.108403 |   0.296197 |
| solution-aron-mark |     0.555848 |       0.108938 |   0.297837 |
| solution-flask     |     0.554184 |       1.00902  |   0.474965 |
| solution-1-flask   |     0.564687 |       1.00881  |   0.787411 |
| solution-2         |     0.554472 |       0.469016 |   2.73174  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.556716 |       0.115832 |   0.989711 |
| solution-pl        |     0.5584   |       0.116196 |   0.992174 |
| solution-flask     |     0.559278 |       1.00934  |   2.09165  |
| solution-1-flask   |     0.558424 |       1.00881  |   5.41703  |
| solution-2         |     0.559246 |       0.523023 |  34.9696   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.557534 |       0.146093 |    4.17211 |
| solution-aron-mark |     0.554004 |       0.145195 |    4.18337 |
| solution-flask     |     0.557736 |       1.00935  |    8.41197 |