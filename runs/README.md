# 2026-08-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.85793  |       1.08682  |   0.100106 |
| solution-1-flask   |     0.463227 |       1.00936  |   0.225456 |
| solution-pl        |     0.457763 |       0.160915 |   0.236076 |
| solution-aron-mark |     4.94053  |       0.158665 |   0.238098 |
| solution-1         |     8.95921  |       1e-06    |   0.632833 |
| solution-2         |     0.457183 |       0.712692 |   1.64168  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.428165 |       0.155385 |   0.352196 |
| solution-aron-mark |     0.446893 |       0.15301  |   0.3563   |
| solution-flask     |     0.447199 |       1.00918  |   0.393364 |
| solution-1-flask   |     0.432133 |       1.0089   |   0.716021 |
| solution-2         |     0.432015 |       0.531955 |  11.7189   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.426114 |       0.158623 |    1.0335  |
| solution-aron-mark |     0.443981 |       0.161541 |    1.05314 |
| solution-flask     |     0.425309 |       1.00909  |    1.64577 |
| solution-1-flask   |     0.432064 |       1.00914  |    5.59982 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434843 |       0.186567 |    3.60168 |
| solution-aron-mark |     0.429807 |       0.185132 |    3.60785 |
| solution-flask     |     0.448583 |       1.00932  |    5.29283 |