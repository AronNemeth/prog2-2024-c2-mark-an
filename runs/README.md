# 2026-02-09

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.72493  |       1.07733  |   0.100783 |
| solution-pl        |     0.437876 |       0.166809 |   0.246759 |
| solution-aron-mark |     0.437424 |       0.167101 |   0.250114 |
| solution-1-flask   |     0.440701 |       1.00832  |   0.257363 |
| solution-1         |     7.77695  |       1e-06    |   0.656326 |
| solution-2         |     4.77659  |       0.591509 |   1.51657  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.442283 |       0.16736  |   0.378752 |
| solution-pl        |     0.4412   |       0.166763 |   0.38364  |
| solution-flask     |     0.436959 |       1.00862  |   0.401377 |
| solution-1-flask   |     0.441953 |       1.00821  |   0.793172 |
| solution-2         |     0.436893 |       0.50317  |   2.02772  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438015 |       0.172532 |    1.10342 |
| solution-pl        |     0.444646 |       0.170182 |    1.10573 |
| solution-flask     |     0.438674 |       1.00837  |    1.56566 |
| solution-1-flask   |     0.4403   |       1.00826  |    5.58271 |
| solution-2         |     0.434138 |       0.579603 |  297.329   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.4366   |       0.200067 |    3.79587 |
| solution-aron-mark |     0.438576 |       0.198355 |    3.83659 |
| solution-flask     |     0.438592 |       1.00839  |    5.11269 |