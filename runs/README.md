# 2025-07-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.68747  |       1.10677  |   0.101531 |
| solution-pl        |     0.507568 |       0.152387 |   0.238938 |
| solution-aron-mark |     4.54208  |       0.147844 |   0.239483 |
| solution-1-flask   |     0.505704 |       1.00799  |   0.268057 |
| solution-1         |     7.88709  |       1e-06    |   0.665936 |
| solution-2         |     0.498665 |       0.616738 |   0.825459 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.505596 |       0.15171  |   0.36065  |
| solution-pl        |     0.497399 |       0.151527 |   0.36307  |
| solution-flask     |     0.499639 |       1.00833  |   0.377279 |
| solution-1-flask   |     0.530392 |       1.00826  |   0.795906 |
| solution-2         |     0.496173 |       0.506345 |   5.5217   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.5037   |       0.157917 |    1.06338 |
| solution-aron-mark |     0.508019 |       0.158088 |    1.08227 |
| solution-flask     |     0.50242  |       1.00836  |    1.59665 |
| solution-1-flask   |     0.510719 |       1.00856  |    5.72338 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.506363 |       0.191276 |    3.22476 |
| solution-pl        |     0.504942 |       0.189457 |    3.23564 |
| solution-flask     |     0.505707 |       1.0083   |    5.12665 |