# Move Commits to Another Branch

To move recent N commits from branch A to branch B:

1. Create a new branch B from branch A or merge branch A to an existing branch B, so that branch B will have the recent commits from branch A.

2. In branch A, reset N recent commits:

  ```console
  git reset --hard HEAD~<N+1>
  ```
