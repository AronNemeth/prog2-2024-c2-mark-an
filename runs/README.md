# 2026-06-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.13282  |       1.06117  |   0.106338 |
| solution-1-flask   |     0.430274 |       1.00867  |   0.225775 |
| solution-aron-mark |     0.42991  |       0.149128 |   0.228814 |
| solution-pl        |     6.08456  |       0.1708   |   0.229407 |
| solution-1         |     7.51879  |       1e-06    |   0.630353 |
| solution-2         |     0.412469 |       0.758394 |   1.10516  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430578 |       0.152204 |   0.348621 |
| solution-pl        |     0.427659 |       0.152205 |   0.354778 |
| solution-flask     |     0.424251 |       1.00873  |   0.395298 |
| solution-1-flask   |     0.431756 |       1.00887  |   0.711866 |
| solution-2         |     0.423838 |       0.508135 |   3.46843  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.439426 |       0.170596 |    1.04408 |
| solution-pl        |     0.430807 |       0.157549 |    1.04838 |
| solution-flask     |     0.42724  |       1.00896  |    1.65635 |
| solution-1-flask   |     0.440667 |       1.00907  |    5.52592 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.432136 |       0.183899 |    3.83551 |
| solution-aron-mark |     0.426397 |       0.182089 |    3.90201 |
| solution-flask     |     0.427855 |       1.00937  |    5.20017 |