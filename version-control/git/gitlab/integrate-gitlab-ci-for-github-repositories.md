# Integrate GitLab CI for GitHub Repositories

With the help of [GitLab CI/CD for External Repositories](https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/), we can use GitLab CI/CD for a GitHub Repo.

1. On GitHub, generate a [personal access token](https://github.com/settings/tokens) with at least the `repo` scope.

2. Create a new GitLab project, choose `CI/CD for external repo`. Use the personal access token to select the GitHub repo. The mirror repo info should be found in `Settings > Repository > Mirroring repositories`.

3. Create a `.gitlab-ci.yml` in the root directory (default path) of the GitHub repo. The push will trigger the pipeline with a shared runner (enabled by default).
