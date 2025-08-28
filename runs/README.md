# 2025-08-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.496314 |       1.00831  |   0.095959 |
| solution-aron-mark |     0.542407 |       0.15832  |   0.24104  |
| solution-pl        |     5.8632   |       0.205251 |   0.242453 |
| solution-1-flask   |     1.10653  |       1.06181  |   0.269731 |
| solution-1         |     8.22092  |       1e-06    |   0.676251 |
| solution-2         |     0.496223 |       0.651134 |   1.38695  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48032  |       0.154733 |   0.3614   |
| solution-aron-mark |     0.479477 |       0.153697 |   0.362767 |
| solution-flask     |     0.508826 |       1.00847  |   0.376988 |
| solution-1-flask   |     0.48959  |       1.00829  |   0.803112 |
| solution-2         |     0.482793 |       0.500124 |  17.3324   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.508587 |       0.169175 |    1.0733  |
| solution-pl        |     0.521619 |       0.166801 |    1.08989 |
| solution-flask     |     0.50545  |       1.00867  |    1.56433 |
| solution-1-flask   |     0.513402 |       1.00879  |    5.72629 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.502954 |       0.200269 |    3.36412 |
| solution-pl        |     0.502479 |       0.202497 |    3.36968 |
| solution-flask     |     0.49897  |       1.00853  |    5.25714 |