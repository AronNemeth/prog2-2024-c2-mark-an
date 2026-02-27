# 2026-02-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.59426  |       1.0611   |   0.109125 |
| solution-aron-mark |     0.442854 |       0.149073 |   0.235147 |
| solution-pl        |     4.79685  |       0.1466   |   0.235966 |
| solution-1-flask   |     0.451662 |       1.00864  |   0.272681 |
| solution-1         |     7.7537   |       1e-06    |   0.713679 |
| solution-2         |     0.450167 |       0.684353 |   0.874503 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.45297  |       0.151326 |   0.371435 |
| solution-pl        |     0.456833 |       0.148226 |   0.376197 |
| solution-flask     |     0.454989 |       1.00892  |   0.389981 |
| solution-1-flask   |     0.474039 |       1.00922  |   0.829401 |
| solution-2         |     0.446264 |       0.534483 |   3.04082  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.451369 |       0.152524 |    1.11939 |
| solution-pl        |     0.45627  |       0.155198 |    1.14271 |
| solution-flask     |     0.461977 |       1.00905  |    1.62224 |
| solution-1-flask   |     0.455044 |       1.00886  |    5.52981 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.447204 |       0.179412 |    3.85256 |
| solution-pl        |     0.453098 |       0.181245 |    3.92519 |
| solution-flask     |     0.447157 |       1.00893  |    5.21448 |