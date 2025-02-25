# 2025-02-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.569328 |       1.00932  |   0.082293 |
| solution-pl        |     1.92552  |       0.165721 |   0.216614 |
| solution-aron-mark |     0.566349 |       0.146595 |   0.223368 |
| solution-1-flask   |     5.2099   |       1.07787  |   0.278788 |
| solution-1         |     7.67025  |       1e-06    |   0.630292 |
| solution-2         |     0.571458 |       0.577824 |   1.53619  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.587998 |       1.00936  |   0.304425 |
| solution-pl        |     0.582695 |       0.158069 |   0.32371  |
| solution-aron-mark |     0.599481 |       0.154557 |   0.329717 |
| solution-1-flask   |     0.586038 |       1.00915  |   0.840391 |
| solution-2         |     0.584795 |       0.565488 |   2.47116  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.574874 |       0.161094 |   0.940716 |
| solution-pl        |     0.579207 |       0.163627 |   0.955538 |
| solution-flask     |     0.580013 |       1.00927  |   1.2699   |
| solution-1-flask   |     0.603575 |       1.0089   |   6.0962   |
| solution-2         |     0.582142 |       0.621948 |  38.3472   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.590141 |       0.19276  |    3.22427 |
| solution-aron-mark |     0.582695 |       0.193022 |    3.23524 |
| solution-flask     |     0.606568 |       1.00928  |    4.61865 |