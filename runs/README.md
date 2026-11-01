# 2026-11-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.381315 |       1.00651  |   0.073743 |
| solution-aron-mark |     2.96159  |       0.134409 |   0.190937 |
| solution-pl        |     0.344078 |       0.134321 |   0.197753 |
| solution-1-flask   |     1.2567   |       1.0709   |   0.20962  |
| solution-1         |     6.57292  |       1e-06    |   0.491966 |
| solution-2         |     4.33333  |       0.44532  |   0.832335 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.36305  |       1.00703  |   0.177474 |
| solution-pl        |     0.362151 |       0.142281 |   0.310761 |
| solution-aron-mark |     0.374403 |       0.151433 |   0.320912 |
| solution-1-flask   |     0.37313  |       1.0067   |   0.649057 |
| solution-2         |     0.35871  |       0.433327 |   2.3643   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.364873 |       1.00738  |   0.863079 |
| solution-pl        |     0.365968 |       0.152515 |   0.960576 |
| solution-aron-mark |     0.368557 |       0.151265 |   0.986667 |
| solution-1-flask   |     0.367593 |       1.00691  |   5.22551  |
| solution-2         |     0.378334 |       0.498419 | 168.699    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.377021 |       0.181929 |    3.64616 |
| solution-pl        |     0.363286 |       0.174587 |    3.65631 |
| solution-flask     |     0.356242 |       1.00667  |    3.97377 |