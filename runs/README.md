# 2026-05-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.26739  |       1.06034  |   0.108449 |
| solution-pl        |     0.411368 |       0.136889 |   0.215174 |
| solution-aron-mark |     6.30486  |       0.143882 |   0.215646 |
| solution-1-flask   |     0.409322 |       1.00638  |   0.238488 |
| solution-1         |     7.47805  |       2e-06    |   0.831508 |
| solution-2         |     0.416247 |       0.629694 |   0.901882 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.404613 |       0.138975 |   0.334369 |
| solution-pl        |     0.404611 |       0.135914 |   0.337032 |
| solution-flask     |     0.409853 |       1.00676  |   0.453942 |
| solution-1-flask   |     0.4029   |       1.00663  |   0.731968 |
| solution-2         |     0.404813 |       0.493601 |   3.60668  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.402411 |       0.144403 |    1.08181 |
| solution-aron-mark |     0.398407 |       0.143427 |    1.08729 |
| solution-flask     |     0.408513 |       1.00638  |    1.91386 |
| solution-1-flask   |     0.408933 |       1.00667  |    5.57359 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.40368  |       0.174304 |    5.01279 |
| solution-pl        |     0.409134 |       0.172502 |    5.1528  |
| solution-flask     |     0.401222 |       1.00679  |    6.35466 |