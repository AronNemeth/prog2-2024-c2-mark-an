# 2026-02-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.35181  |       1.04102  |   0.099269 |
| solution-aron-mark |     0.435742 |       0.144319 |   0.223571 |
| solution-pl        |     0.440278 |       0.143922 |   0.228016 |
| solution-1-flask   |     0.43964  |       1.00801  |   0.259696 |
| solution-1         |     7.94922  |       1e-06    |   0.825179 |
| solution-2         |     4.64804  |       0.708568 |   1.46615  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.479854 |       0.145483 |   0.354642 |
| solution-pl        |     0.437676 |       0.146808 |   0.370087 |
| solution-flask     |     0.437329 |       1.00821  |   0.376623 |
| solution-1-flask   |     0.440976 |       1.00833  |   0.803088 |
| solution-2         |     0.433908 |       0.496204 |   1.8      |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.434358 |       0.150903 |    1.05654 |
| solution-pl        |     0.437077 |       0.151157 |    1.05994 |
| solution-flask     |     0.436758 |       1.00825  |    1.53821 |
| solution-1-flask   |     0.441964 |       1.00822  |    5.49894 |
| solution-2         |     0.433934 |       0.551251 |  300.173   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.435793 |       0.176807 |    3.59354 |
| solution-pl        |     0.436008 |       0.176906 |    3.66029 |
| solution-flask     |     0.434276 |       1.00821  |    4.9939  |